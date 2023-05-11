from django.db import models


class Predvaritelnie(models.Model):
    title = models.TextField(
        'Наименование услуги',
        help_text='Введите наименование услуги',
        max_length=100
    )
    description = models.TextField(
        'Текст объявления',
        max_length=350,
        help_text='Введите текст объявления',
    )
    price = models.TextField(
        'Цена',
        help_text='Введите цену справки',
        max_length=50
    )

    class Meta:
        verbose_name = 'Предварительный осмотр'
        verbose_name_plural = 'Предварительный осмотр'
