from django.test import TestCase

from homepage.views import HomePageView
from headlines.models import Headline


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
