from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail

from DjangoTask.settings import DEFAULT_FROM_EMAIL

from .models import Countries, CustomUser
from .forms import UserCreateForm, UserAuthForm


class UserCreateView(CreateView):
    model = CustomUser
    form_class = UserCreateForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')  # Error?

    def form_valid(self, form):
        from_email = DEFAULT_FROM_EMAIL
        print(form.cleaned_data['email'])

        # send_mail(subject='test1', message='Proverka', from_email=from_email,
        #           recipient_list=[form.cleaned_data.get('email')])
        return super().form_valid(form)


class UserAuthView(LoginView):
    template_name = 'login.html'
    form_class = UserAuthForm
    success_url = reverse_lazy('home')
