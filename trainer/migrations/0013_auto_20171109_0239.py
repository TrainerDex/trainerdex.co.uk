# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-09 02:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0012_auto_20171108_1823'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DiscordServer',
            new_name='DiscordGuild',
        ),
    ]
