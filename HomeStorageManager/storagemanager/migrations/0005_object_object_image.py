# Generated by Django 4.2 on 2024-11-23 11:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("storagemanager", "0004_remove_object_object_image_alter_unit_unit_image"),
    ]

    operations = [
        migrations.AddField(
            model_name="object",
            name="object_image",
            field=models.ImageField(default="images/item.svg", upload_to="images/"),
        ),
    ]
