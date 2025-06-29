from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name='Пост')
    content = models.TextField(max_length=500, verbose_name='Содержание')
    preview = models.ImageField(upload_to='posts/photo', blank=True, null=True, verbose_name='Превью')
    creation_date = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    publication_flag = models.BooleanField(verbose_name='Опубликовано')
    number_of_views = models.PositiveIntegerField(default=0, verbose_name='Количество просмотров')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['title']