# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-07 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datalayer', '0009_auto_20170607_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='fax',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='agency',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='agency',
            name='phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='agent_rental',
            name='fullname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='agent_rental',
            name='mobile',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='agent_rental',
            name='office_phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='agent_rental',
            name='url_slug',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='district',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='rental_listings',
            name='agency_reference',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rental_listings',
            name='category',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rental_listings',
            name='category_path',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rental_listings',
            name='easting',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rental_listings',
            name='latitude',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rental_listings',
            name='listing_group',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rental_listings',
            name='listing_length',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rental_listings',
            name='longitude',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rental_listings',
            name='northing',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rental_listings',
            name='price_display',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rental_listings',
            name='property_id',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rental_listings',
            name='property_type',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rental_listings',
            name='title',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='suburb',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
