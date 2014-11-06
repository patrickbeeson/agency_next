# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20141106_1517'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetgroup',
            name='project',
        ),
        migrations.AddField(
            model_name='asset',
            name='project',
            field=models.ForeignKey(to='projects.Project', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='assets',
            field=models.ManyToManyField(to='projects.AssetGroup', through='projects.Asset'),
            preserve_default=True,
        ),
    ]
