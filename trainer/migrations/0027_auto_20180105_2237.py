# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-05 22:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0026_auto_20180104_2329'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='faction',
            name='image',
        ),
        migrations.RemoveField(
            model_name='faction',
            name='leader_image',
        ),
    ]
