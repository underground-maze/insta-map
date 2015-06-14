from django.db.models.signals import post_save, pre_save
from django.utils.html import strip_tags

from cards.models import Card
from cards.tasks import upload_on_youtube_task


def escape_tags(sender, instance, **kwargs):
    """ Signal for remove tags from description """
    instance.description = strip_tags(instance.description)


def upload_on_youtube(sender, instance, **kwargs):
    """ Signal for async upload video on youtube """
    if not instance.youtube_id:
        upload_on_youtube_task.delay(instance)


pre_save.connect(escape_tags, sender=Card)
post_save.connect(upload_on_youtube, sender=Card)
