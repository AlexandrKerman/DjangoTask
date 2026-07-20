from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomeListView.as_view(), name='home'),
    path('contacts/', views.ContactsView.as_view(), name='contacts'),
    path('product/<int:pk>/', views.ProductDetailView.as_view(), name='product'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# urlpatterns = [
#                   path('', views.home, name='home'),
#                   path('contacts/', views.contacts, name='contacts'),
#                   path('product/<int:product_id>', views.product, name='product')
#               ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
