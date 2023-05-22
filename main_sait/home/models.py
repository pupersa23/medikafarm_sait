from django.db import models


class HomeTopInfo(models.Model):
    work_time = models.TextField(
        'Режим работы',
        help_text='Введите режим работы',
        max_length=200
    )
    phone_number = models.TextField(
        'Номер телефона',
        help_text='Введите номер телефона',
        max_length=50
    )
    email_adm = models.TextField(
        'Общая почта',
        help_text='Введите общую почту',
        max_length=100
    )
    email_sail = models.TextField(
        'Почта отдела продаж',
        help_text='Введите почта отдела продаж',
        max_length=100
    )

    class Meta:
        verbose_name = 'Режим работы, телефон, почты'
        verbose_name_plural = 'Режим работы, телефон, почты'


class HomeBord(models.Model):
    CHOICES = (
        ('true', 'Первый'),
        ('false', 'Не первый'),
    )
    choice = models.CharField(
        'Выбор порядка слайда',
        help_text='Выберети будет ли этот слайд первым',
        max_length=100,
        null=False,
        choices=CHOICES
    )
    title = models.TextField(
        'Заголовок объявления',
        help_text='Введите заголовок',
        max_length=100
    )
    description = models.TextField(
        'Текст объявления',
        max_length=350,
        help_text='Введите текст объявления',
    )
    url_for_button = models.TextField(
        'Ссылка для кнопки (если нужно)',
        help_text='Введите ссылка для кнопки (если нужно)',
        blank=True,
    )

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Баннер на главной странице'
        verbose_name_plural = 'Баннер на главной странице'


class HomePriceCorp(models.Model):
    title = models.TextField(
        'Название услуги',
        help_text='Введите название услуги',
        max_length=200
    )
    price = models.TextField(
        'Цена',
        help_text='Введите цену',
        max_length=200
    )
    quantity = models.TextField(
        'За человека или т.д.',
        help_text='Введите за что цена',
        max_length=200
    )
    description = models.TextField(
        'Описание услуги',
        help_text='Введите описания услуги',
    )
    url_for_button = models.TextField(
        'Ссылка для кнопки (если нужно)',
        help_text='Введите ссылка для кнопки (если нужно)',
        blank=True,
    )

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Выгодные корпоративный цены'
        verbose_name_plural = 'Выгодные корпоративный цены'


class HomeDoctor(models.Model):
    image = models.ImageField(
        'Фото врача',
        upload_to='home/',
        blank=True
    )
    fio = models.TextField(
        'Фамилия Имя Отчество врача',
        help_text='Введите ФИО врача раздельно'
    )
    job_title = models.TextField(
        'Должность врача',
        help_text='Введите должность врача'
    )

    class Meta:
        ordering = ['-pk']
        verbose_name = 'Список врачей на главной странице'
        verbose_name_plural = 'Список врачей на главной странице'
