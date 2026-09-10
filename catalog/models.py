from django.db import models
from django.db.models import ForeignKey

from user.models import CustomUser

class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=300, verbose_name='Описание')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['name']

    def __str__(self):
        return f'{self.pk}. {self.name}'


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Наименование')
    description = models.CharField(max_length=300, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категория')
    price = models.IntegerField(verbose_name='Цена')
    created_at = models.DateField(verbose_name='Создано')
    updated_at = models.DateField(verbose_name='Обновлено')
    is_published = models.BooleanField(default=False, verbose_name='Опубликовано')
    owner = ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, verbose_name='Владелец')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price']
        permissions = [
            ('can_unpublish_product', 'can unpublish product'),
        ]

    def __str__(self):
        return f'{self.pk}. {self.name}. {self.price}. {self.category}'
