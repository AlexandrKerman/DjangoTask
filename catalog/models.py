from django.db import models


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
    description = models.CharField(max_length=300, verbose_name='Описвание')
    image = models.ImageField(verbose_name='Изображение')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['name', 'price']

    def __str__(self):
        return f'{self.pk}. {self.name}. {self.price}. {self.category}'
