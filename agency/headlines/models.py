from random import randint
from django.db import models


class Headline(models.Model):
    """
    A headline to be displayed on the homepage.
    """
    headline = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters.',
        default=''
    )

    objects = models.Manager()

    class Meta:
        ordering = ['pk']

    def get_random_headline(self):
        """
        Get a random headline for homepage display.
        """
        count = self.objects.all().count()
        rand_id = randint(1, count)
        return self.objects.filter(id=rand_id)[1]

    def __str__(self):
        return self.headline
