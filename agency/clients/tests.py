from django.test import TestCase
import tempfile
import os
from settings import base
from clients.models import Client


class ClientTest(TestCase):

    def setUp(self):
        self.path = os.path.join(base.MEDIA_ROOT, 'clients/logos')
        self.logo = os.path.join(
            self.path, os.path.basename(tempfile.mkstemp(suffix='.jpg')[1]))
        Client.objects.create(
            name='Coca-Cola',
            logo=self.logo,
            website='http://us.coca-cola.com/home/'
        )

    def test_client_name(self):
        client = Client.objects.get(name='Coca-Cola')
        expected = 'Coca-cola'
        self.assertEqual(client.name, expected)

    def tearDown(self):
        os.remove(self.logo)
        clients = Client.objects.all()
        clients.delete()
