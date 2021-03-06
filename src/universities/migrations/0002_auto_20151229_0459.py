# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-29 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('universities', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LocalUniversities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('university_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('university_photo', models.ImageField(upload_to='school_photos')),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='University',
            new_name='InternationalUniversities',
        ),
    ]
