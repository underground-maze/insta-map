from django.db.models.signals import post_save, pre_save
from django.utils.html import strip_tags

from cards.models import Card
from cards.tasks import upload_on_youtube_task, send_message_task, site_update_task

from helpers.emails import send_accepted_card_message, send_new_card_message


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


def update_main_page(sender, instance, **kwargs):
    """ Resave the fog of war map js """
    if not instance.is_new:
        site_update_task.delay()


def email_notify_accepted(sender, instance, **kwargs):
    """ Sent notification to user if card is accepted """
    # for new card - instance hasn't pk
    if not instance.pk or not instance.is_accepted:
        return
    instance_db = Card.objects.get(pk=instance.pk)

    if instance_db.status != instance.status:
        # async send msg
        send_message_task.delay(send_accepted_card_message, instance)


def email_notify_new(sender, instance, **kwargs):
    """ Sent notification to staff if card is created """
    if kwargs['created']:
        # async send msg
        send_message_task.delay(send_new_card_message, instance)


pre_save.connect(escape_tags, sender=Card)
post_save.connect(upload_on_youtube, sender=Card)
post_save.connect(update_main_page, sender=Card)
pre_save.connect(delete_video, sender=Card)
pre_save.connect(email_notify_accepted, sender=Card)
post_save.connect(email_notify_new, sender=Card)
