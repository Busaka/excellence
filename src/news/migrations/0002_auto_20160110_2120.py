# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-10 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='New',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_one', models.CharField(max_length=500)),
                ('text_one', models.TextField()),
                ('image_one', models.ImageField(upload_to='')),
                ('heading_two', models.CharField(max_length=500)),
                ('text_two', models.TextField()),
                ('image_two', models.ImageField(upload_to='')),
                ('heading_three', models.CharField(max_length=500)),
                ('text_three', models.TextField()),
                ('image_three', models.ImageField(upload_to='')),
                ('heading_four', models.CharField(max_length=500)),
                ('text_four', models.TextField()),
                ('image_four', models.ImageField(upload_to='')),
                ('heading_five', models.CharField(max_length=500)),
                ('text_five', models.TextField()),
                ('image_five', models.ImageField(upload_to='')),
                ('file_five', models.FileField(upload_to='')),
            ],
        ),
        migrations.DeleteModel(
            name='News',
        ),
    ]
