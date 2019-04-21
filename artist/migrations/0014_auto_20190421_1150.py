# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-21 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0013_auto_20190420_2045'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artgroup',
            old_name='artist',
            new_name='Artist',
        ),
        migrations.RenameField(
            model_name='artgroup',
            old_name='can_dance',
            new_name='can_Dance',
        ),
        migrations.RenameField(
            model_name='artgroup',
            old_name='can_draw',
            new_name='can_Draw',
        ),
        migrations.RenameField(
            model_name='artgroup',
            old_name='can_narrate',
            new_name='can_Narrate',
        ),
        migrations.RenameField(
            model_name='artgroup',
            old_name='can_other',
            new_name='can_Other',
        ),
        migrations.RenameField(
            model_name='artgroup',
            old_name='can_paint',
            new_name='can_Paint',
        ),
        migrations.RenameField(
            model_name='artgroup',
            old_name='can_perform',
            new_name='can_Perform',
        ),
        migrations.RenameField(
            model_name='artgroup',
            old_name='can_playInst',
            new_name='can_Play_Inst',
        ),
        migrations.RenameField(
            model_name='artgroup',
            old_name='can_rap',
            new_name='can_RAP',
        ),
        migrations.RenameField(
            model_name='artgroup',
            old_name='can_sing',
            new_name='can_Sing',
        ),
        migrations.RenameField(
            model_name='artgroup',
            old_name='can_snap',
            new_name='can_Snap',
        ),
        migrations.AlterField(
            model_name='member',
            name='talent',
            field=models.CharField(choices=[('pr', 'Painter'), ('mu', 'Musician'), ('dp', 'Performance'), ('pt', 'Poet/RAP'), ('ph', 'Photography'), ('an', 'Animation'), ('at', 'Architecture'), ('cr', 'Computer'), ('ce', 'Ceramics'), ('ca', 'Calligraphy'), ('ag', 'Assemblage'), ('dr', 'Drawing'), ('gi', 'Graffiti'), ('gr', 'Graphic'), ('il', 'Illustration'), ('mo', 'Mosaic'), ('sc', 'Sculpture'), ('vr', 'Videographer')], max_length=3),
        ),
    ]
