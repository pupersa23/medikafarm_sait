from django.db import models


class UltraSound(models.Model):
    description = models.TextField(
        'Описание услуги УЗИ',
        help_text='Введите описание услуги УЗИ',
        max_length=200
    )
    price = models.TextField(
        'Цена',
        help_text='Введите цену услуги',
        max_length=50
    )

    class Meta:
        verbose_name = 'Услуги УЗИ'
        verbose_name_plural = 'Услуги УЗИ'


class Rentgen(models.Model):
    description = models.TextField(
        'Описание услуги Рентген',
        help_text='Введите описание услуги Рентген',
        max_length=200
    )
    price = models.TextField(
        'Цена',
        help_text='Введите цену услуги',
        max_length=50
    )

    class Meta:
        verbose_name = 'Услуги Рентген'
        verbose_name_plural = 'Услуги Рентген'


class Analisi(models.Model):
    file = models.FileField(
        'PDF файл с ценами на анализы',
        help_text='Загрузите файл PDF с ценами',
    )

    class Meta:
        verbose_name = 'Услуги Анализы'
        verbose_name_plural = 'Услуги Анализы'


class Fluromobil(models.Model):
    description = models.TextField(
        'Описание услуги Флюромобиля',
        help_text='Введите описание услуги Флюромобиля',
        max_length=500
    )
    distance = models.TextField(
        'Расстояние от Москвы',
        help_text='Введите расстояние от Москвы',
        max_length=200
    )
    price = models.TextField(
        'Цена',
        help_text='Введите цену услуги',
        max_length=50
    )

    class Meta:
        verbose_name = 'Услуги Флюромобиль'
        verbose_name_plural = 'Услуги Флюромобиль'
