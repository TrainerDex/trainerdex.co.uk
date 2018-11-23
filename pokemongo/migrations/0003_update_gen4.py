# Generated by Django 2.1.2 on 2018-11-23 14:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemongo', '0002_auto_20181123_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='update',
            name='badge_pokedex_entries_gen4',
            field=models.PositiveIntegerField(blank=True, help_text='Register 80 Pokémon first discovered in the Sinnoh region to the Pokédex.', null=True, validators=[django.core.validators.MaxValueValidator(47)], verbose_name='Sinnoh'),
        ),
    ]
