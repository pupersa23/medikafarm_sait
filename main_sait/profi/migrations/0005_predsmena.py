# Generated by Django 4.2 on 2023-05-12 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("profi", "0004_psixushka_alter_pereodik_options"),
    ]

    operations = [
        migrations.CreateModel(
            name="Predsmena",
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
                    "title",
                    models.TextField(
                        help_text="Введите наименование услуги",
                        max_length=100,
                        verbose_name="Наименование услуги",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите текст объявления",
                        max_length=350,
                        verbose_name="Текст объявления",
                    ),
                ),
                (
                    "price",
                    models.TextField(
                        help_text="Введите цену справки",
                        max_length=50,
                        verbose_name="Цена",
                    ),
                ),
            ],
            options={
                "verbose_name": "Предсменный осмотр",
                "verbose_name_plural": "Предсменный осмотр",
            },
        ),
    ]
