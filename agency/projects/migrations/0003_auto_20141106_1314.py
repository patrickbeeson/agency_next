# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import sorl.thumbnail.fields
import embed_video.fields
import agency.utils.validators


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_auto_20141030_1506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200, help_text='Limited to 200 characters.')),
                ('body', models.TextField(blank=True, help_text='Optional. An asset as text.', default='')),
                ('image', sorl.thumbnail.fields.ImageField(upload_to='projects/assets/images', blank=True, help_text='Optional. An asset as an image. Please use jpg (jpeg) or             png files only. Will be resized for public display.', validators=[agency.utils.validators.validate_file_type], null=True, default='')),
                ('video', embed_video.fields.EmbedVideoField(blank=True, null=True, help_text='Optional. An asset as video. Copy and paste the video             URL into this field.')),
                ('layout', models.CharField(max_length=12, help_text='Determines the layout option for an asset.', default='One of one')),
                ('position', models.CharField(max_length=4, blank=True, help_text='Aligns the asset to the left (pull) or right (push).', choices=[('Pull', 'Pull'), ('Push', 'Push')], null=True, default='')),
            ],
            options={
                'ordering': ['name'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssetGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('order', models.PositiveIntegerField(db_index=True, editable=False)),
                ('layout', models.CharField(choices=[('full', 'full'), ('centered', 'centered'), ('narrow', 'narrow')], max_length=8, default='centered')),
                ('assets', models.ManyToManyField(through='projects.Asset', to='projects.Project')),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='asset',
            name='group',
            field=models.ForeignKey(to='projects.AssetGroup'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='asset',
            name='project',
            field=models.ForeignKey(to='projects.Project'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='hero_image',
            field=sorl.thumbnail.fields.ImageField(upload_to='projects/hero_images', validators=[agency.utils.validators.validate_file_type], help_text='Please use jpg (jpeg) or png files only. Will be resized             for public display.', default=''),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='slug',
            field=models.SlugField(unique=True, help_text='Used to build the project URL.             Will populate from the name field.', default=''),
            preserve_default=True,
        ),
    ]
