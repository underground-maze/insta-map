from django.conf import settings
from django.core.urlresolvers import reverse

from helpers.tests import InstaTransactionTestCase
from cards.models import Card


class AddCardViewTestCase(InstaTransactionTestCase):

    """ Tests for add card view check """

    def setUp(self):
        self.url = reverse('card:add')
        self.ajax_kwargs = dict(HTTP_X_REQUESTED_WITH='XMLHttpRequest')
        self._create_admin_and_login()

    def test_url_resolved(self):
        """ Check url reverse correct """
        self.assertEqual(self.url, '/cards/add')

    def test_add_card_access(self):
        """ Check is allowed only for ajax request """
        # check get request
        response = self.json_response(self.client.get(self.url), 403)
        self.assertEqual('Forbidden', response['message'])
        # check post request
        response = self.json_response(self.client.post(self.url), 403)
        self.assertEqual('Forbidden', response['message'])
        # check ajax request get
        # 200 get Ok
        response = self.json_response(self.client.get(self.url, **self.ajax_kwargs), 200)
        self.assertNotIn('message', response)
        # check ajax request post
        # 400 cause form invalid
        response = self.json_response(self.client.post(self.url, **self.ajax_kwargs), 400)
        self.assertNotIn('message', response)

    def test_add_card_view_get(self):
        """ Check is correct process get request """
        response = self.json_response(self.client.get(self.url, **self.ajax_kwargs), 200)
        self.assertIn('csrf_token', response)

    def test_add_card_form_validation_description(self):
        """ Check form validation for field 'description' """
        # check is required field not provided
        data = dict()
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertEqual(response['errors']['description'], ['Обязательное поле.'])
        # check is required field empty value
        data = dict(description='                          ')
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertEqual(response['errors']['description'], ['Обязательное поле.'])
        # check is very long field value
        data = dict(description='a' * 1001)
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertEqual(response['errors']['description'], [
            'Убедитесь, что это значение содержит не более 1000 символов (сейчас 1001).'])
        # check correct
        data = dict(description='test description')
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertNotIn('description', response['errors'])

    def test_add_card_form_validation_position(self):
        """ Check form validation for field 'position' """
        # check is required field not provided
        data = dict()
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertEqual(response['errors']['position'], ['Обязательное поле.'])
        # check is required field empty value
        data = dict(position='                          ')
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertEqual(response['errors']['position'], ['Обязательное поле.'])
        # check correct
        data = dict(position='(44.61979915773973, 33.52958679199219)')
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertNotIn('position', response['errors'])

    def test_add_card_form_validation_email(self):
        """ Check form validation for field 'email' """
        # # check is required field not provided
        # data = dict()
        # response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        # self.assertEqual(response['errors']['email'], ['Обязательное поле.'])
        # # check is required field empty value
        # data = dict(email='                          ')
        # response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        # self.assertEqual(response['errors']['email'], ['Обязательное поле.'])
        # check is very long field value
        data = dict(email=('a' * 1001) + '@e.co')
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertEqual(response['errors']['email'], [
            'Убедитесь, что это значение содержит не более 200 символов (сейчас 1006).'])
        # check invalide email
        data = dict(email='not_email@dddd')
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertEqual(response['errors']['email'], ['Введите корректный адрес электронной почты.'])
        # check correct
        data = dict(email='user@e.co')
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertNotIn('email', response['errors'])

    def test_add_card_form_validation_video(self):
        """ Check form validation for field 'video' """
        settings.VIDEO_MIN_SIZE = 1
        settings.VIDEO_MAX_SIZE = 5
        # check is required field not provided
        data = dict()
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertEqual(response['errors']['video'], ['Обязательное поле.'])
        # check is very big file
        data = dict(video=self.create_stream('.mov', settings.VIDEO_MAX_SIZE))
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertEqual(response['errors']['video'], ['Недопустимый размер файла.'])
        # check is very small file
        data = dict(video=self.create_stream('.mov', settings.VIDEO_MIN_SIZE))
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertEqual(response['errors']['video'], ['Недопустимый размер файла.'])
        # check is incorrect video file
        data = dict(video=self.create_stream('.cow', 3))
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertEqual(response['errors']['video'], ['Неверный формат видео.'])
        # check correct
        data = dict(video=self.create_stream('.mov', 3))
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertNotIn('video', response['errors'])

    def test_correct_create_card(self):
        """ Check is correct bind to request user are """
        # check is not created are
        self.assertEqual(Card.objects.all().count(), 0)
        # prepare data
        settings.VIDEO_MIN_SIZE = 1
        settings.VIDEO_MAX_SIZE = 5
        data = dict(
            video=self.create_stream('.mov', 3),
            position='(44.61979915773973, 33.52958679199219)',
            description='test description', )
        data.update({'g-recaptcha-response': 'PASSED'})
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 200)
        # check creates
        self.assertEqual(Card.objects.all().count(), 1)
        card = Card.objects.first()
        # check card
        self.assertEqual(card.user, self.adminuser)
        self.assertEqual(card.radius, 3)
        self.assertEqual(card.description, 'test description')
        self.assertEqual(str(card.position), '44.61979915773973,33.52958679199219')
        self.assertEqual(str(card.position.latitude), '44.61979915773973')
        self.assertEqual(str(card.position.longitude), '33.52958679199219')
        self.assertTrue(card.video)
