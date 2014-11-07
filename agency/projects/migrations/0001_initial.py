# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import embed_video.fields
import model_utils.fields
import agency.utils.validators
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetGroup',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('name', models.CharField(max_length=200, help_text='Limited to 200 characters.')),
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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200, help_text='Limited to 200 characters.')),
                ('slug', models.SlugField(unique=True, help_text='Used to build the category URL.             Will populate from the name field.')),
                ('description', models.TextField(default='', blank=True, help_text='Optional.')),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImageAsset',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, help_text='Limited to 200 characters.')),
                ('image', sorl.thumbnail.fields.ImageField(default='', validators=[agency.utils.validators.validate_file_type], upload_to='projects/assets/images', help_text='Please use jpg (jpeg) or png files only.')),
                ('group', models.ForeignKey(to='projects.AssetGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('name', models.CharField(default='', max_length=200, help_text='Limited to 200 characters.')),
                ('slug', models.SlugField(default='', unique=True, help_text='Used to build the project URL.             Will populate from the name field.')),
                ('description', models.TextField(default='')),
                ('hero_image', sorl.thumbnail.fields.ImageField(default='', validators=[agency.utils.validators.validate_file_type], upload_to='projects/hero_images', help_text='Please use jpg (jpeg) or png files only. Will be resized             for public display.')),
                ('is_featured', models.BooleanField(default=False, help_text='Check this box to feature this project on the homepage             and project list page.')),
                ('status', model_utils.fields.StatusField(default='draft', max_length=100, choices=[('draft', 'draft'), ('published', 'published')], no_check_for_status=True)),
                ('categories', models.ManyToManyField(default='', blank=True, help_text='Optional. Used for administrative purposes only. Not             shown to the public.', to='projects.Category')),
            ],
            options={
                'abstract': False,
                'ordering': ('order',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextAsset',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, help_text='Limited to 200 characters.')),
                ('text', models.TextField(default='', help_text='Plain text only.')),
                ('group', models.ForeignKey(to='projects.AssetGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VideoAsset',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=200, help_text='Limited to 200 characters.')),
                ('video', embed_video.fields.EmbedVideoField(default='', help_text='Copy and paste the video URL into this field.')),
                ('group', models.ForeignKey(to='projects.AssetGroup')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='assetgroup',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
            preserve_default=True,
        ),
    ]
