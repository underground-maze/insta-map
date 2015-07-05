from django.conf import settings
from django.core.urlresolvers import reverse

from helpers.tests import InstaTransactionTestCase
from cards.models import Card


class AddCardViewTestCase(InstaTransactionTestCase):

    """ Tests for add card view check """

    def setUp(self):
        self.url = reverse('card:add')
        self.ajax_kwargs = dict(HTTP_X_REQUESTED_WITH='XMLHttpRequest')

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
        # check is very long field value
        data = dict(position='a' * 1001)
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertEqual(response['errors']['position'], [
            'Убедитесь, что это значение содержит не более 1000 символов (сейчас 1001).'])
        # check correct
        data = dict(position='(44.61979915773973, 33.52958679199219)')
        response = self.json_response(self.client.post(self.url, data=data, **self.ajax_kwargs), 400)
        self.assertNotIn('position', response['errors'])
