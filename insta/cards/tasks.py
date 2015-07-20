from celery import shared_task

from helpers.youtube import upload_video
from helpers.service import site_update

from cards.models import Card


@shared_task
def upload_on_youtube_task(card):
    upload_video(card)


@shared_task
def send_message_task(function, instance):
    function(instance)


@shared_task
def site_update_task(template_name='index.html'):
    active = Card.active.all()
    site_update(active, template_name)
