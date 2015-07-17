# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ossi', '0003_auto_20150717_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='variety',
            name='active',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variety',
            name='origin_selection_stabilization',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variety',
            name='origin_single_parent',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variety',
            name='origin_two_or_more',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variety',
            name='sold_commercially',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variety',
            name='submission_IP',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variety',
            name='submission_permission',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='variety',
            name='submission_sole_breeder',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
