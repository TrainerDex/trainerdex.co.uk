# Generated by Django 3.2.13 on 2022-05-28 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220528_0811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='discordguildsettings',
            old_name='language',
            new_name='language_old',
        ),
        migrations.RenameField(
            model_name='discordguildsettings',
            old_name='monthly_gains_channel',
            new_name='monthly_gains_channel_old',
        ),
        migrations.RenameField(
            model_name='discordguildsettings',
            old_name='renamer',
            new_name='renamer_old',
        ),
        migrations.RenameField(
            model_name='discordguildsettings',
            old_name='renamer_with_level_format',
            new_name='renamer_with_level_format_old',
        ),
        migrations.RenameField(
            model_name='discordguildsettings',
            old_name='renamer_with_level',
            new_name='renamer_with_level_old',
        ),
        migrations.RenameField(
            model_name='discordguildsettings',
            old_name='timezone',
            new_name='timezone_old',
        ),
    ]
