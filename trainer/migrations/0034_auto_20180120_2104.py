# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-20 21:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0033_auto_20180120_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='play_zones_city',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='play_zones_country',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='play_zones_region',
        ),
        migrations.RemoveField(
            model_name='trainer',
            name='play_zones_subregion',
        ),
        migrations.AlterField(
            model_name='update',
            name='meta_source',
            field=models.CharField(choices=[('?', 'undefined'), ('cs_social_twitter', 'Twitter'), ('cs_social_facebook', 'Facebook'), ('ts_social_discord', 'Official Discord Bot'), ('web_quick', 'Quick Update'), ('web_detailed', 'Detailed Update'), ('ts_registration', 'Registration'), ('ss_registration', 'Registration Screenshot'), ('ss_generic', 'Generic Screenshot')], default='?', max_length=256, verbose_name='Source'),
        ),
    ]
