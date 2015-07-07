# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ossi', '0007_auto_20150629_1603'),
    ]

    operations = [
        migrations.AddField(
            model_name='variety',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='seedsold',
            name='variety',
            field=models.ForeignKey(related_name='locations', blank=True, to='ossi.Variety', null=True),
        ),
    ]
