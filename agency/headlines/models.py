from random import choice
from django.db import models


class RandomHeadlineManager(models.Manager):
    """
    Get a random headline for homepage display.
    """
    def get_queryset(self):
        count = []
        for headline in Headline.objects.all():
            count.append(headline.id)
        rand_id = choice(count)
        return super(
            RandomHeadlineManager, self).get_queryset().filter(id=rand_id)[0]


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
    random_headline = RandomHeadlineManager()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.headline
