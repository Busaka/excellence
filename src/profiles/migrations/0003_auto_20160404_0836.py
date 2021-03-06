# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-04 05:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('authtools', '0003_auto_20151228_0215'),
        ('profiles', '0002_profile_school'),
    ]

    operations = [
        migrations.CreateModel(
            name='StaffProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Profile picture')),
                ('bio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Short Bio')),
                ('school', models.CharField(blank=True, max_length=200, null=True, verbose_name='School Name')),
                ('school_phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='School Phone')),
                ('school_email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='School Email')),
                ('website', models.CharField(blank=True, max_length=200, null=True, verbose_name='School Website')),
                ('location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Location')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email verified')),
                ('staff_email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Staff Email')),
                ('staff_phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Staff Phone')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudentProfile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/%Y-%m-%d/', verbose_name='Profile picture')),
                ('bio', models.CharField(blank=True, max_length=200, null=True, verbose_name='Short Bio')),
                ('school', models.CharField(blank=True, max_length=200, null=True, verbose_name='School Name')),
                ('school_phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='School Phone')),
                ('school_email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='School Email')),
                ('website', models.CharField(blank=True, max_length=200, null=True, verbose_name='School Website')),
                ('location', models.CharField(blank=True, max_length=200, null=True, verbose_name='Location')),
                ('email_verified', models.BooleanField(default=False, verbose_name='Email verified')),
                ('student_email', models.EmailField(blank=True, max_length=200, null=True, verbose_name='Student Email')),
                ('student_phone', models.CharField(blank=True, max_length=200, null=True, verbose_name='Student Phone')),
                ('study_level', models.CharField(blank=True, max_length=200, null=True, verbose_name='Study Level')),
                ('career1', models.CharField(blank=True, max_length=200, null=True, verbose_name='First Option')),
                ('career2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Second Option')),
                ('career3', models.CharField(blank=True, max_length=200, null=True, verbose_name='Third Option')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
