from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.conf import settings

from geoposition.fields import GeopositionField

from helpers.service import video_path
from helpers.youtube import upload_video


class CardActiveManager(models.Manager):

    """ Manager to get all active cards instance """

    def get_queryset(self):
        return super().get_queryset().filter(status=Card.STATUS_ACCEPTED)


class Card(models.Model):

    """ Card place model class """

    STATUS_NEW = 'new'
    STATUS_ACCEPTED = 'accepted'
    STATUS_REJECTED = 'rejected'

    STATUS_CHOICES = (
        (STATUS_NEW, 'Не проверено'),
        (STATUS_ACCEPTED, 'Принято'),
        (STATUS_REJECTED, 'Отклонено'), )

    user = models.ForeignKey(User, verbose_name='Автор')
    position = GeopositionField(verbose_name='Координаты')
    video = models.FileField(verbose_name='Видеофайл', upload_to=video_path)
    youtube_id = models.CharField(verbose_name='ID видео на youtube', blank=True, null=True, max_length=32)
    description = models.TextField(verbose_name='Описание', blank=True, null=True)
    radius = models.PositiveSmallIntegerField(verbose_name='Радиус (км)', default=10)

    # additional fields
    created_at = models.DateTimeField(verbose_name='Дата добавления', default=timezone.now)
    checked_at = models.DateTimeField(verbose_name='Дата проверки', blank=True, null=True)
    status = models.CharField(verbose_name='Статус', choices=STATUS_CHOICES, max_length=10, default=STATUS_NEW)

    # managers
    objects = models.Manager()    # default obj manager
    active = CardActiveManager()  # all active obj manager

    class Meta:
        verbose_name = 'карточка'
        verbose_name_plural = 'карточки'
        ordering = ('-created_at', )

    def __str__(self):
        return '{user} {lat}:{lon}'.format(
            user=self.user.username, lat=self.position.latitude, lon=self.position.longitude)

    @property
    def is_new(self):
        return self.status == self.STATUS_NEW

    @property
    def is_accepted(self):
        return self.status == self.STATUS_ACCEPTED

    @property
    def is_rejected(self):
        return self.status == self.STATUS_REJECTED

    def save(self, *args, **kwargs):
        # set date of check if change status from new - to other and if not checked already
        if not self.checked_at and not self.is_new:
            self.checked_at = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return '?card={id}'.format(id=self.pk)

    def youtube_meta_data(self):
        """ Create metadata dict for youtube video upload """
        return dict(
            snippet=dict(
                title=settings.YOUTUBE_TITLE.format(coord=self.position),
                tags=settings.YOUTUBE_TAGS,
                categoryId=settings.YOUTUBE_CATEGORY_ID,
                description=self.description,
            ),
            status=dict(
                privacyStatus=settings.YOUTUBE_PRIVACY_STATUS,
            ),
            recordingDetails=dict(
                location=dict(
                    latitude=str(self.position.latitude),
                    longitude=str(self.position.longitude),
                ),
            ),
        )

    def upload_on_youtube(self):
        upload_video(self)
