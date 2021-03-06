# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 15:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0004_auto_20160119_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image_five',
            field=models.ImageField(default=datetime.datetime(2016, 2, 9, 15, 5, 15, 910818, tzinfo=utc), upload_to='magazine_photos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='image_four',
            field=models.ImageField(default=datetime.datetime(2016, 2, 9, 15, 5, 27, 750277, tzinfo=utc), upload_to='magazine_photos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='image_six',
            field=models.ImageField(default=datetime.datetime(2016, 2, 9, 15, 5, 40, 83308, tzinfo=utc), upload_to='magazine_photos'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='image_three',
            field=models.ImageField(default=datetime.datetime(2016, 2, 9, 15, 6, 16, 797771, tzinfo=utc), upload_to='magazine_photos'),
            preserve_default=False,
        ),
    ]
