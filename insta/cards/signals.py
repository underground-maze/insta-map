import json

from django.db.models.signals import post_save, pre_save
from django.utils.html import strip_tags

from cards.models import Card
from cards.tasks import upload_on_youtube_task

from helpers.coordinates import get_map_polygons, get_map_markers
from helpers.service import write_js, render_to_file
from helpers.emails import send_accepted_card_message


def escape_tags(sender, instance, **kwargs):
    """ Signal for remove tags from description """
    instance.description = strip_tags(instance.description)


def upload_on_youtube(sender, instance, **kwargs):
    """ Signal for async upload video on youtube """
    if not instance.youtube_id:
        upload_on_youtube_task.delay(instance)
        instance.youtube_id = 'uploading...'
        instance.save()


def delete_video(sender, instance, **kwargs):
    """ Signal for delete permanent video file """
    if not instance.is_new:
        instance.video.delete(False)


def update_coord_js(sender, instance, **kwargs):
    """ Resave the fog of war map js """
    if not instance.is_new:
        # get coord of all active cards
        active = Card.active.all()
        # get js representation of card polygons
        polygons = get_map_polygons([card.as_tuple() for card in active])
        markers = get_map_markers([card.as_dict() for card in active])
        markers_data = json.dumps({card.pk: card.as_dict() for card in active})
        # write the script into file
        write_js(polygons, markers, markers_data)
        render_to_file('index.html', {}, 'index.html')


def email_notify_accepted(sender, instance, **kwargs):
    """ Sent notification to user if card is accepted """
    if not instance.pk or not instance.is_accepted:
        return
    instance_db = Card.objects.get(pk=instance.pk)
    if not instance_db.is_accepted:
        send_accepted_card_message(instance)


pre_save.connect(escape_tags, sender=Card)
post_save.connect(upload_on_youtube, sender=Card)
post_save.connect(update_coord_js, sender=Card)
pre_save.connect(delete_video, sender=Card)
pre_save.connect(email_notify_accepted, sender=Card)
