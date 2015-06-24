# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address_1', models.CharField(max_length=100)),
                ('address_2', models.CharField(max_length=100, null=True, blank=True)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Breeder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('affiliation', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('bio', models.TextField()),
                ('image', models.CharField(max_length=50)),
                ('address', models.ForeignKey(to='ossi.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.ForeignKey(to='ossi.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
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
                ('image', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('crop', models.CharField(max_length=50)),
                ('latin_name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('breeder', models.ForeignKey(to='ossi.Breeder')),
            ],
        ),
        migrations.CreateModel(
            name='VarietySubmission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('breeder', models.CharField(max_length=100)),
                ('breeder_affiliation', models.CharField(max_length=100)),
                ('breeder_email', models.EmailField(max_length=254)),
                ('crop_common_name', models.CharField(max_length=100)),
                ('crop_latin_name', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('image', models.CharField(max_length=50)),
                ('sold_commercially', models.BooleanField()),
                ('where_sold_commercially', models.TextField()),
                ('origin_population', models.TextField()),
                ('origin_parents', models.TextField()),
                ('origin_characteristics', models.TextField()),
                ('origin_two_or_more', models.BooleanField()),
                ('origin_selection_stabilization', models.BooleanField()),
                ('origin_single_parent', models.BooleanField()),
                ('breeding_crosses', models.TextField()),
                ('breeding_goals', models.TextField()),
                ('breeding_processes', models.TextField()),
                ('breeding_generations', models.IntegerField()),
                ('breeding_differ', models.TextField()),
                ('stability', models.CharField(max_length=100)),
                ('submission_IP', models.BooleanField()),
                ('submission_IP_details', models.TextField()),
                ('submission_sole_breeder', models.BooleanField()),
                ('submission_sole_breeder_details', models.TextField()),
                ('submission_permission', models.BooleanField()),
                ('submission_permission_details', models.TextField()),
                ('submission_signature', models.CharField(max_length=100)),
                ('breeder_address', models.ForeignKey(to='ossi.Address')),
                ('breeder_phone', models.ForeignKey(to='ossi.Phone')),
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
            field=models.ForeignKey(to='ossi.Variety'),
        ),
    ]
