# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ossi', '0004_auto_20150629_1553'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='variety',
            name='sold',
        ),
    ]
