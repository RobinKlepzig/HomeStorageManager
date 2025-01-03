# Generated by Django 4.2 on 2024-10-06 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Unit",
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
                ("unit_name", models.CharField(max_length=128)),
                ("create_date", models.DateTimeField(auto_now_add=True)),
                ("lastmodified_date", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Object",
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
                ("object_name", models.CharField(max_length=128)),
                ("create_date", models.DateTimeField(auto_now_add=True)),
                ("lastmodified_date", models.DateTimeField(auto_now=True)),
                (
                    "unit",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="storagemanager.unit",
                    ),
                ),
            ],
        ),
    ]
