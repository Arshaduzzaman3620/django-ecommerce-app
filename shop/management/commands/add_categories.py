from django.core.management.base import BaseCommand
from shop.models import Category

class Command(BaseCommand):
    help = 'Adds Kids and Toys categories to the database'

    def handle(self, *args, **options):
        # Create Kids category
        kids_category, created = Category.objects.get_or_create(
            name='Kids',
            slug='kids'
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created Kids category'))
        else:
            self.stdout.write('Kids category already exists')

        # Create Toys category
        toys_category, created = Category.objects.get_or_create(
            name='Toys',
            slug='toys'
        )
        if created:
            self.stdout.write(self.style.SUCCESS('Successfully created Toys category'))
        else:
            self.stdout.write('Toys category already exists') 