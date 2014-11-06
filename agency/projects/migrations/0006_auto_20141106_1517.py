# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20141106_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetgroup',
            name='assets',
        ),
        migrations.AddField(
            model_name='asset',
            name='group',
            field=models.ForeignKey(to='projects.AssetGroup', default=0),
            preserve_default=False,
        ),
    ]
