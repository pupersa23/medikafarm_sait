from django.db import models


CHOICES = (
        ('men', 'Мужчинам'),
        ('woman', 'Женщинам'),
        ('corporat', 'Корпоративным'),
    )
CHOICES_2 = (
        ('all', 'Частным'),
        ('corporat', 'Корпоративным'),
    )


class Predvaritelnie(models.Model):
    choice = models.CharField(
        'Выбор к кому относится услуга',
        help_text='''Выбор отобразит описание и
                     цены в нужном окошке на сайте''',
        max_length=100,
        null=True,
        choices=CHOICES
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


class Pereodik(models.Model):
    choice = models.CharField(
        'Выбор к кому относится услуга',
        help_text='''Выбор отобразит описание и
                     цены в нужном окошке на сайте''',
        max_length=100,
        null=True,
        choices=CHOICES
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
        verbose_name = 'Переодический и внеочередной осмотр'
        verbose_name_plural = 'Переодический и внеочередной осмотр'


class Psixushka(models.Model):
    choice = models.CharField(
        'Выбор к кому относится услуга',
        help_text='''Выбор отобразит описание и
                     цены в нужном окошке на сайте''',
        max_length=100,
        null=True,
        choices=CHOICES_2
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
        verbose_name = 'Психиатрическое освидетельствование'
        verbose_name_plural = 'Психиатрическое освидетельствование'


class Predsmena(models.Model):
    choice = models.CharField(
        'Выбор к кому относится услуга',
        help_text='''Выбор отобразит описание и
                     цены в нужном окошке на сайте''',
        max_length=100,
        null=True,
        choices=CHOICES_2
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
        verbose_name = 'Предрейсовый осмотр'
        verbose_name_plural = 'Предрейсовый осмотр'
