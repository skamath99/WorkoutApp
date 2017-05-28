from rest_framework import viewsets

from api.serializers.ExerciseSerializers import ExerciseSerializer
from core.models import Exercise


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
