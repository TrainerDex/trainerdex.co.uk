# Generated by Django 3.2.12 on 2022-04-10 08:25

import django.contrib.postgres.fields.citext
import django.core.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("pokemongo", "0007_populate_nickname_field"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trainer",
            name="_nickname",
            field=django.contrib.postgres.fields.citext.CICharField(
                db_index=True,
                editable=False,
                help_text="A local cached version of a trainers nickname.",
                max_length=15,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        "^[A-Za-z0-9]{3,15}$", "Only letters and numbers are allowed.", "invalid"
                    )
                ],
                verbose_name="Nickname",
            ),
        ),
    ]
