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

    class Meta:
        verbose_name = 'Режим работы и телефон'
        verbose_name_plural = 'Режим работы и телефон'
