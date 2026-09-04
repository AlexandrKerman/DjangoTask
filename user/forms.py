from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Countries, CustomUser

class UserCreateForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.user_country:
            self.initial['country'] = self.instance.user_country.country


class UserAuthForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['email', 'password']