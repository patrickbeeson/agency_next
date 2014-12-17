from sorl.thumbnail import ImageField
from model_utils.managers import QueryManager
from model_utils.fields import StatusField
from model_utils import Choices
from ordered_model.models import OrderedModel
from agency.utils.validators import validate_file_type
from embed_video.fields import EmbedVideoField
from embed_video.backends import detect_backend

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
        ('narrow', _('Centered Narrow')),
        ('6030', _('60/30')),
        ('3060', _('30/60')),
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
    order_with_respect_to = 'project'

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return '{} / {}'.format(self.name, self.asset_group_type)

    def as_html(self):
        """ Method to allow asset groups to use a specific template. """
        if self.asset_group_type:
            template_name = (
                'projects/{}_assetgroup.html'.format(
                    (self.asset_group_type).lower()
                )
            )
        else:
            template_name = ('projects/base_assetgroup.html')
        return render_to_string(template_name, {'obj': self})


class CommonAsset(models.Model):
    """
    Base model used across assets for a project.
    """
    name = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters.'
    )
    description = models.TextField(
        help_text='Optional. Plain text only.',
        default='',
        blank=True
    )
    group = models.ForeignKey(AssetGroup)

    class Meta:
        abstract = True


class ImageAsset(CommonAsset):
    """
    An image asset for a project.
    """
    image = ImageField(
        help_text='Please use jpg (jpeg) or png files only.',
        upload_to='projects/assets/images',
        default='',
        validators=[validate_file_type]
    )
    caption = models.TextField(
        help_text='Optional. Plain text only.',
        default='',
        blank=True
    )

    def __str__(self):
        return '{} / image'.format(self.name)


class TextAsset(CommonAsset):
    """
    A text asset for a project.
    """
    title = models.CharField(
        help_text='Optional. Limited to 200 characters.',
        default='',
        blank=True,
        max_length=200
    )
    text = models.TextField(
        help_text='Optional. Plain text only.',
        default='',
        blank=True
    )

    def __str__(self):
        return '{} / text'.format(self.name)


class VideoAsset(CommonAsset):
    """
    A video asset for a project.
    """
    video = EmbedVideoField(
        help_text='Optional. Copy and paste the video URL into this field.',
        default='',
        blank=True
    )
    caption = models.TextField(
        help_text='Optional. Plain text only.',
        default='',
        blank=True
    )

    def get_video_id(self):
        """
        Get the video id for video referenced.
        """
        video = detect_backend(self.video)
        video_id = video.get_code()
        return video_id

    def get_video_thumbnail_url(self):
        """
        Get the thumbnail for the video at size 3400 x 1500 in jpg format.
        """
        video = detect_backend(self.video)
        orig_thumbnail_url = video.get_thumbnail_url().split('_')
        new_thumbnail_url = (
            '{}_{}'.format(orig_thumbnail_url, '3400x1500.jpg')
        )
        return new_thumbnail_url

    def __str__(self):
        return '{} / video'.format(self.name)
