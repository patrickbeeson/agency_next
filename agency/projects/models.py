from sorl.thumbnail import ImageField
from model_utils.managers import QueryManager
from ordered_model.models import OrderedModel

from django.db import models


class Category(models.Model):
    """
    A category relating similar projects completed by the agency.
    """
    name = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters.',
        default=''
    )
    slug = models.SlugField(
        help_text='Used to build the category URL. \
            Will populate from the name field.',
        unique=True
    )
    description = models.TextField(
        default='',
        blank=True,
        help_text='Optional.'
    )

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(OrderedModel):
    """
    A project completed by the agency.
    """
    name = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters.',
        default=''
    )
    slug = models.SlugField(
        help_text='Used to build the project URL. \
            Will populate from the name field.',
        default='',
        unique_for_month=True
    )
    description = models.TextField(
        default='',
        help_text='No HTML allowed. Please use Markdown for formatting.'
    )
    categories = models.ManyToManyField(
        Category,
        blank=True,
        default='',
        help_text='Optional. Used for administrative purposes only. Not \
            shown to the public.'
    )
    hero_image = ImageField(
        upload_to='projects/hero_images',
        default='',
        help_text='Please use JPG (JPEG) or PNG files only. Will be resized \
            for public display.',
    )
    is_featured = models.BooleanField(
        default=False,
        help_text='Check this box to feature this project on the homepage \
            and project list page.',
    )

    objects = models.Manager()
    featured = QueryManager(is_featured=True)[:10]

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.name
