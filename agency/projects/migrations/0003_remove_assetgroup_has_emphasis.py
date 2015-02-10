# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20150210_1409'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assetgroup',
            name='has_emphasis',
        ),
    ]
