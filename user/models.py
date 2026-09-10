from django.db import models
from django.contrib.auth.models import AbstractUser

class Countries (models.Model):
    country = models.CharField(max_length=50, verbose_name='Страна')

class CustomUser (AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    user_image = models.ImageField(upload_to='avatars/', verbose_name='Аватар', null=True, blank=True)
    user_phone = models.CharField(max_length=11, verbose_name='Номер телефона')
    user_country = models.ForeignKey(Countries, on_delete=models.SET_NULL, verbose_name='Страна', null=True, blank=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['',]

    def __str__(self):
        return self.email