# Generated by Django 5.1.1 on 2024-09-06 03:03

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="DataCentre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("status", models.CharField(max_length=50)),
                ("color", models.CharField(max_length=50)),
                ("wt", models.CharField(max_length=10)),
            ],
            options={
                "db_table": "dataCentre",
            },
        ),
    ]
