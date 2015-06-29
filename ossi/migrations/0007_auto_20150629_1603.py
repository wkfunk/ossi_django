# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ossi', '0006_variety_sold'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variety',
            name='sold',
        ),
        migrations.AddField(
            model_name='seedsold',
            name='variety',
            field=models.ForeignKey(blank=True, to='ossi.Variety', null=True),
        ),
    ]
