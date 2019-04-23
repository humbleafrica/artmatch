# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-23 13:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stagename', models.CharField(max_length=250)),
                ('Members', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=500)),
                ('Year', models.DateField(blank=True, null=True)),
                ('Band', models.CharField(max_length=250)),
                ('Genre', models.CharField(max_length=250)),
                ('Stagename', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.Artist')),
            ],
        ),
    ]
