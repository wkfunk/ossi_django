# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ossi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breeder',
            name='image',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='breeder',
            name='phone',
            field=models.ForeignKey(to='ossi.Phone'),
        ),
        migrations.AlterField(
            model_name='seller',
            name='image',
            field=models.FileField(upload_to=b''),
        ),
        migrations.AlterField(
            model_name='variety',
            name='image',
            field=models.FileField(upload_to=b''),
        ),
    ]
