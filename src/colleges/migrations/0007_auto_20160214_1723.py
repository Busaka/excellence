# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0006_auto_20160201_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='course1_link',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='college',
            name='course2_link',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='college',
            name='course3_link',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='college',
            name='course4_link',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='college',
            name='course5_link',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
