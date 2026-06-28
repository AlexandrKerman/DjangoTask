from django.shortcuts import render

from DjangoTask.settings import MEDIA_URL, MEDIA_ROOT
from .models import Product


def home(request):
    products = Product.objects.values('id', 'name', 'description', 'image', 'category__name', 'price')
    for i in products:
        i['image'] = MEDIA_URL + i['image']
        i['description'] = i['description'][:97] + '...'
    data = {
        'products': products,
    }
    return render(request, 'home.html', data)


def contacts(request):
    if request.method == 'POST':
        print(f'Данные успешно отправлены методом POST.\n'
              f'Содержимое:\n'
              f'{[i for i in request.POST.items() if i[0] != 'csrfmiddlewaretoken']}')
    return render(request, 'contacts.html')


def product(request, product_id):
    product_info = Product.objects.values('name', 'description', 'image', 'category__name', 'price').filter(
        pk=product_id).first()
    product_info['image'] = MEDIA_URL + product_info['image']
    print(product_info)
    data = {
        'product_info': product_info,
    }
    return render(request, 'product.html', data)
