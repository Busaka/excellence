# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-19 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0003_auto_20160114_1432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image_one',
            field=models.ImageField(upload_to='magazine_photos'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image_two',
            field=models.ImageField(upload_to='magazine_photos'),
        ),
    ]
