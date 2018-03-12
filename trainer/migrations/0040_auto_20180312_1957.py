# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-12 19:57
from __future__ import unicode_literals

import django.contrib.postgres.fields.citext
from django.db import migrations
import trainer.validators


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0039_auto_20180301_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='username',
            field=django.contrib.postgres.fields.citext.CICharField(max_length=30, unique=True, validators=[trainer.validators.validate_pokemon_go_username], verbose_name='Username'),
        ),
    ]
