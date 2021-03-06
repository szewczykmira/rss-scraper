# Generated by Django 3.0.2 on 2020-01-06 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Rate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("currency", models.CharField(max_length=3, unique=True)),
                ("exchange_rate", models.DecimalField(decimal_places=4, max_digits=50)),
                ("parser_update_date", models.DateTimeField()),
                ("description", models.TextField()),
            ],
        ),
    ]
