# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 19:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_lil_jstor', '0005_comments'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comments',
            new_name='Comment',
        ),
    ]
