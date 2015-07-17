# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import address.models


class Migration(migrations.Migration):

    dependencies = [
        ('ossi', '0002_auto_20150717_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variety',
            name='breeder_address',
            field=address.models.AddressField(blank=True, to='address.Address', null=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='breeder_affiliation',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='breeder_email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='breeder_name',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='breeding_crosses',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='breeding_differ',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='breeding_generations',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='breeding_goals',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='breeding_processes',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='origin_characteristics',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='origin_parents',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='origin_population',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='stability',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='submission_IP_details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='submission_permission_details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='submission_signature',
            field=models.CharField(max_length=100, blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='submission_sole_breeder_details',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='variety',
            name='where_sold_commercially',
            field=models.TextField(blank=True),
        ),
    ]
