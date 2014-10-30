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

    def tearDown(self):
        headlines = Headline.objects.all()
        headlines.delete()
