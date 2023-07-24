from random import randint, choice

from django.core.management.base import BaseCommand
from faker import Faker

from apps.models import Product, Category
from tqdm import tqdm


class Command(BaseCommand):
    help = "Closes the specified poll for voting"
    fake = Faker()

    def handle(self, *args, **options):
        c = Category.objects.all()
        for _ in tqdm(range(1000000)):
            p = Product.objects.create(title=self.fake.sentence(6),
                                       description=self.fake.text(),
                                       price=randint(1000, 9000),
                                       )
            p.categories.set([choice(c) for _ in range(3)])
        self.stdout.write(
            self.style.SUCCESS('Successfully created products')
        )
