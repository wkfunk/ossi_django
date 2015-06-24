# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ossi', '0002_auto_20150622_2156'),
    ]

    operations = [
        migrations.CreateModel(
            name='BreederAddress',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='ossi.Address')),
            ],
            bases=('ossi.address',),
        ),
        migrations.CreateModel(
            name='BreederPhone',
            fields=[
                ('phone_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='ossi.Phone')),
            ],
            bases=('ossi.phone',),
        ),
        migrations.CreateModel(
            name='MemberAddress',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='ossi.Address')),
            ],
            bases=('ossi.address',),
        ),
        migrations.CreateModel(
            name='VarietySubmissionAddress',
            fields=[
                ('address_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='ossi.Address')),
            ],
            bases=('ossi.address',),
        ),
        migrations.CreateModel(
            name='VarietySubmissionPhone',
            fields=[
                ('phone_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='ossi.Phone')),
            ],
            bases=('ossi.phone',),
        ),
        migrations.RemoveField(
            model_name='breeder',
            name='address',
        ),
        migrations.RemoveField(
            model_name='breeder',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='member',
            name='address',
        ),
        migrations.RemoveField(
            model_name='varietysubmission',
            name='breeder_address',
        ),
        migrations.RemoveField(
            model_name='varietysubmission',
            name='breeder_phone',
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(max_length=50),
        ),
        migrations.AddField(
            model_name='varietysubmissionphone',
            name='variety_submission',
            field=models.ForeignKey(to='ossi.VarietySubmission'),
        ),
        migrations.AddField(
            model_name='varietysubmissionaddress',
            name='variety_submission',
            field=models.ForeignKey(to='ossi.VarietySubmission'),
        ),
        migrations.AddField(
            model_name='memberaddress',
            name='member',
            field=models.ForeignKey(to='ossi.Member'),
        ),
        migrations.AddField(
            model_name='breederphone',
            name='breeder',
            field=models.ForeignKey(to='ossi.Breeder'),
        ),
        migrations.AddField(
            model_name='breederaddress',
            name='breeder',
            field=models.ForeignKey(to='ossi.Breeder'),
        ),
    ]
