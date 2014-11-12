# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields
import sorl.thumbnail.fields
import embed_video.fields
import agency.utils.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssetGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('asset_group_type', models.CharField(help_text='Default is centered. Choice impacts display of group.', choices=[('fullbleed', 'Full bleed'), ('centered', 'Centered'), ('centerednarrow', 'Centered Narrow'), ('5050', '50/50'), ('6030', '60/30'), ('3060', '30/60')], default='centered', max_length=15)),
                ('name', models.CharField(help_text='Limited to 200 characters.', max_length=200)),
                ('description', models.TextField(help_text='Optional. Plain text only.', blank=True)),
                ('has_emphasis', models.BooleanField(help_text='Set to True if this asset group needs visual emphasis for             display purposes.', default=False)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(help_text='Limited to 200 characters.', default='', max_length=200)),
                ('slug', models.SlugField(help_text='Used to build the category URL.             Will populate from the name field.', unique=True)),
                ('description', models.TextField(help_text='Optional.', default='', blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(help_text='Limited to 200 characters.', max_length=200)),
                ('description', models.TextField(help_text='Optional. Plain text only.', default='', blank=True)),
                ('image', sorl.thumbnail.fields.ImageField(help_text='Please use jpg (jpeg) or png files only.', default='', upload_to='projects/assets/images', validators=[agency.utils.validators.validate_file_type])),
                ('caption', models.TextField(help_text='Optional. Plain text only.', default='', blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('name', models.CharField(help_text='Limited to 200 characters.', default='', max_length=200)),
                ('slug', models.SlugField(help_text='Used to build the project URL.             Will populate from the name field.', default='', unique=True)),
                ('description', models.TextField(default='')),
                ('hero_image', sorl.thumbnail.fields.ImageField(help_text='Please use jpg (jpeg) or png files only. Will be resized             for public display.', default='', upload_to='projects/hero_images', validators=[agency.utils.validators.validate_file_type])),
                ('is_featured', models.BooleanField(help_text='Check this box to feature this project on the homepage             and project list page.', default=False)),
                ('status', model_utils.fields.StatusField(no_check_for_status=True, choices=[('draft', 'Draft'), ('published', 'Published')], default='draft', max_length=100)),
                ('categories', models.ManyToManyField(help_text='Optional. Used for administrative purposes only. Not             shown to the public.', to='projects.Category', default='', blank=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TextAsset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(help_text='Limited to 200 characters.', max_length=200)),
                ('description', models.TextField(help_text='Optional. Plain text only.', default='', blank=True)),
                ('title', models.CharField(help_text='Optional. Limited to 200 characters.', default='', max_length=200, blank=True)),
                ('text', models.TextField(help_text='Optional. Plain text only.', default='', blank=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(help_text='Limited to 200 characters.', max_length=200)),
                ('description', models.TextField(help_text='Optional. Plain text only.', default='', blank=True)),
                ('video', embed_video.fields.EmbedVideoField(help_text='Optional. Copy and paste the video URL into this field.', default='', blank=True)),
                ('caption', models.TextField(help_text='Optional. Plain text only.', default='', blank=True)),
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
