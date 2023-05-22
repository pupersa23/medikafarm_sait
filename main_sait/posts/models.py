from django.db import models


class Post(models.Model):
    title = models.TextField(
        'Заголовок статьи',
        help_text='Введите заголовок статьи'
    )
    overview = models.TextField(
        'Краткое описание статьи',
        help_text='Введите краткое описание статьи'
    )
    text = models.TextField(
        'Текст статьи',
        help_text='Введите текст статьи'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True
    )
    image = models.ImageField(
        'Картинка',
        upload_to='posts/',
        blank=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.text[:15]
