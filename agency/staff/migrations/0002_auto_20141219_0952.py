# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import agency.utils.validators
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('order',)},
        ),
        migrations.AddField(
            model_name='employee',
            name='order',
            field=models.PositiveIntegerField(editable=False, db_index=True, default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='mugshot',
            field=sorl.thumbnail.fields.ImageField(help_text='Please use jpg (jpeg) or png files only. Will be resized             for public display.', default='', upload_to='staff/mugshots', validators=[agency.utils.validators.validate_file_type]),
            preserve_default=True,
        ),
    ]
