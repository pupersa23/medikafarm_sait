# Generated by Django 4.2 on 2023-05-29 17:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0003_alter_homedoctor_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="HomeDocuments",
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
                        help_text="Введите название документа",
                        verbose_name="Название документа",
                    ),
                ),
                (
                    "file",
                    models.FileField(
                        help_text="Загрузите документ",
                        upload_to="",
                        verbose_name="Документ",
                    ),
                ),
            ],
            options={
                "verbose_name": "Список внутренних нормативных документов",
                "verbose_name_plural": "Список внутренних нормативных документов",
                "ordering": ["-pk"],
            },
        ),
    ]