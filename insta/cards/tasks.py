from celery import shared_task
from helpers.youtube import upload_video


@shared_task
def upload_on_youtube_task(card):
    upload_video(card)
