from django.test import RequestFactory
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

    def setUp(self):
        self.request = RequestFactory().get('/')
        self.view = HomePageView.as_view()

        Headline.objects.create(
            headline='Makers, Bakers, Screenprinters, Homebrewers'
        )
        self.headline = Headline.random_headline.all()

        tempfile.tempdir = os.path.join(base.MEDIA_ROOT, 'clients/logos')
        tf_logo = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        tf_logo.close()
        self.logo = tf_logo.name
        Client.objects.create(
            name='Coca-Cola',
            logo=self.logo,
            website='http://us.coca-cola.com/home/'
        )
        self.client_list = Client.objects.all()

        tempfile.tempdir = os.path.join(
            base.MEDIA_ROOT, 'staff/mugshots'
        )
        tf_mugshot = tempfile.NamedTemporaryFile(delete=False, suffix='.jpg')
        tf_mugshot.close()
        self.mugshot = tf_mugshot.name
        Employee.objects.create(
            first_name='Patrick',
            middle_name='Scott',
            last_name='Beeson',
            title='Director of Digital Strategy',
            brief_description='Mountains require grit',
            mugshot=self.mugshot,
            is_employed=True
        )
        self.employee_list = Employee.public.all()

        tempfile.tempdir = os.path.join(
            base.MEDIA_ROOT, 'projects/hero_images'
        )
        tf_hero = tempfile.NamedTemporaryFile(delete=False, suffix='.png')
        tf_hero.close()
        self.hero_image = tf_hero.name
        Project.objects.create(
            name='Lowes Foods',
            slug='lowes-foods',
            description='Lowes Foods is a local grocery store chain.',
            hero_image=self.hero_image,
            is_featured=True,
            status='published'
        )
        self.project_list = Project.featured.all()

    def test_home_page_renders_home_template(self):
        response = self.view(self.request)
        self.assertEqual(response.template_name[0], 'home.html')

    def test_home_page_returns(self):
        response = self.view(self.request)
        self.assertEqual(response.status_code, 200)

    def test_home_page_renders_headline_list(self):
        response = self.view(self.request, headline=self.headline)
        self.assertEqual(response.context_data['headline'], self.headline)

    def test_home_page_renders_client_list(self):
        response = self.view(self.request, self.client_list)
        self.assertEqual(
            response.context_data['client_list'][0], self.client_list[0]
        )

    def test_home_page_renders_staff_list(self):
        response = self.view(self.request, self.employee_list)
        self.assertEqual(
            response.context_data['employee_list'][0], self.employee_list[0]
        )

    def test_home_page_renders_featured_project_list(self):
        response = self.view(self.request, self.project_list)
        self.assertEqual(
            response.context_data['project_list'][0], self.project_list[0]
        )

    def tearDown(self):
        headlines = Headline.objects.all()
        headlines.delete()
        os.remove(self.logo)
        clients = Client.objects.all()
        clients.delete()
        os.remove(self.mugshot)
        employees = Employee.objects.all()
        employees.delete()
        os.remove(self.hero_image)
        projects = Project.objects.all()
        projects.delete()
