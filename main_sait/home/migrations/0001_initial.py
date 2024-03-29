# Generated by Django 4.2 on 2023-04-24 17:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="HomeBord",
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
                    "choice",
                    models.CharField(
                        choices=[("true", "Первый"), ("false", "Не первый")],
                        help_text="Выберети будет ли этот слайд первым",
                        max_length=100,
                        verbose_name="Выбор порядка слайда",
                    ),
                ),
                (
                    "title",
                    models.TextField(
                        help_text="Введите заголовок",
                        max_length=100,
                        verbose_name="Заголовок объявления",
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
                    "url_for_button",
                    models.TextField(
                        blank=True,
                        help_text="Введите ссылка для кнопки (если нужно)",
                        verbose_name="Ссылка для кнопки (если нужно)",
                    ),
                ),
            ],
            options={
                "verbose_name": "Баннер на главной странице",
                "verbose_name_plural": "Баннер на главной странице",
                "ordering": ["-pk"],
            },
        ),
        migrations.CreateModel(
            name="HomeDoctor",
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
                    "image",
                    models.ImageField(
                        blank=True, upload_to="", verbose_name="Фото врача"
                    ),
                ),
                (
                    "fio",
                    models.TextField(
                        help_text="Введите ФИО врача раздельно",
                        verbose_name="Фамилия Имя Отчество врача",
                    ),
                ),
                (
                    "job_title",
                    models.TextField(
                        help_text="Введите должность врача",
                        verbose_name="Должность врача",
                    ),
                ),
            ],
            options={
                "verbose_name": "Список врачей на главной странице",
                "verbose_name_plural": "Список врачей на главной странице",
                "ordering": ["-pk"],
            },
        ),
        migrations.CreateModel(
            name="HomePriceCorp",
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
                        help_text="Введите название услуги",
                        max_length=200,
                        verbose_name="Название услуги",
                    ),
                ),
                (
                    "price",
                    models.TextField(
                        help_text="Введите цену", max_length=200, verbose_name="Цена"
                    ),
                ),
                (
                    "quantity",
                    models.TextField(
                        help_text="Введите за что цена",
                        max_length=200,
                        verbose_name="За человека или т.д.",
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        help_text="Введите описания услуги",
                        verbose_name="Описание услуги",
                    ),
                ),
                (
                    "url_for_button",
                    models.TextField(
                        blank=True,
                        help_text="Введите ссылка для кнопки (если нужно)",
                        verbose_name="Ссылка для кнопки (если нужно)",
                    ),
                ),
            ],
            options={
                "verbose_name": "Выгодные корпоративный цены",
                "verbose_name_plural": "Выгодные корпоративный цены",
                "ordering": ["-pk"],
            },
        ),
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
                (
                    "email_adm",
                    models.TextField(
                        help_text="Введите общую почту",
                        max_length=100,
                        verbose_name="Общая почта",
                    ),
                ),
                (
                    "email_sail",
                    models.TextField(
                        help_text="Введите почта отдела продаж",
                        max_length=100,
                        verbose_name="Почта отдела продаж",
                    ),
                ),
            ],
            options={
                "verbose_name": "Режим работы и телефон",
                "verbose_name_plural": "Режим работы и телефон",
            },
        ),
    ]
