from django.db import models

from users.models import User


class Category(models.Model):
    category_name = models.CharField(max_length=150, verbose_name='Наименование')
    category_description = models.TextField(max_length=500, verbose_name='Описание')


    def __str__(self):
        return self.category_name


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['category_name']


class Product(models.Model):
    product_name = models.CharField(max_length=150, verbose_name='Наименование')
    product_description = models.TextField(max_length=500, verbose_name='Описание')
    product_image = models.ImageField(upload_to='products/photo', blank=True, null=True, verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='products', verbose_name='Категория')
    product_price = models.FloatField(verbose_name='Цена')
    created_at = models.DateField(auto_now_add=True, verbose_name='Создано')
    updated_at = models.DateField(auto_now=True, verbose_name='Обновлено')
    owner = models.ForeignKey(User, verbose_name='Владелец', blank=True, null=True, on_delete=models.SET_NULL)
    publication_flag = models.BooleanField(default=False, verbose_name='Опубликовано')


    def __str__(self):
        return self.product_name


    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['product_name']
        permissions = [
            ('can_unpublish_product', 'Can unpublished product'),
        ]
