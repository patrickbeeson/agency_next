from sorl.thumbnail import ImageField
from model_utils.managers import QueryManager
from ordered_model.models import OrderedModel

from django.db import models

from agency.utils.validators import validate_file_type


class Employee(OrderedModel):
    """
    An employee of the agency.
    """
    first_name = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters.',
        default=''
    )
    middle_name = models.CharField(
        max_length=200,
        help_text='Optional. Limited to 200 characters. Will only use first \
            letter resolve disputes where two employees have the same first \
            and last name',
        blank=True,
        default=''
    )
    last_name = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters.',
        default=''
    )
    title = models.CharField(
        max_length=250,
        help_text='Limited to 250 characters.',
        default=''
    )
    brief_description = models.TextField(
        help_text='Optional.',
        blank=True,
        default=''
    )
    mugshot = ImageField(
        upload_to='staff/mugshots',
        help_text='Please use jpg (jpeg) or png files only. Will be resized \
            for public display.',
        default='',
        validators=[validate_file_type]
    )
    is_employed = models.BooleanField(
        default=True,
        help_text='Uncheck to remove employee from public display.'
    )

    objects = models.Manager()
    public = QueryManager(is_employed=True).order_by('last_name')

    class Meta(OrderedModel.Meta):
        pass

    @property
    def _get_full_name(self):
        "Return the full name of the employee"
        if self.middle_name:
            full_name = '{} {}. {}'.format(
                self.first_name, self.middle_name[0], self.last_name
            )
        else:
            full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name

    def __str__(self):
        if self.middle_name:
            full_name = '{} {}. {}'.format(
                self.first_name, self.middle_name[0], self.last_name
            )
        else:
            full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name
