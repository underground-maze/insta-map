import http

from django.test import TransactionTestCase
from django.contrib.auth.models import User


class InstaTransactionTestCase(TransactionTestCase):

    reset_sequences = True

    def assert200(self, response):
        return self.assertEqual(response.status_code, http.client.OK)

    def assert302(self, response):
        return self.assertEqual(response.status_code, http.client.OK)

    def _create_admin_and_login(self):
        self.adminuser = User.objects.create_superuser('admin', 'admin@test.com', 'pass')
        response = self.client.post('/admin/login/', dict(username='admin', password='pass'))
        self.assert302(response)

    def _create_user(self):
        self.user = User.objects.create_user('user', 'user@test.com', 'pass')
