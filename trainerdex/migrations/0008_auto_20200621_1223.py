# Generated by Django 3.0.7 on 2020-06-21 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainerdex', '0007_auto_20200621_1208'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='evidence',
            constraint=models.UniqueConstraint(fields=('content_type', 'object_pk', 'content_field'), name='unique_request'),
        ),
    ]
