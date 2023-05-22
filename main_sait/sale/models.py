from django.db import models


class Sale(models.Model):
    CHOICES = (
        ('services:ultrasound', 'Узи'),
        ('services:rentgen', 'Рентген'),
        ('services:analisi', 'Анализы'),
        ('services:fluromobil', 'Флюромобиль'),
        ('profi:predvaritelnie', 'Предварительные'),
        ('profi:pereodicheskiy', 'Периодические'),
        ('profi:vneocherednoy', 'Внеочередной'),
        ('profi:psihiatricheskoe', 'Психиатрическое'),
        ('profi:predsmenniy', 'Предрейсы'),
    )
    CHOICES_BANNER = (
        ('true', 'Первый'),
        ('false', 'Не первый'),
    )
    choice = models.CharField(
        'Выбор услуги',
        help_text='''Выберети нужную услугу для
                   которой будет действовать акция''',
        max_length=100,
        null=True,
        choices=CHOICES
    )
    board_choice = models.CharField(
        'Выбор положения банера на главной странице',
        help_text='''Выберети порядок баннера
                     на главной странице''',
        max_length=100,
        null=True,
        choices=CHOICES_BANNER
    )
    text = models.TextField(
        'Описание акции',
        help_text='Введите описание акции'
    )
    pub_date = models.TextField(
        'Дата окончания акцции',
        help_text='Введите дату окончания акции'
    )
    image = models.ImageField(
        'Картинка',
        blank=True
    )

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'

    def __str__(self):
        return self.text[:15]
