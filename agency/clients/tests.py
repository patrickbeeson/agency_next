from django.test import TestCase
import tempfile
import os
from settings import base
from clients.models import Client
from django.core.exceptions import ValidationError


class ClientTest(TestCase):

    def setUp(self):
        tempfile.tempdir = os.path.join(base.MEDIA_ROOT, 'clients/logos')
        tf = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        tf_invalid = tempfile.NamedTemporaryFile(delete=False, suffix='.gif')
        tf_invalid.close()
        tf.close()
        self.logo = tf.name
        self.invalid_logo = tf_invalid.name
        Client.objects.create(
            name='Coca-Cola',
            logo=self.logo,
            website='http://us.coca-cola.com/home/'
        )
        Client.objects.create(
            name='Django',
            logo=self.invalid_logo,
            website='http://djangoproject.com'
        )

    def test_can_create_client(self):
        client = Client.objects.get(name='Coca-Cola')
        expected = 'Coca-Cola'
        self.assertEqual(client.name, expected)

    def test_invalid_file_type(self):
        client = Client.objects.get(name='Django')
        self.assertRaises(ValidationError, client.full_clean)

    def tearDown(self):
        os.remove(self.logo)
        os.remove(self.invalid_logo)
        clients = Client.objects.all()
        clients.delete()
