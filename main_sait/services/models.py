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
