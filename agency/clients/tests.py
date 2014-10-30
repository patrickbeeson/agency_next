from django.test import TestCase
import tempfile
import os
from settings import base
from clients.models import Client


class ClientTest(TestCase):

    def setUp(self):
        tempfile.tempdir = os.path.join(base.MEDIA_ROOT, 'clients/logos')
        tf = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
        tf.close()
        self.logo = tf.name
        Client.objects.create(
            name='Coca-Cola',
            logo=self.logo,
            website='http://us.coca-cola.com/home/'
        )

    def test_can_create_client(self):
        client = Client.objects.get(name='Coca-Cola')
        expected = 'Coca-Cola'
        self.assertEqual(client.name, expected)

    def tearDown(self):
        os.remove(self.logo)
        clients = Client.objects.all()
        clients.delete()
