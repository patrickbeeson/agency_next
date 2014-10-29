# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Limited to 100 characters.', default='', max_length=100)),
                ('logo', sorl.thumbnail.fields.ImageField(help_text='Please use JPG (JPEG) or PNG files only. Will be resized             for public display.', upload_to='clients/logos', default='')),
                ('website', models.URLField(blank=True, help_text="Optional. Could be useful if client isn't widely known.", default='')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
    ]
