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
    A container for organizing individual assets for a project.
    """
    name = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters.',
    )
    has_background = models.BooleanField(
        default=False,
        help_text='Set to True if a background is needed for display purposes.'
    )
    project = models.ForeignKey(Project)

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.name

    def as_html(self):
        template_name = ('projects/{}_assetgroup.html'.format((self.name).lower()))
        return render_to_string(template_name, {'obj': self})


class GenericAsset(models.Model):
    """
    A content asset.
    """
    name = models.CharField(
        max_length=200,
        help_text='Limited to 200 characters.'
    )
    group = models.ForeignKey(AssetGroup)

    class Meta:
        abstract = True


class ImageAsset(GenericAsset):
    """
    A content asset as an image.
    """
    image = ImageField(
        help_text='Please use jpg (jpeg) or png files only.',
        upload_to='projects/assets/images',
        default='',
        validators=[validate_file_type]
    )


class TextAsset(GenericAsset):
    """
    A content asset as text.
    """
    text = models.TextField(
        help_text='Plain text only.',
        default=''
    )


class VideoAsset(GenericAsset):
    """
    A content asset as video.
    """
    video = EmbedVideoField(
        help_text='Copy and paste the video URL into this field.',
        default=''
    )
