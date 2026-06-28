from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **options):
        Category.objects.all().delete()
        Product.objects.all().delete()

        category, _ = Category.objects.get_or_create(name='Смартфоны', description='Описание смартфонов')

        products = [
            {'name': 'Samsung', 'description': 'Samsung description', 'image': '/images/1.png', 'category': category,
             'price': 1200, 'created_at': '2026-12-23', 'updated_at': '2026-12-23'},
            {'name': 'Xiaomi', 'description': 'Xiaomi description', 'image': '/images/2.png', 'category': category,
             'price': 1000, 'created_at': '2026-12-23', 'updated_at': '2026-12-23'}
        ]
        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully created product: {product.name}'))

            else:
                self.stdout.write(self.style.WARNING(f'Product already exists: {product.name}'))