from django.test import TestCase
import os
import tempfile
from settings import base
from homepage.views import HomePageView
from headlines.models import Headline
from clients.models import Client
from staff.models import Employee
from projects.models import Project


class HomePageTest(TestCase):

    def test_home_page_renders_home_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_home_page_returns(self):
        response = self.client.get('/')
        self.assertEqual(response, 200)


class HomePageHeadlines(TestCase):

    def setUp(self):
        Headline.objects.create(
            headline='Makers, Bakers, Screenprinters, Homebrewers'
        )

    def test_home_page_renders_headline_list(self):
        headline_list = Headline.objects.all()
        response = self.client.get('/')
        self.assertEqual(len(response.context['headline_list']), 1)

    def tearDown(self):
        headlines = Headline.objects.all()
        headlines.delete()


class HomePageClients(TestCase):

    def setUp(self):
        self.path = os.path.join(base.MEDIA_ROOT, 'clients/logos')
        self.logo = os.path.join(
            self.path, os.path.basename(tempfile.mkstemp(suffix='.jpg')[1]))
        Client.objects.create(
            name='Coca-Cola',
            logo=self.logo,
            website='http://us.coca-cola.com/home/'
        )

    def test_home_page_renders_client_list(self):
        client_list = Client.objects.all()
        response = self.client.get('/')
        self.assertEqual(len(response.context['client_list']), 1)

    def tearDown(self):
        os.remove(self.logo)
        clients = Client.objects.all()
        clients.delete()


class HomePageStaff(TestCase):

    def setUp(self):
        self.path = os.path.join(base.MEDIA_ROOT, 'staff/mugshots')
        self.mugshot = os.path.join(
            self.path, os.path.basename(tempfile.mkstemp(suffix='.jpg')[1]))
        Employee.objects.create(
            first_name='Patrick',
            middle_name='Scott',
            last_name='Beeson',
            title='Director of Digital Strategy',
            brief_description='Mountains require grit',
            mugshot=self.mugshot,
            is_employed=True
        )

    def test_home_page_renders_staff_list(self):
        employee_list = Employee.public.all()
        response = self.client.get('/')
        self.assertEqual(len(response.context['employee_list']), 1)

    def tearDown(self):
        os.remove(self.mugshot)
        employees = Employee.objects.all()
        employees.delete()
