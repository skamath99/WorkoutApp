from rest_framework import serializers

from api.serializers.RoutineBridgeExerciseSerializer import RoutineBridgeExerciseSerializer
from api.serializers.ExerciseSerializers import ExerciseSerializer
from core.models import Routine, RoutineBridgeExercise


# Helper Serializers

# class ExerciseSerializer(serializers.Serializer):


# Main Serializers

class RoutineListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:routine-detail')

    class Meta:
        model = Routine
        fields = ('url', 'name')


class RoutineDetailSerializer(serializers.Serializer):
    sets = RoutineBridgeExerciseSerializer(many=True)

    class Meta:
        model = Routine
        fields = (
            'name',
            'sets',
        )
