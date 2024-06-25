import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))
            print(phones)

        for phone in phones:
            new_phone_model = Phone(
                name=phone.get('name'),
                image=phone.get('image'),
                price=phone.get('price'),
                release_date=phone.get('release_date'),
                lte_exists=phone.get('lte_exists'),
                slug=slugify(phone.get('name'))
            )
            new_phone_model.save()
