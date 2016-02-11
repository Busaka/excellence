# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-14 10:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading_one', models.CharField(max_length=500)),
                ('question', models.CharField(blank=True, max_length=200)),
                ('h1_paragraph_one', models.TextField(blank=True)),
                ('h1_paragraph_two', models.TextField(blank=True)),
                ('h1_paragraph_three', models.TextField(blank=True)),
                ('answer', models.CharField(blank=True, max_length=200)),
                ('h1_paragraph_four', models.TextField(blank=True)),
                ('h1_paragraph_five', models.TextField(blank=True)),
                ('h1_paragraph_six', models.TextField(blank=True)),
                ('h1_paragraph_seven', models.TextField(blank=True)),
                ('h1_paragraph_eight', models.TextField(blank=True)),
                ('h1_paragraph_nine', models.TextField(blank=True)),
                ('h1_paragraph_ten', models.TextField(blank=True)),
                ('image_one', models.ImageField(upload_to='')),
                ('heading_two', models.CharField(max_length=500)),
                ('sub_heading_two', models.CharField(blank=True, max_length=200)),
                ('h2_paragraph_one', models.TextField(blank=True)),
                ('h2_paragraph_two', models.TextField(blank=True)),
                ('h2_paragraph_three', models.TextField(blank=True)),
                ('h2_paragraph_four', models.TextField(blank=True)),
                ('h2_paragraph_five', models.TextField(blank=True)),
                ('h2_paragraph_six', models.TextField(blank=True)),
                ('h2_paragraph_seven', models.TextField(blank=True)),
                ('h2_paragraph_eight', models.TextField(blank=True)),
                ('h2_paragraph_nine', models.TextField(blank=True)),
                ('h2_paragraph_ten', models.TextField(blank=True)),
                ('image_two', models.ImageField(upload_to='')),
                ('heading_three', models.CharField(max_length=500)),
                ('sub_heading_three', models.CharField(blank=True, max_length=200)),
                ('h3_paragraph_one', models.TextField(blank=True)),
                ('h3_paragraph_two', models.TextField(blank=True)),
                ('h3_paragraph_three', models.TextField(blank=True)),
                ('h3_paragraph_four', models.TextField(blank=True)),
                ('h3_paragraph_five', models.TextField(blank=True)),
                ('h3_paragraph_six', models.TextField(blank=True)),
                ('h3_paragraph_seven', models.TextField(blank=True)),
                ('h3_paragraph_eight', models.TextField(blank=True)),
                ('h3_paragraph_nine', models.TextField(blank=True)),
                ('h3_paragraph_ten', models.TextField(blank=True)),
                ('image_three', models.ImageField(upload_to='')),
                ('heading_four', models.CharField(max_length=500)),
                ('sub_heading_four', models.CharField(blank=True, max_length=200)),
                ('h4_paragraph_one', models.TextField(blank=True)),
                ('h4_paragraph_two', models.TextField(blank=True)),
                ('h4_paragraph_three', models.TextField(blank=True)),
                ('h4_paragraph_four', models.TextField(blank=True)),
                ('h4_paragraph_five', models.TextField(blank=True)),
                ('h4_paragraph_six', models.TextField(blank=True)),
                ('h4_paragraph_seven', models.TextField(blank=True)),
                ('h4_paragraph_eight', models.TextField(blank=True)),
                ('h4_paragraph_nine', models.TextField(blank=True)),
                ('h4_paragraph_ten', models.TextField(blank=True)),
                ('image_four', models.ImageField(upload_to='')),
                ('heading_five', models.CharField(max_length=500)),
                ('sub_heading_five', models.CharField(blank=True, max_length=200)),
                ('h5_paragraph_one', models.TextField(blank=True)),
                ('h5_paragraph_two', models.TextField(blank=True)),
                ('h5_paragraph_three', models.TextField(blank=True)),
                ('h5_paragraph_four', models.TextField(blank=True)),
                ('h5_paragraph_five', models.TextField(blank=True)),
                ('h5_paragraph_six', models.TextField(blank=True)),
                ('h5_paragraph_seven', models.TextField(blank=True)),
                ('h5_paragraph_eight', models.TextField(blank=True)),
                ('h5_paragraph_nine', models.TextField(blank=True)),
                ('h5_paragraph_ten', models.TextField(blank=True)),
                ('image_five', models.ImageField(upload_to='')),
                ('heading_six', models.CharField(max_length=500)),
                ('sub_heading_six', models.CharField(blank=True, max_length=200)),
                ('h6_paragraph_one', models.TextField(blank=True)),
                ('h6_paragraph_two', models.TextField(blank=True)),
                ('h6_paragraph_three', models.TextField(blank=True)),
                ('h6_paragraph_four', models.TextField(blank=True)),
                ('h6_paragraph_five', models.TextField(blank=True)),
                ('h6_paragraph_six', models.TextField(blank=True)),
                ('h6_paragraph_seven', models.TextField(blank=True)),
                ('h6_paragraph_eight', models.TextField(blank=True)),
                ('h6_paragraph_nine', models.TextField(blank=True)),
                ('h6_paragraph_ten', models.TextField(blank=True)),
                ('image_six', models.ImageField(upload_to='')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Published')),
            ],
        ),
    ]
