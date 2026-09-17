from django.contrib import admin

from user.models import CustomUser, Countries

@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email')


@admin.register(Countries)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'country')