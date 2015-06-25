from django.db.models.signals import post_save, pre_save
from django.utils.html import strip_tags

from cards.models import Card
from cards.tasks import upload_on_youtube_task

from helpers.coordinates import get_map_js
from helpers.service import write_js


def escape_tags(sender, instance, **kwargs):
    """ Signal for remove tags from description """
    instance.description = strip_tags(instance.description)


def upload_on_youtube(sender, instance, **kwargs):
    """ Signal for async upload video on youtube """
    if not instance.youtube_id:
        upload_on_youtube_task.delay(instance)
        instance.youtube_id = 'uploading...'
        instance.save()

def update_coord_js(sender, instance, **kwargs):
    """ Resave the fog of war map js """
    if not instance.is_new:
        # get coord of all active cards
        points = [card.as_tuple() for card in Card.active.all()]
        # get js representation of card polygons
        js_string = get_map_js(points)
        # write the script into file
        write_js(js_string)


pre_save.connect(escape_tags, sender=Card)
post_save.connect(upload_on_youtube, sender=Card)
post_save.connect(update_coord_js, sender=Card)
