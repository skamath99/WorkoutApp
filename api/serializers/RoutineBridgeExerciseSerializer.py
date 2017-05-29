from rest_framework import serializers

from core.models import RoutineBridgeExercise


class RoutineBridgeExerciseSerializer(serializers.Serializer):
    sets = serializers.IntegerField()

    class Meta:
        model = RoutineBridgeExercise
        fields = ('sets',)