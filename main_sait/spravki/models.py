from django.db import models


class Gibdd(models.Model):
    title = models.TextField(
        'Наименование услуги',
        help_text='Введите наименование услуги',
        max_length=100
    )
    price = models.TextField(
        'Цена',
        help_text='Введите цену справки',
        max_length=50
    )

    class Meta:
        verbose_name = 'Справки ГАИ'
        verbose_name_plural = 'Справки ГАИ'


class Gims(models.Model):
    title = models.TextField(
        'Наименование услуги',
        help_text='Введите наименование услуги',
        max_length=100
    )
    price = models.TextField(
        'Цена',
        help_text='Введите цену справки',
        max_length=50
    )

    class Meta:
        verbose_name = 'Справки ГИМС'
        verbose_name_plural = 'Справки ГИМС'


class Gsy(models.Model):
    title = models.TextField(
        'Наименование услуги',
        help_text='Введите наименование услуги',
        max_length=100
    )
    price = models.TextField(
        'Цена',
        help_text='Введите цену справки',
        max_length=50
    )

    class Meta:
        verbose_name = 'Справки Госслужба (001-ГС/у)'
        verbose_name_plural = 'Справки Госслужба (001-ГС/у)'


class Gstayna(models.Model):
    title = models.TextField(
        'Наименование услуги',
        help_text='Введите наименование услуги',
        max_length=100
    )
    price = models.TextField(
        'Цена',
        help_text='Введите цену справки',
        max_length=50
    )

    class Meta:
        verbose_name = 'Справки Гостайна (989н)'
        verbose_name_plural = 'Справки Госслужба (989н)'
