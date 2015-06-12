from http import client

from django.test import TransactionTestCase
from django.core.urlresolvers import reverse


class IndexTestCase(TransactionTestCase):

    """ Test index app """

    def setUp(self):
        self.url = reverse('index')

    def test_index_available_get(self):
        """ Check is index page has 200 status code """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, client.OK)

    def test_index_disallow_post(self):
        """ Check is index page has 405 status code """
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, client.METHOD_NOT_ALLOWED)

    def test_index_url_resolve(self):
        """ Check is index correct url """
        self.assertEqual(self.url, '/')
