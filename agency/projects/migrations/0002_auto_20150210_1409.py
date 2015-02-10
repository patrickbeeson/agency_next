# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetgroup',
            name='asset_group_type',
            field=models.CharField(choices=[('fullbleed', 'Full bleed'), ('centered', 'Centered'), ('5050', '50/50'), ('5050_text_left', '50/50 text left'), ('5050_text_right', '50/50 text right'), ('collection_text_upper_left', 'Collection text upper left'), ('collection_text_upper_right', 'Collection text upper right'), ('collection_text_lower_left', 'Collection text lower left'), ('collection_text_lower_right', 'Collection text lower right')], default='centered', help_text='Default is centered. Choice impacts display of group.', max_length=30),
            preserve_default=True,
        ),
    ]
