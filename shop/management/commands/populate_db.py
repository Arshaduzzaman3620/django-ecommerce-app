from django.core.management.base import BaseCommand
from shop.models import Category, Product
import os
from django.conf import settings

class Command(BaseCommand):
    help = 'Populates the database with sample products'

    def handle(self, *args, **kwargs):
        # Create categories
        men_category = Category.objects.create(
            name='Men\'s Clothing',
            slug='mens-clothing',
            gender='M'
        )

        women_category = Category.objects.create(
            name='Women\'s Clothing',
            slug='womens-clothing',
            gender='W'
        )

        # Sample products for men
        men_products = [
            {
                'name': 'Classic White T-Shirt',
                'slug': 'classic-white-tshirt',
                'price': 29.99,
                'description': 'A comfortable and versatile white t-shirt made from 100% cotton.',
            },
            {
                'name': 'Slim Fit Jeans',
                'slug': 'slim-fit-jeans',
                'price': 59.99,
                'description': 'Modern slim fit jeans with a comfortable stretch.',
            },
            {
                'name': 'Casual Blazer',
                'slug': 'casual-blazer',
                'price': 89.99,
                'description': 'A stylish blazer perfect for both casual and formal occasions.',
            },
        ]

        # Sample products for women
        women_products = [
            {
                'name': 'Floral Summer Dress',
                'slug': 'floral-summer-dress',
                'price': 49.99,
                'description': 'A beautiful floral dress perfect for summer days.',
            },
            {
                'name': 'Skinny Jeans',
                'slug': 'skinny-jeans',
                'price': 54.99,
                'description': 'Comfortable skinny jeans with a perfect fit.',
            },
            {
                'name': 'Knit Sweater',
                'slug': 'knit-sweater',
                'price': 39.99,
                'description': 'A cozy knit sweater for colder days.',
            },
        ]

        # Create products
        for product_data in men_products:
            Product.objects.create(
                category=men_category,
                **product_data
            )

        for product_data in women_products:
            Product.objects.create(
                category=women_category,
                **product_data
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated the database with sample products')) 