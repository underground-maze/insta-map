from django.template.loader import render_to_string
from django.core.mail.message import EmailMultiAlternatives
from django.utils.html import strip_tags
from django.conf import settings

from accounts.models import InstaUser


def _send_message(to_emails, subject, email_template, email_ctx):
    """ Render and send email """
    # render email message
    html_content = render_to_string(email_template, email_ctx)
    msg = EmailMultiAlternatives(
        subject='{} / Я первооткрыватель!'.format(subject),
        body=strip_tags(html_content),
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=to_emails, )
    msg.attach_alternative(html_content, 'text/html')
    # send messages
    msg.send(fail_silently=True)


def send_new_card_message(instance):
    """ Send notification to all staff users about new card created """
    # validate is need to send
    if not instance.is_new:
        return
    # get filter all staff user emails
    emails = InstaUser.objects.values_list('email', flat=True).filter(is_staff=True)
    # create context
    email_ctx = dict(instance=instance, support_email=settings.DEFAULT_FROM_EMAIL, site_url=settings.SITE_URL, )
    # render and send email
    _send_message(emails, 'Новое открытие', 'emails/new_card.html', email_ctx)


def send_accepted_card_message(instance):
    """ Send notification to user about accepted his card """
    email = instance.user.email
    # validate is need to send
    if not instance.is_accepted or not email:
        return
    # create context
    email_ctx = dict(instance=instance, support_email=settings.DEFAULT_FROM_EMAIL, site_url=settings.SITE_URL, )
    # render and send email
    _send_message([email], 'Открытие подтверждено', 'emails/active_card.html', email_ctx)
