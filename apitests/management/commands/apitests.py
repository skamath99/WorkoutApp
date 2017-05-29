import random

from django.core.management import BaseCommand

from apitests.models import Bakery, Owner


class Command(BaseCommand):
    def handle(self, *args, **options):
        bakeries = [
            'La Petite',
            'Sanketh Sweets',
            'Cater to U'
        ]

        owners = [
            {
                'first_name': 'Sanketh',
                'last_name': 'Kamath'
            },
            {
                'first_name': 'Samantha',
                'last_name': 'Kamath'
            },
            {
                'first_name': 'Connor',
                'last_name': 'Kellog'
            }
        ]

        for bakery in bakeries:
            b = Bakery.objects.create(name=bakery)
            owner = random.sample(owners, 1)
            Owner.objects.create(
                bakery=b,
                first_name=owner[0]['first_name'],
                last_name=owner[0]['last_name']
            )


