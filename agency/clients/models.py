from django.db import models
from sorl.thumbnail import ImageField


class Client(models.Model):
    """
    A past or current client of the agency.
    """
    name = models.CharField(
        max_length=100,
        help_text='Limited to 100 characters.',
        default=''
    )
    logo = ImageField(
        help_text='Client logo',
        upload_to='clients/logos',
        default=''
    )
    website = models.URLField(
        blank=True,
        default='',
        help_text='Optional. Could be useful if client isn\'t widely known.'
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
