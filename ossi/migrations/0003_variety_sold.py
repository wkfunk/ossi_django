# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ossi', '0002_remove_variety_sold'),
    ]

    operations = [
        migrations.AddField(
            model_name='variety',
            name='sold',
            field=models.ForeignKey(default=b'', blank=True, to='ossi.SeedSold'),
        ),
    ]
