# Generated by Django 4.2 on 2023-04-21 12:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_homedoctor"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homedoctor",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="", verbose_name="Фото врача"
            ),
        ),
    ]
