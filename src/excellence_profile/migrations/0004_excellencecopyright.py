# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-10 14:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excellence_profile', '0003_termsandcondition'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExcellenceCopyright',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading1', models.CharField(max_length=500)),
                ('h1_paragragh1', models.TextField(blank=True)),
                ('h1_paragragh2', models.TextField(blank=True)),
                ('h1_paragragh3', models.TextField(blank=True)),
                ('h1_paragragh4', models.TextField(blank=True)),
                ('h1_paragragh5', models.TextField(blank=True)),
                ('h1_paragragh6', models.TextField(blank=True)),
                ('h1_paragragh7', models.TextField(blank=True)),
                ('heading2', models.CharField(max_length=500)),
                ('h2_paragragh1', models.TextField(blank=True)),
                ('h2_paragragh2', models.TextField(blank=True)),
                ('h2_paragragh3', models.TextField(blank=True)),
                ('h2_paragragh4', models.TextField(blank=True)),
                ('h2_paragragh5', models.TextField(blank=True)),
                ('h2_paragragh6', models.TextField(blank=True)),
                ('h2_paragragh7', models.TextField(blank=True)),
                ('heading3', models.CharField(max_length=500)),
                ('h3_paragragh1', models.TextField(blank=True)),
                ('h3_paragragh2', models.TextField(blank=True)),
                ('h3_paragragh3', models.TextField(blank=True)),
                ('h3_paragragh4', models.TextField(blank=True)),
                ('h3_paragragh5', models.TextField(blank=True)),
                ('h3_paragragh6', models.TextField(blank=True)),
                ('h3_paragragh7', models.TextField(blank=True)),
            ],
        ),
    ]
