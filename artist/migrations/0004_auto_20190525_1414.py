# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-25 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0003_auto_20190525_1352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='catalogue',
            old_name='year',
            new_name='release_date',
        ),
        migrations.RemoveField(
            model_name='catalogue',
            name='cover_Image',
        ),
        migrations.AddField(
            model_name='catalogue',
            name='num_stars',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
