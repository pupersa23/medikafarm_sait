from django.db import models


class Knigki(models.Model):
    CHOICES = (
        ('all', 'Все деятельности'),
        ('medik', 'Для медиков'),
    )
    choice = models.CharField(
        'Выбор вид деятельности книжки',
        help_text='''Выберети нужную деятельность
                     для правильного формирования цен''',
        max_length=100,
        null=True,
        choices=CHOICES
    )
    title = models.TextField(
        'Наименование услуги',
        help_text='Введите наименование деятельности',
        max_length=100
    )
    description = models.TextField(
        'Какие услуги входят в книжку',
        max_length=550,
        help_text='Введите услуги входящие в книжку',
    )
    price = models.TextField(
        'Цена',
        help_text='Введите цену',
        max_length=50
    )

    class Meta:
        verbose_name = 'Медицинские книжки'
        verbose_name_plural = 'Медицинские книжки'
