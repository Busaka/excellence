# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-14 14:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magazine', '0002_auto_20160114_1415'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='h2_paragraph_eleven',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='h2_paragraph_twelve',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='h3_paragraph_eleven',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='h3_paragraph_twelve',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='h4_paragraph_eleven',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='h4_paragraph_twelve',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='h5_paragraph_eleven',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='h5_paragraph_twelve',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='h6_paragraph_eleven',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='h6_paragraph_twelve',
            field=models.TextField(blank=True),
        ),
    ]