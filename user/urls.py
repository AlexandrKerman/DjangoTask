from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views


urlpatterns = [
    path('register/', views.UserCreateView.as_view(), name='register'),
    path('login/', views.UserAuthView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout')
]