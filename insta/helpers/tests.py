import http
import os
from io import BytesIO

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

    def create_stream(self, file_format, size):
        """ Create temporary stream """
        data = b'*' * size
        data_io = BytesIO(data)
        data_io.seek(0, os.SEEK_END)
        data_io.size = data_io.tell()
        data_io.name = 'video' + file_format
        data_io.seek(0)
        return data_io
