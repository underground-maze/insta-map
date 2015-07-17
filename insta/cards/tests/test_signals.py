from django.core import mail
from django.conf import settings

from helpers.tests import InstaTransactionTestCase
from cards.models import Card


class TestCardSignals(InstaTransactionTestCase):

    """ Testing an Card signals """

    model = Card

    def setUp(self):
        self._create_user()
        # create kwargs for spares request model
        self.kwargs = dict(
            user=self.user, position='44.33,33.44', video='video.mov',
            youtube_id='123456', description='Тестовое описание.', )

    def test_new_card_email(self):
        """ Check is send email to staff when new card are created """
        self.assertEquals(len(mail.outbox), 0)
        # create supeuser
        self._create_admin_and_login()
        # create card
        card = Card.objects.create(**self.kwargs)
        # check email was send
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals('Новое открытие / Я первооткрыватель!', mail.outbox[0].subject)
        self.assertEquals(settings.DEFAULT_FROM_EMAIL, mail.outbox[0].from_email)
        self.assertEquals(['admin@test.com', ], mail.outbox[0].to)
        self.assertIn('http://revealer.ru/admin/cards/card/{}/'.format(card.pk), mail.outbox[0].body)
        self.assertIn('multipart/alternative', mail.outbox[0].message()['Content-Type'])

    def test_accepted_card_email(self):
        """ Check is send email to user when card are accepted """
        self.assertEquals(len(mail.outbox), 0)
        # create card and change status
        card = Card.objects.create(**self.kwargs)
        card.status = Card.STATUS_ACCEPTED
        card.save()
        # check email was send
        self.assertEquals(len(mail.outbox), 1)
        self.assertEquals('Открытие подтверждено / Я первооткрыватель!', mail.outbox[0].subject)
        self.assertEquals(settings.DEFAULT_FROM_EMAIL, mail.outbox[0].from_email)
        self.assertEquals(['user@test.com', ], mail.outbox[0].to)
        self.assertIn('http://revealer.ru/?card={}'.format(card.pk), mail.outbox[0].body)
        self.assertIn('multipart/alternative', mail.outbox[0].message()['Content-Type'])
