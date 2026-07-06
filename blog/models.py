from django.db import models

class Blog(models.Model):
    header = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(max_length=500, verbose_name='Содержимое')
    preview_image = models.ImageField(upload_to='thumbnails/')
    is_published = models.BooleanField()
    views = models.IntegerField()
    created_at = models.DateField()
    updated_at = models.DateField()