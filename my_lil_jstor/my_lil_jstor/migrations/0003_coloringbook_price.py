# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_lil_jstor', '0002_dataload'),
    ]

    operations = [
        migrations.AddField(
            model_name='coloringbook',
            name='price',
            field=models.DecimalField(max_digits=5, default=5.0, decimal_places=2),
        ),
    ]
