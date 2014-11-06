# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20141106_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='group',
        ),
        migrations.RemoveField(
            model_name='asset',
            name='project',
        ),
        migrations.RemoveField(
            model_name='assetgroup',
            name='project_assets',
        ),
        migrations.AddField(
            model_name='assetgroup',
            name='assets',
            field=models.ForeignKey(default=0, to='projects.Asset'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assetgroup',
            name='project',
            field=models.ForeignKey(default=0, to='projects.Project'),
            preserve_default=False,
        ),
    ]
