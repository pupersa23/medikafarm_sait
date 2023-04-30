# Generated by Django 4.2 on 2023-04-30 20:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("spravki", "0002_gsy"),
    ]

    operations = [
        migrations.CreateModel(
            name="Gstayna",
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
                    "price",
                    models.TextField(
                        help_text="Введите цену справки",
                        max_length=50,
                        verbose_name="Цена",
                    ),
                ),
            ],
            options={
                "verbose_name": "Справки Гостайна (989н)",
                "verbose_name_plural": "Справки Госслужба (989н)",
            },
        ),
    ]
