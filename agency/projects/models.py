from sorl.thumbnail import ImageField
from model_utils.managers import QueryManager
from model_utils.fields import StatusField
from model_utils import Choices
from ordered_model.models import OrderedModel
from agency.utils.validators import validate_file_type
from embed_video.fields import EmbedVideoField

from django.db.models import Q
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse


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
    STATUS = Choices('draft', 'published')
    name = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters.',
        default=''
    )
    slug = models.SlugField(
        help_text='Used to build the project URL. \
            Will populate from the name field.',
        default='',
        unique=True
    )
    description = models.TextField(
        default=''
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
        help_text='Please use jpg (jpeg) or png files only. Will be resized \
            for public display.',
        validators=[validate_file_type]
    )
    is_featured = models.BooleanField(
        default=False,
        help_text='Check this box to feature this project on the homepage \
            and project list page.',
    )
    status = StatusField(default='draft')

    objects = models.Manager()
    published = QueryManager(status='published')
    featured = QueryManager(Q(is_featured=True) & Q(status='published'))

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('project_detail', kwargs={'slug': self.slug})


class AssetGroup(OrderedModel):
    """
    A container for organizing project assets for ordering and display.
    """
    LAYOUT = Choices(
        ('full', _('full')),
        ('centered', _('centered')),
        ('narrow', _('narrow'))
    )
    layout = models.CharField(
        choices=LAYOUT,
        default=LAYOUT.centered,
        max_length=8
    )
    assets = models.ManyToManyField(
        Project,
        through='Asset',
        through_fields=('assetgroup', 'project')
    )

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.id


class Asset(models.Model):
    """
    A content object for a particular project.
    """
    POSITION = Choices(
        ('Pull', _('Pull')),
        ('Push', _('Push'))
    )
    LAYOUT = Choices(
        ('One of one', _('One of one')),
        ('One of two', _('One of two')),
        ('One of three', _('One of three')),
        ('Two of three', _('Two of three'))
    )
    name = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters.'
    )
    body = models.TextField(
        help_text='Optional. An asset as text.',
        blank=True,
        default=''
    )
    image = ImageField(
        help_text='Optional. An asset as an image. Please use jpg (jpeg) or \
            png files only. Will be resized for public display.',
        upload_to='projects/assets/images',
        default='',
        validators=[validate_file_type],
        blank=True,
        null=True
    )
    video = EmbedVideoField(
        help_text='Optional. An asset as video. Copy and paste the video \
            URL into this field.',
        blank=True,
        null=True
    )
    layout = models.CharField(
        max_length=12,
        help_text='Determines the layout option for an asset.',
        default='One of one'
    )
    position = models.CharField(
        help_text='Aligns the asset to the left (pull) or right (push).',
        max_length=4,
        choices=POSITION,
        default='',
        null=True,
        blank=True
    )
    group = models.ForeignKey(AssetGroup)
    project = models.ForeignKey(Project)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
