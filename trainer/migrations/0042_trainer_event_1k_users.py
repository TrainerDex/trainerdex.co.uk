# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-18 17:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0041_auto_20180315_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='event_1k_users',
            field=models.BooleanField(default=True),
        ),
    ]
