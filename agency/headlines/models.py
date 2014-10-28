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

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.headline
