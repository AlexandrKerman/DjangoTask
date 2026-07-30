from itertools import product

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils import timezone

from .models import Product, Category
from .forms import CatalogCreateForm


class HomeListView(ListView):
    model = Product
    template_name = 'home.html'
    context_object_name = 'products'


class ProductDetailView(DetailView):
    model = Product
    template_name = 'product.html'
    context_object_name = 'product_info'


class ProductCreateView(CreateView):
    model = Product
    form_class = CatalogCreateForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('name')
        return context

    def form_valid(self, form):
        category_name = form.cleaned_data['category'].strip()
        category, _ = Category.objects.get_or_create(name=category_name)

        product = form.save(commit=False)
        product.category = category
        product.created_at = timezone.now().today()
        product.updated_at = timezone.now().today()

        product.save()
        return super().form_valid(form)


class ProductUpdateView(UpdateView):
    model = Product
    form_class = CatalogCreateForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all().order_by('name')
        return context

    def form_valid(self, form):
        category_name = form.cleaned_data['category'].strip()
        category, _ = Category.objects.get_or_create(name=category_name)

        product = form.save(commit=False)
        product.category = category
        product.updated_at = timezone.now().today()

        product.save()
        return super().form_valid(form)

class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

class ContactsView(View):
    template_name = 'contacts.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        print(f'Данные успешно отправлены методом POST.\n'
              f'Содержимое:\n'
              f'{[i for i in request.POST.items() if i[0] != 'csrfmiddlewaretoken']}')
        return render(request, self.template_name)
