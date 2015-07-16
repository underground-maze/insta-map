import http
import json
import os
from io import BytesIO

from django.test import TransactionTestCase
from accounts.models import InstaUser


class InstaTransactionTestCase(TransactionTestCase):

    reset_sequences = True

    def assert200(self, response):
        return self.assertEqual(response.status_code, http.client.OK)

    def assert302(self, response):
        return self.assertEqual(response.status_code, http.client.FOUND)

    def _create_admin_and_login(self):
        self.adminuser = InstaUser.objects.create_superuser('admin', 'admin@test.com', 'pass')
        response = self.client.post('/admin/login/', dict(username='admin', password='pass'))
        self.assert302(response)

    def _create_user(self):
        self.user = InstaUser.objects.create_user('user', 'user@test.com', 'pass')

    def create_stream(self, file_format, size):
        """ Create temporary stream """
        data = b'*' * size
        data_io = BytesIO(data)
        data_io.seek(0, os.SEEK_END)
        data_io.size = data_io.tell()
        data_io.name = 'video' + file_format
        data_io.seek(0)
        return data_io

    def json_response(self, response, status_code):
        self.assertEqual(response.status_code, status_code)
        return json.loads(response.content.decode('utf-8'))
