# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-25 12:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('genre', models.CharField(max_length=10)),
                ('year', models.DateField(blank=True, null=True)),
                ('cover_Image', models.ImageField(upload_to='images/')),
                ('file', models.FileField(upload_to='artForm/')),
            ],
            options={
                'verbose_name': 'Art Form',
                'verbose_name_plural': 'Art Forms',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('fname', models.CharField(max_length=50)),
                ('sname', models.CharField(max_length=50)),
                ('stagename', models.CharField(max_length=50)),
                ('craft', models.CharField(choices=[('Painting', 'Painting'), ('Music', 'Music'), ('Performance', 'Performance'), ('Poet/RAP', 'Poetry'), ('Photography', 'Photography'), ('Animation', 'Animation'), ('Design & Architecture', 'Design & Architecture'), ('Computer', 'Computer'), ('Ceramics', 'Ceramics'), ('Calligraphy', 'Calligraphy'), ('Assemblage', 'Assemblage'), ('Drawing', 'Drawing'), ('Graffiti', 'Graffiti'), ('Graphic', 'Graphic'), ('Illustration', 'Illustration'), ('Mosaic', 'Mosaic'), ('Sculpture', 'Sculpture'), ('Videographer', 'Videographer')], max_length=20, verbose_name='Craft')),
                ('speciality', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'artist',
                'verbose_name_plural': 'artists',
            },
        ),
        migrations.CreateModel(
            name='Bug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('What', models.CharField(max_length=2500)),
                ('When', models.DateField(blank=True, null=True)),
                ('How', models.CharField(max_length=2500)),
                ('Who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.Artist')),
            ],
            options={
                'verbose_name': 'bug',
                'verbose_name_plural': 'bugs',
            },
        ),
        migrations.CreateModel(
            name='Catalogue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('year', models.DateField(blank=True, null=True)),
                ('cover_Image', models.ImageField(upload_to='images/')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.Artist')),
            ],
        ),
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('What', models.CharField(max_length=2500)),
                ('When', models.DateField(blank=True, null=True)),
                ('How', models.CharField(max_length=2500)),
                ('Who', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.Artist')),
            ],
            options={
                'verbose_name': 'feature',
                'verbose_name_plural': 'features',
            },
        ),
        migrations.AddField(
            model_name='artform',
            name='catalogue',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='artist.Catalogue'),
        ),
    ]
