# Generated by Django 4.2 on 2023-04-25 17:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("services", "0004_alter_analisi_file"),
    ]

    operations = [
        migrations.CreateModel(
            name="Fluromobil",
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
                (
                    "description",
                    models.TextField(
                        help_text="Введите описание услуги Флюромобиля",
                        max_length=500,
                        verbose_name="Описание услуги Флюромобиля",
                    ),
                ),
                (
                    "distance",
                    models.TextField(
                        help_text="Введите расстояние от Москвы",
                        max_length=200,
                        verbose_name="Расстояние от Москвы",
                    ),
                ),
                (
                    "price",
                    models.TextField(
                        help_text="Введите цену услуги",
                        max_length=50,
                        verbose_name="Цена",
                    ),
                ),
            ],
            options={
                "verbose_name": "Услуги Флюромобиль",
                "verbose_name_plural": "Услуги Флюромобиль",
            },
        ),
    ]