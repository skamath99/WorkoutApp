from datetime import datetime

from django.db import models


# Create your models here.
class Routine(models.Model):
    name = models.CharField(max_length=20)

    def get_exercises(self):
        return Exercise.objects.filter(routine=self)

    def __str__(self):
        return self.name


class Exercise(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class RoutineBridgeExercise(models.Model):
    exercise = models.ForeignKey('core.Exercise')
    routine = models.ForeignKey('core.Routine')
    sets = models.IntegerField()


class StrengthHistory(models.Model):
    exercise = models.ForeignKey('core.Exercise', on_delete=models.CASCADE)
    routine = models.ForeignKey('core.Routine', related_name='exercises', on_delete=models.SET_NULL, null=True)
    order = models.IntegerField()
    reps = models.IntegerField()
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField(default=datetime.now)


class CardioHistory(models.Model):
    # add stuff for treadmill
    time = models.TimeField()
    calories = models.DecimalField(max_digits=6, decimal_places=2)
