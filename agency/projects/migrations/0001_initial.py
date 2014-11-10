# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import sorl.thumbnail.fields
import agency.utils.validators
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('asset_type', models.CharField(max_length=5, choices=[('Image', 'Image'), ('Text', 'Text'), ('Video', 'Video')], default='Image')),
                ('name', models.CharField(max_length=200, help_text='Limited to 200 characters.')),
                ('text', models.TextField(help_text='Optional. Plain text only.', blank=True, default='')),
                ('image', sorl.thumbnail.fields.ImageField(help_text='Optional. Please use jpg (jpeg) or png files only.', validators=[agency.utils.validators.validate_file_type], default='', upload_to='projects/assets/images', blank=True)),
                ('video', embed_video.fields.EmbedVideoField(help_text='Optional. Copy and paste the video URL into this field.', blank=True, default='')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssetGroup',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('asset_group_type', models.CharField(max_length=15, default='centered')),
                ('name', models.CharField(max_length=200, help_text='Limited to 200 characters.')),
                ('description', models.TextField(help_text='Optional. Plain text only.', blank=True)),
                ('has_emphasis', models.BooleanField(help_text='Set to True if this asset group needs visual emphasis for             display purposes.', default=False)),
            ],
            options={
                'abstract': False,
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=200, help_text='Limited to 200 characters.', default='')),
                ('slug', models.SlugField(help_text='Used to build the category URL.             Will populate from the name field.', unique=True)),
                ('description', models.TextField(help_text='Optional.', blank=True, default='')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Categories',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('name', models.CharField(max_length=200, help_text='Limited to 200 characters.', default='')),
                ('slug', models.SlugField(help_text='Used to build the project URL.             Will populate from the name field.', unique=True, default='')),
                ('description', models.TextField(default='')),
                ('hero_image', sorl.thumbnail.fields.ImageField(help_text='Please use jpg (jpeg) or png files only. Will be resized             for public display.', validators=[agency.utils.validators.validate_file_type], default='', upload_to='projects/hero_images')),
                ('is_featured', models.BooleanField(help_text='Check this box to feature this project on the homepage             and project list page.', default=False)),
                ('status', model_utils.fields.StatusField(max_length=100, choices=[('draft', 'draft'), ('published', 'published')], default='draft', no_check_for_status=True)),
                ('categories', models.ManyToManyField(help_text='Optional. Used for administrative purposes only. Not             shown to the public.', blank=True, default='', to='projects.Category')),
            ],
            options={
                'abstract': False,
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='assetgroup',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asset',
            name='group',
            field=models.ForeignKey(to='projects.AssetGroup'),
            preserve_default=True,
        ),
    ]
