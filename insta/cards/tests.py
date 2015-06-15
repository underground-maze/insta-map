import os
from io import BytesIO

from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
from django.test.client import RequestFactory
from django.conf import settings

from helpers.tests import InstaTransactionTestCase
from cards.models import Card


class TestCardModels(InstaTransactionTestCase):

    """ Testing an Card model """

    model = Card

    def setUp(self):
        self._create_user()
        # create kwargs for spares request model
        self.kwargs = dict(
            user=self.user, position='44.33,33.44', video='video.mov',
            youtube_id='123456', description='Тестовое описание.', )
        self.card = self.model.objects.create(**self.kwargs)
        self.admin_url = reverse('admin:cards_card_changelist')

    def test_verbose_names(self):
        """ Test verbose name for model """
        # create verbose_names dict with correct name of fields
        verbose_names = dict(
            user='Автор', position='Координаты', video='Видеофайл',
            youtube_id='ID видео на youtube', description='Описание', radius='Радиус (км)',
            created_at='Дата добавления', checked_at='Дата проверки', status='Статус', )
        # create counter to check correct number of fields
        counter = 0
        # cycle check verbose names
        for field in verbose_names:
            field = self.model._meta.get_field_by_name(field)[0]
            counter += 1
            self.assertEquals(field.verbose_name, verbose_names[field.name])
        # check is counter has a correct value 1
        self.assertEquals(counter, 9)
        # check class verbose name
        self.assertEquals(self.model._meta.verbose_name, 'карточка')
        self.assertEquals(self.model._meta.verbose_name_plural, 'карточки')
        self.assertEquals(self.model._meta.ordering, ('-created_at', ))

    def test_status(self):
        """ Check status propertyes """
        card = self.card
        # check status
        self.assertEquals(card.status, self.model.STATUS_NEW)
        self.assertTrue(card.is_new)
        self.assertFalse(card.is_accepted)
        self.assertFalse(card.is_rejected)
        # change status to is_confirmed
        card.status = self.model.STATUS_ACCEPTED
        card.save()
        # check status
        self.assertEquals(card.status, self.model.STATUS_ACCEPTED)
        self.assertFalse(card.is_new)
        self.assertTrue(card.is_accepted)
        self.assertFalse(card.is_rejected)
        # change status to is_unwanted
        card.status = self.model.STATUS_REJECTED
        card.save()
        # check status
        self.assertEquals(card.status, self.model.STATUS_REJECTED)
        self.assertFalse(card.is_new)
        self.assertFalse(card.is_accepted)
        self.assertTrue(card.is_rejected)

    def test_checked_at_values(self):
        """ Save model and check values checked_at """
        card = self.card
        self.assertTrue(card.created_at)
        self.assertFalse(card.checked_at)
        # save with checked date
        card.status = self.model.STATUS_ACCEPTED
        card.save()
        self.assertTrue(card.checked_at)
        # set checked at as None and recheck
        card.status = self.model.STATUS_NEW
        card.checked_at = None
        card.save()
        self.assertTrue(card.created_at)
        self.assertFalse(card.checked_at)
        # save with check date
        card.status = self.model.STATUS_REJECTED
        card.save()
        self.assertTrue(card.checked_at)

    def test_object_manager(self):
        """ Check correct work active manager """
        # check counts
        self.assertEquals(self.model.objects.count(), 1)
        self.assertEquals(self.model.active.count(), 0)
        # set value is acepted
        self.model.objects.all().update(status=self.model.STATUS_ACCEPTED)
        # check counts
        self.assertEquals(self.model.objects.count(), 1)
        self.assertEquals(self.model.active.count(), 1)
        # set value is rejected
        self.model.objects.all().update(status=self.model.STATUS_REJECTED)
        # check counts
        self.assertEquals(self.model.objects.count(), 1)
        self.assertEquals(self.model.active.count(), 0)

    def create_stream(self, file_format, size):
        """ Create temporary stream """
        data = b'*' * size
        data_io = BytesIO(data)
        data_io.seek(0, os.SEEK_END)
        data_io.size = data_io.tell()
        data_io.name = 'video' + file_format
        data_io.seek(0)
        return data_io

    def test_video_validate(self):
        """ Check is correct validation video """
        self.assertTrue(settings.VIDEO_MIN_SIZE < settings.VIDEO_MAX_SIZE)
        settings.VIDEO_MIN_SIZE = 1
        settings.VIDEO_MAX_SIZE = 5
        card = self.card
        # check correct ext
        for ext in settings.VIDEO_EXT:
            card.video = self.create_stream(ext, settings.VIDEO_MIN_SIZE + 1)
            card.full_clean()
        # check incorrect ext
        for ext in ('.jpg', '.txt', '.doc'):
            card.video = self.create_stream(ext, settings.VIDEO_MIN_SIZE + 1)
            with self.assertRaises(ValidationError) as validation:
                card.full_clean()
            self.assertEquals(validation.exception.message_dict['video'], ['Неверный формат видео.'])
        # check incorrect size small
        card.video = self.create_stream('.MOV', settings.VIDEO_MIN_SIZE)
        with self.assertRaises(ValidationError) as validation:
            card.full_clean()
        self.assertEquals(validation.exception.message_dict['video'], ['Недопустимый размер файла.'])
        # check incorrect size big
        card.video = self.create_stream('.MOV', settings.VIDEO_MAX_SIZE)
        with self.assertRaises(ValidationError) as validation:
            card.full_clean()
        self.assertEquals(validation.exception.message_dict['video'], ['Недопустимый размер файла.'])
