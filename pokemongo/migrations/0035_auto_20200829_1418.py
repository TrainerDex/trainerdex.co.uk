# Generated by Django 2.2.15 on 2020-08-29 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemongo', '0034_auto_20200829_1342'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='update',
            name='badge_pokedex_entries_gen6',
        ),
        migrations.RemoveField(
            model_name='update',
            name='badge_pokedex_entries_gen7',
        ),
        migrations.RemoveField(
            model_name='update',
            name='badge_pokedex_entries_gen8',
        ),
        migrations.AddField(
            model_name='update',
            name='badge_buddy_best',
            field=models.PositiveIntegerField(blank=True, help_text='Have 100 Best Buddies.', null=True, verbose_name='Best Buddy'),
        ),
        migrations.AddField(
            model_name='update',
            name='badge_rocket_giovanni_defeated',
            field=models.PositiveIntegerField(blank=True, help_text='Defeat Giovanni 20 time(s).', null=True, verbose_name='Ultra Hero'),
        ),
        migrations.AddField(
            model_name='update',
            name='badge_wayfarer',
            field=models.PositiveIntegerField(blank=True, help_text='Earn 1,000 Wayfarer Agreements.', null=True, verbose_name='Wayfarer'),
        ),
    ]
