# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(default='', help_text='Limited to 200 characters.', max_length=200)),
                ('slug', models.SlugField(unique=True, help_text='Used to build the category URL.             Will populate from the name field.')),
                ('description', models.TextField(default='', help_text='Optional.', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('order', models.PositiveIntegerField(editable=False, db_index=True)),
                ('name', models.CharField(default='', help_text='Limited to 200 characters.', max_length=200)),
                ('slug', models.SlugField(default='', unique_for_month=True, help_text='Used to build the project URL.             Will populate from the name field.')),
                ('description', models.TextField(default='', help_text='No HTML allowed. Please use Markdown for formatting.')),
                ('hero_image', sorl.thumbnail.fields.ImageField(default='', help_text='Please use JPG (JPEG) or PNG files only. Will be resized             for public display.', upload_to='projects/hero_images')),
                ('is_featured', models.BooleanField(default=False, help_text='Check this box to feature this project on the homepage             and project list page.')),
                ('categories', models.ManyToManyField(default='', to='projects.Category', help_text='Optional. Used for administrative purposes only. Not             shown to the public.', blank=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
