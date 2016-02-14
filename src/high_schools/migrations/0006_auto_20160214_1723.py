# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-14 14:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('high_schools', '0005_highschool_high_school_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='highschool',
            old_name='subject_five',
            new_name='course1_link',
        ),
        migrations.RenameField(
            model_name='highschool',
            old_name='subject_four',
            new_name='course2_link',
        ),
        migrations.RenameField(
            model_name='highschool',
            old_name='subject_one',
            new_name='course3_link',
        ),
        migrations.RenameField(
            model_name='highschool',
            old_name='subject_three',
            new_name='course4_link',
        ),
        migrations.RenameField(
            model_name='highschool',
            old_name='subject_two',
            new_name='course5_link',
        ),
        migrations.AddField(
            model_name='highschool',
            name='course_five',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='highschool',
            name='course_four',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='highschool',
            name='course_one',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='highschool',
            name='course_three',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='highschool',
            name='course_two',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]