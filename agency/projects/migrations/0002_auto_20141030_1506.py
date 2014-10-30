# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], max_length=100, default='draft', no_check_for_status=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default=''),
            preserve_default=True,
        ),
    ]
