from django.core.management.base import BaseCommand
from shop.models import Product, Category
from django.utils.text import slugify
import os

class Command(BaseCommand):
    help = 'Adds initial products to the database'

    def handle(self, *args, **kwargs):
        # Get the categories
        kids_category = Category.objects.get(name='Kids')
        toys_category = Category.objects.get(name='Toys')

        # List of products to add
        products = [
            {
                'name': 'Kids T-Shirt',
                'description': 'Comfortable cotton t-shirt for kids',
                'price': 19.99,
                'category': kids_category,
                'image': 'products/tshirt.jpg'
            },
            {
                'name': 'Kids Jeans',
                'description': 'Durable denim jeans for kids',
                'price': 29.99,
                'category': kids_category,
                'image': 'products/jeans.jpg'
            },
            {
                'name': 'Kids Shoes',
                'description': 'Comfortable running shoes for kids',
                'price': 39.99,
                'category': kids_category,
                'image': 'products/shoes.jpg'
            },
            {
                'name': 'Lego Set',
                'description': 'Creative building blocks set',
                'price': 49.99,
                'category': toys_category,
                'image': 'products/lego.jpg'
            },
            {
                'name': 'Remote Control Car',
                'description': 'Fun remote controlled car',
                'price': 34.99,
                'category': toys_category,
                'image': 'products/car.jpg'
            },
            {
                'name': 'Board Game',
                'description': 'Family board game for all ages',
                'price': 24.99,
                'category': toys_category,
                'image': 'products/game.jpg'
            }
        ]

        # Add products
        for product_data in products:
            # Generate slug from name
            slug = slugify(product_data['name'])
            
            # Create or update product
            product, created = Product.objects.update_or_create(
                name=product_data['name'],
                defaults={
                    'description': product_data['description'],
                    'price': product_data['price'],
                    'category': product_data['category'],
                    'image': product_data['image'],
                    'slug': slug
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Successfully added {product.name}'))
            else:
                self.stdout.write(f'Updated {product.name}') 