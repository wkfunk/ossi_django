# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import address.models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '__first__'),
        ('ossi', '0008_auto_20150707_1001'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='address',
            field=address.models.AddressField(to='address.Address', null=True),
        ),
    ]
