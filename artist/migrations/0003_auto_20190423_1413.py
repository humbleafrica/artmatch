# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-23 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0002_band_song'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='Band',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.Band'),
        ),
    ]