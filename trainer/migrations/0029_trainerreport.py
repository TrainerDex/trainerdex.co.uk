# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-05 23:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('trainer', '0028_auto_20180105_2330'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainerReport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('report', models.TextField(verbose_name='Report')),
                ('reporter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Reported by')),
                ('trainer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trainer.Trainer', verbose_name='Trainer')),
            ],
            options={
                'verbose_name': 'Report',
                'verbose_name_plural': 'Reports',
            },
        ),
    ]
