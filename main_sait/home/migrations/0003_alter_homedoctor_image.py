# Generated by Django 4.2 on 2023-05-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_alter_hometopinfo_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homedoctor",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="home/", verbose_name="Фото врача"
            ),
        ),
    ]
