# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-28 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('school_photo', models.ImageField(upload_to='school_photos')),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]