# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0007_auto_20160214_1723'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='facebook',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='college',
            name='twitter',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]