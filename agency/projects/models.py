from sorl.thumbnail import ImageField
from model_utils.managers import QueryManager
from model_utils.fields import StatusField
from model_utils import Choices
from ordered_model.models import OrderedModel
from agency.utils.validators import validate_file_type
from embed_video.fields import EmbedVideoField

from django.db.models import Q
from django.db import models
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.utils.translation import ugettext_lazy as _


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
    STATUS = Choices(
        ('draft', _('Draft')),
        ('published', _('Published'))
    )
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
    A container for organizing individual assets for a project.
    """
    TYPE = Choices(
        ('fullbleed', _('Full bleed')),
        ('centered', _('Centered')),
        ('centerednarrow', _('Centered Narrow')),
        ('5050', _('50/50')),
        ('6030', _('60/30')),
        ('3060', _('30/60'))
    )
    asset_group_type = models.CharField(
        help_text='Default is centered. Choice impacts display of group.',
        choices=TYPE,
        max_length=15,
        default=TYPE.centered
    )
    name = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters.'
    )
    description = models.TextField(
        blank=True,
        help_text='Optional. Plain text only.'
    )
    has_emphasis = models.BooleanField(
        default=False,
        help_text='Set to True if this asset group needs visual emphasis for \
            display purposes.'
    )
    project = models.ForeignKey(Project)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return '{} / {}'.format(self.name, self.asset_group_type)

    def as_html(self):
        """ Determines what template is used for the AssetGroup. """
        if self.asset_group_type:
            template_name = (
                'projects/{}_assetgroup.html'.format(
                    (self.asset_group_type).lower()
                )
            )
        else:
            template_name = ('projects/base_assetgroup.html')
        return render_to_string(template_name, {'obj': self})


class Asset(models.Model):
    """
    A content asset for a project.
    """
    TYPE = Choices(
        'Image',
        'Text',
        'Video'
    )
    asset_type = models.CharField(
        choices=TYPE,
        default=TYPE.Image,
        max_length=5
    )
    name = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters.'
    )
    text = models.TextField(
        help_text='Optional. Plain text only.',
        default='',
        blank=True
    )
    image = ImageField(
        help_text='Optional. Please use jpg (jpeg) or png files only.',
        upload_to='projects/assets/images',
        default='',
        validators=[validate_file_type],
        blank=True
    )
    video = EmbedVideoField(
        help_text='Optional. Copy and paste the video URL into this field.',
        default='',
        blank=True
    )
    group = models.ForeignKey(AssetGroup)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{} / {}'.format(self.name, self.asset_type)
