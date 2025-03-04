# Generated by Django 5.1.4 on 2025-01-13 21:58

import petstagram.photos.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("photos", "0002_petphoto_create_at_petphoto_modified_ad"),
    ]

    operations = [
        migrations.AlterField(
            model_name="petphoto",
            name="photo",
            field=models.ImageField(
                upload_to="pet_photos/",
                validators=[petstagram.photos.models.validate_image_size_less_then_5mb],
            ),
        ),
    ]
