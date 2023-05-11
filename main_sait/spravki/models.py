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


class Spravka086_1(models.Model):
    CHOICES = (
        ('dlya-meditsinskikh-napravleniy', 'Медики'),
        ('na-dolzhnost-sudi', 'Судья'),
        ('dlya-raboty', 'Обычная'),
        ('dlya-postupleniya', 'Институт'),
    )
    choice = models.CharField(
        'Выбор справки 086',
        help_text='''Выберети нужную справку для
                   правильного отображения страницы''',
        max_length=100,
        null=True,
        choices=CHOICES
    )
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
        verbose_name = 'Справки 086/у'
        verbose_name_plural = 'Справки 086/у'


class Spravka095_1(models.Model):
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
        verbose_name = 'Справки 095/у'
        verbose_name_plural = 'Справки 095/у'


class Bassein(models.Model):
    CHOICES = (
        ('bassein', 'Бассейн'),
        ('sport', 'Спорт'),
        ('sabeg', 'Забег'),
        ('sapliv', 'Заплыв'),
    )
    choice = models.CharField(
        'Выбор справки спорт',
        help_text='''Выберети нужную справку для
                   правильного отображения страницы''',
        max_length=100,
        null=True,
        choices=CHOICES
    )
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
        verbose_name = 'Справки для спорта'
        verbose_name_plural = 'Справки для спорта'


class Travel(models.Model):
    CHOICES = (
        ('sankarta', 'Санкарта'),
        ('sanatoriy', 'Санаторий'),
        ('sagranica', 'Заграница'),
    )
    choice = models.CharField(
        'Выбор справки для путешествий',
        help_text='''Выберети нужную справку для
                   правильного отображения страницы''',
        max_length=100,
        null=True,
        choices=CHOICES
    )
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
        verbose_name = 'Справки для поездок'
        verbose_name_plural = 'Справки для поездок'


class Bolnichnij(models.Model):
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
        verbose_name = 'Больничные листы'
        verbose_name_plural = 'Больничные листы'
