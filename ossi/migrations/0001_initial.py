# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import address.models


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('address', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Breeder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('affiliation', models.CharField(max_length=50)),
                ('default_url', models.URLField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('bio', models.TextField()),
                ('image', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', address.models.AddressField(to='address.Address', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.CharField(max_length=50)),
                ('object_id', models.PositiveIntegerField()),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='SeedSold',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('default_url', models.URLField()),
                ('image', models.FileField(upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('breeder_name', models.CharField(max_length=100, blank=True)),
                ('breeder_affiliation', models.CharField(max_length=100, blank=True)),
                ('breeder_email', models.EmailField(max_length=254, blank=True)),
                ('crop_common_name', models.CharField(max_length=100, blank=True)),
                ('crop_latin_name', models.CharField(max_length=50, blank=True)),
                ('name', models.CharField(max_length=50, blank=True)),
                ('image', models.FileField(upload_to=b'', blank=True)),
                ('sold_commercially', models.BooleanField()),
                ('where_sold_commercially', models.TextField(blank=True)),
                ('description', models.TextField(blank=True)),
                ('origin_population', models.TextField(blank=True)),
                ('origin_parents', models.TextField(blank=True)),
                ('origin_characteristics', models.TextField(blank=True)),
                ('origin_two_or_more', models.BooleanField()),
                ('origin_selection_stabilization', models.BooleanField()),
                ('origin_single_parent', models.BooleanField()),
                ('breeding_crosses', models.TextField(blank=True)),
                ('breeding_goals', models.TextField(blank=True)),
                ('breeding_processes', models.TextField(blank=True)),
                ('breeding_generations', models.IntegerField(blank=True)),
                ('breeding_differ', models.TextField(blank=True)),
                ('stability', models.CharField(max_length=100, blank=True)),
                ('submission_IP', models.BooleanField()),
                ('submission_IP_details', models.TextField(blank=True)),
                ('submission_sole_breeder', models.BooleanField()),
                ('submission_sole_breeder_details', models.TextField(blank=True)),
                ('submission_permission', models.BooleanField()),
                ('submission_permission_details', models.TextField(blank=True)),
                ('submission_signature', models.CharField(max_length=100, blank=True)),
                ('active', models.BooleanField()),
                ('breeder', models.ForeignKey(blank=True, to='ossi.Breeder', null=True)),
                ('breeder_address', address.models.AddressField(blank=True, to='address.Address', null=True)),
            ],
        ),
        migrations.AddField(
            model_name='seedsold',
            name='seller',
            field=models.ForeignKey(to='ossi.Seller'),
        ),
        migrations.AddField(
            model_name='seedsold',
            name='variety',
            field=models.ForeignKey(related_name='locations', blank=True, to='ossi.Variety', null=True),
        ),
    ]
