from django.core.management import BaseCommand

from core.models import Routine, Exercise, RoutineBridgeExercise


class Command(BaseCommand):
    def handle(self, *args, **options):
        routine = Routine.objects.create(
            name='Arms'
        )

        exercise = Exercise.objects.create(
            name='Curls',
        )

        RoutineBridgeExercise.objects.create(
            exercise=exercise,
            routine=routine,
            sets=3,
        )