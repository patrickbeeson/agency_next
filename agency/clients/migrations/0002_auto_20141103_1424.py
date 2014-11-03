# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import agency.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='logo',
            field=sorl.thumbnail.fields.ImageField(upload_to='clients/logos', help_text='Please use jpg (jpeg) or png files only. Will be resized             for public display.', validators=[agency.utils.validators.validate_file_type], default=''),
            preserve_default=True,
        ),
    ]
