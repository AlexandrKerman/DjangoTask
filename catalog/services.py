from django.core.cache import cache

from .models import Product


def get_products_by_category(category_id_):
    cache_name = f'product_by_category_{category_id_}'
    products = cache.get(cache_name)
    if products is None:
        products = list(Product.objects.filter(category_id=category_id_))
        cache.set(cache_name, products, 60*5)
    return products