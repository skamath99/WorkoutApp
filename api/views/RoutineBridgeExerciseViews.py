from rest_framework import viewsets

from api.serializers import RoutineBridgeExerciseSerializer
from core.models import RoutineBridgeExercise


class RoutineBridgeExerciseViewSet(viewsets.ModelViewSet):
    queryset = RoutineBridgeExercise.objects.all()
    serializer_class = RoutineBridgeExerciseSerializer