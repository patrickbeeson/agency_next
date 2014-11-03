from random import randint
from django.test import TestCase

from headlines.models import Headline


class HeadlineTest(TestCase):

    def setUp(self):
        Headline.objects.create(
            headline='Makers, Bakers, Screenprinters, Homebrewers'
        )

    def test_can_create_headline(self):
        """ Test if calling the headline object returns a headline """
        headline = Headline.objects.get(
            headline='Makers, Bakers, Screenprinters, Homebrewers'
        )
        expected = 'Makers, Bakers, Screenprinters, Homebrewers'
        self.assertEqual(headline.headline, expected)

    def test_can_pull_random_headline(self):
        """ Test whether a random headline is generated. """
        random_headline = Headline.random_headline.all()
        count = Headline.objects.all().count()
        rand_id = randint(1, count)
        expected = rand_id
        self.assertEqual(expected, random_headline.pk)

    def tearDown(self):
        headlines = Headline.objects.all()
        headlines.delete()
