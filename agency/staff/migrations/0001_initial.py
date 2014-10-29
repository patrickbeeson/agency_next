# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(default='', help_text='Limited to 200 characters.', max_length=200)),
                ('middle_name', models.CharField(default='', help_text='Optional. Limited to 200 characters. Will only use first             letter resolve disputes where two employees have the same first             and last name', blank=True, max_length=200)),
                ('last_name', models.CharField(default='', help_text='Limited to 200 characters.', max_length=200)),
                ('title', models.CharField(default='', help_text='Limited to 250 characters.', max_length=250)),
                ('brief_description', models.TextField(default='', help_text='Optional.', blank=True)),
                ('mugshot', sorl.thumbnail.fields.ImageField(default='', help_text='Please use JPG (JPEG) or PNG files only. Will be resized             for public display.', upload_to='staff/mugshots')),
                ('is_employed', models.BooleanField(default=True, help_text='Uncheck to remove employee from public display.')),
            ],
            options={
                'ordering': ['last_name'],
            },
            bases=(models.Model,),
        ),
    ]
