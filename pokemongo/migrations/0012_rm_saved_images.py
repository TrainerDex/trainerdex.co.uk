# Generated by Django 4.0.6 on 2022-07-30 15:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokemongo', '0011_missing_stats'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trainer',
            name='verification',
        ),
        migrations.RemoveField(
            model_name='update',
            name='screenshot',
        ),
    ]
