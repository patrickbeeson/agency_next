# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_auto_20141106_1314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assetgroup',
            old_name='assets',
            new_name='project_assets',
        ),
        migrations.AlterField(
            model_name='asset',
            name='layout',
            field=models.CharField(choices=[('One of one', 'One of one'), ('One of two', 'One of two'), ('One of three', 'One of three'), ('Two of three', 'Two of three')], help_text='Determines the layout option for an asset.', max_length=12, default='One of one'),
            preserve_default=True,
        ),
    ]
