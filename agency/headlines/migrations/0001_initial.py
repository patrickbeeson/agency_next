# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Headline',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('headline', models.CharField(max_length=200, default='', help_text='Limited to 200 characters.')),
            ],
            options={
                'ordering': ['pk'],
            },
            bases=(models.Model,),
        ),
    ]
