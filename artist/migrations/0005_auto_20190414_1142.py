# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-14 11:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0004_auto_20190414_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='craft',
            old_name='craft_artist',
            new_name='artist',
        ),
    ]