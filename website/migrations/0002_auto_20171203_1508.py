# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-03 15:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0008_clear_default_start_dates'),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='discord',
            name='team',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='trainer.Faction'),
        ),
        migrations.AddField(
            model_name='facebookgroup',
            name='team',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='trainer.Faction'),
        ),
        migrations.AddField(
            model_name='whatsapp',
            name='team',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='trainer.Faction'),
        ),
    ]
