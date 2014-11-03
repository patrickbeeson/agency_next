from agency.utils.validators import validate_file_type
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
        help_text='Please use jpg (jpeg) or png files only. Will be resized \
            for public display.',
        upload_to='clients/logos',
        default='',
        validators=[validate_file_type]
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
