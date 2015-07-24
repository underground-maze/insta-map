import random
import json
import time
import traceback
import subprocess

import http
import httplib2

import urllib
import urllib.request

from apiclient.discovery import build
from apiclient.errors import HttpError
from apiclient.http import MediaFileUpload

from oauth2client.client import AccessTokenCredentials

from django.conf import settings

from cards.models import YoutubeLogger


# Explicitly tell the underlying HTTP transport library not to retry, since we are handling retry logic ourselves.
httplib2.RETRIES = 1

# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (
    httplib2.HttpLib2Error, IOError, http.client.NotConnected,
    http.client.IncompleteRead, http.client.ImproperConnectionState,
    http.client.CannotSendRequest, http.client.CannotSendHeader,
    http.client.ResponseNotReady, http.client.BadStatusLine)

# Always retry when an apiclient.errors.HttpError with one of these status codes is raised.
RETRIABLE_STATUS_CODES = (500, 502, 503, 504)


def get_auth_code():
    """ Get access token for connect to youtube api """
    oauth_url = 'https://accounts.google.com/o/oauth2/token'
    # create post data
    data = dict(
        refresh_token=settings.YOUTUBE_REFRESH_TOKEN, grant_type='refresh_token',
        client_id=settings.YOUTUBE_CLIENT_ID, client_secret=settings.YOUTUBE_CLIENT_SECRET, )
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'Accept': 'application/json'}
    data = urllib.parse.urlencode(data).encode('utf-8')
    # make request and take response
    request = urllib.request.Request(oauth_url, data=data, headers=headers)
    response = urllib.request.urlopen(request)
    # get access_token from response
    response = json.loads(response.read().decode('utf-8'))
    return response['access_token']


def get_authenticated_service():
    """ Create youtube oauth2 connection """
    # make credentials with refresh_token auth
    credentials = AccessTokenCredentials(access_token=get_auth_code(), user_agent='insta-python/1.0')
    # create httplib proxy connection
    if settings.USE_PROXY:
        import socks
        # set socks proxy to ssh tunnel
        socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, 'localhost', 1080)
        # wrap httplib via proxy
        socks.wrapmodule(httplib2)
    # create connection to youtube api
    return build(
        settings.YOUTUBE_API_SERVICE_NAME, settings.YOUTUBE_API_VERSION, http=credentials.authorize(httplib2.Http()))


def initialize_upload(youtube, card):
    """ Create youtube upload data """
    # create video meta data
    body = card.youtube_meta_data()
    # Call the API's videos.insert method to create and upload the video
    insert_request = youtube.videos().insert(
        part=",".join(body.keys()), body=body,
        media_body=MediaFileUpload(card.video.path, chunksize=settings.YOUTUBE_CHUNKSIZE, resumable=True))
    # wait for file uploading
    return resumable_upload(insert_request)


def resumable_upload(insert_request):
    response = None
    error = None
    retry = 0
    while response is None:
        try:
            status, response = insert_request.next_chunk()
            if 'id' in response:
                return response['id']
        except HttpError as err:
            if err.resp.status in RETRIABLE_STATUS_CODES:
                error = True
            else:
                raise
        except RETRIABLE_EXCEPTIONS:
            error = True

        if error:
            retry += 1
            if retry > MAX_RETRIES:
                raise Exception('Maximum retry are fail')

            sleep_seconds = random.random() * 2 ** retry
            time.sleep(sleep_seconds)


def upload_video(card):
    try:
        if settings.USE_PROXY:
            # init ssh tunnel connection
            subprocess.Popen(['ssh', '-fN', '-D', '1080', 'forward@wbmonster'])
            # wait some time while connection established
            time.sleep(10)
        # try to upload video
        video_id = initialize_upload(get_authenticated_service(), card)
        # if failed uploading raise error
        if video_id is None:
            raise Exception('Video ID is None')
        # if not any error occured remove video file from server
        card.video.delete(False)
        # if success uploading save video id to card
        card.youtube_id = video_id
        card.save()
    except Exception as error:
        # save youtube log model with error
        description = 'TRACEBACK:\n{trace}\n---\n\nEXCEPTION:\n{exc}'.format(
            trace=traceback.format_exc(), exc=str(error.args))
        kwargs = dict(card=card, status=YoutubeLogger.STATUS_ERRORED, description=description)
    else:
        # save youtube log model with success
        kwargs = dict(card=card, status=YoutubeLogger.STATUS_SUCCESS, description=card.video_url)
    finally:
        YoutubeLogger.objects.create(**kwargs)
        if settings.USE_PROXY:
            # remove socks default proxy
            socks._defaultproxy = None
            # desctroy ssh tunnel connection
            subprocess.Popen(['pkill', '-f', 'forward@wbmonster'])
            # wait some time while connection will closed
            time.sleep(10)
