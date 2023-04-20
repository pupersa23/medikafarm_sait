# Generated by Django 4.2 on 2023-04-20 16:43

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HomeTopInfo",
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
                    "work_time",
                    models.TextField(
                        help_text="Введите режим работы",
                        max_length=200,
                        verbose_name="Режим работы",
                    ),
                ),
                (
                    "phone_number",
                    models.TextField(
                        help_text="Введите номер телефона",
                        max_length=50,
                        verbose_name="Номер телефона",
                    ),
                ),
            ],
        ),
    ]
