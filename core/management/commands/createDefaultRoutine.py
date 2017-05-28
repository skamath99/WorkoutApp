from django.core.management import BaseCommand

from core.models import Routine, Exercise


class Command(BaseCommand):
    def handle(self, *args, **options):
        routine = Routine.objects.create(
            name='Arms'
        )

        exercise = Exercise.objects.create(
            routine=routine,
            name='Curls',
            sets=3
        )
