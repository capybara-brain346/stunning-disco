# Generated by Django 5.0.4 on 2024-04-17 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="cancerPreScreenData",
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
                ("name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=30)),
                ("cancerPrediction", models.CharField(max_length=10)),
            ],
        ),
    ]
