from django.contrib import admin
from blog.models import *

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('header',)
