# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-06 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0008_clear_default_start_dates'),
        ('cities_light', '0006_compensate_for_0003_bytestring_bug'),
        ('website', '0002_auto_20171203_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessengerGroup',
            fields=[
                ('id', models.CharField(max_length=256, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('extra_data', models.TextField(blank=True)),
                ('invite_slug', models.CharField(max_length=256, unique=True)),
                ('locations', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cities_light.City')),
                ('team', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='trainer.Faction')),
            ],
            options={
                'ordering': ['name'],
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='discord',
            name='enhanced',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='discord',
            name='invite_slug',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='facebookgroup',
            name='username',
            field=models.CharField(max_length=256, unique=True),
        ),
        migrations.AlterField(
            model_name='whatsapp',
            name='invite_slug',
            field=models.CharField(max_length=256, unique=True),
        ),
    ]
