# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-01 18:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('colleges', '0005_college_college_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='college',
            old_name='college_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='college',
            old_name='college_photo1',
            new_name='photo1',
        ),
    ]