# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-06 12:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datalayer', '0002_auto_20170606_2228'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='is_licenced_property_agency',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='agency',
            name='is_real_estate_agency',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='rental_listings',
            name='has_embedded_video1',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='rental_listings',
            name='has_gallery1',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='rental_listings',
            name='is_bold1',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='rental_listings',
            name='is_boosted1',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='rental_listings',
            name='is_classified1',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='rental_listings',
            name='is_featured1',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='rental_listings',
            name='is_highlighted1',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='rental_listings',
            name='is_super_featured1',
            field=models.NullBooleanField(),
        ),
    ]
