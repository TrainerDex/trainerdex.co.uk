# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-07-09 11:48
from __future__ import unicode_literals

import django.contrib.postgres.fields.citext
from django.db import migrations
import trainer.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0052_auto_20180621_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='username',
            field=django.contrib.postgres.fields.citext.CICharField(max_length=15, unique=True, validators=[trainer.validators.PokemonGoUsernameValidator], verbose_name='Username'),
        ),
    ]
