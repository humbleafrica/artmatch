# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-16 12:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0007_auto_20190516_1222'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'artist', 'verbose_name_plural': 'artist'},
        ),
        migrations.AlterModelOptions(
            name='band',
            options={'verbose_name': 'band', 'verbose_name_plural': 'bands'},
        ),
        migrations.AlterModelOptions(
            name='beat',
            options={'verbose_name': 'beat', 'verbose_name_plural': 'beats'},
        ),
        migrations.AlterModelOptions(
            name='craft',
            options={'verbose_name': 'craft', 'verbose_name_plural': 'crafts'},
        ),
        migrations.AlterModelOptions(
            name='song',
            options={'verbose_name': 'song', 'verbose_name_plural': 'songs'},
        ),
    ]