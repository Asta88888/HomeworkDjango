from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add products to database'

    def handle(self, *args, **options):
        category, _ = Category.objects.get_or_create(category_name='Гигиенические средства', category_description='Используются для поддержания чистоты и здоровья тела человека')

        products = [
            {'product_name': 'Зубная паста', 'product_description': 'Освежающая, отбеливающая', 'product_price': 500.00, 'category': category},
            {'product_name': 'Ватные диски', 'product_description': 'Мягкие', 'product_price': 150.00, 'category': category},
        ]

        for product_data in products:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added product: {product.product_name}'))
            else:
                self.stdout.write(self.style.WARNING(f'Product already exist: {product.product_name}'))
