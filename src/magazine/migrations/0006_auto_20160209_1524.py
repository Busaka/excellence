# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-09 15:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0005_auto_20160209_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='answer',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='article',
            name='h1_paragraph_four',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='h1_paragraph_one',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='article',
            name='question',
            field=models.CharField(max_length=200),
        ),
    ]