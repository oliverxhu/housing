# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-06 12:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datalayer', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agency',
            name='is_licenced_property_agency',
        ),
        migrations.RemoveField(
            model_name='agency',
            name='is_real_estate_agency',
        ),
        migrations.RemoveField(
            model_name='rental_listings',
            name='has_embedded_video',
        ),
        migrations.RemoveField(
            model_name='rental_listings',
            name='has_gallery',
        ),
        migrations.RemoveField(
            model_name='rental_listings',
            name='is_bold',
        ),
        migrations.RemoveField(
            model_name='rental_listings',
            name='is_boosted',
        ),
        migrations.RemoveField(
            model_name='rental_listings',
            name='is_featured',
        ),
        migrations.RemoveField(
            model_name='rental_listings',
            name='is_highlighted',
        ),
        migrations.RemoveField(
            model_name='rental_listings',
            name='is_super_featured',
        ),
    ]
