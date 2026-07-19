from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

from .models import Product

class HomeListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_info'

class ContactsView(View):
    template_name = 'contacts.html'
    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print(f'Данные успешно отправлены методом POST.\n'
              f'Содержимое:\n'
              f'{[i for i in request.POST.items() if i[0] != 'csrfmiddlewaretoken']}')
        return render(request, self.template_name)

