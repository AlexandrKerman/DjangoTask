from tkinter.font import names

from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='blog'),
    path('delete/<int:pk>', views.BlogDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', views.BlogDetailView.as_view(), name='detail'),
    path('edit/<int:pk>', views.BlogUpdateView.as_view(), name='edit')
]