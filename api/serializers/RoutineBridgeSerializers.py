from rest_framework import serializers

from api.serializers.RoutineSerializers import RoutineListSerializer
from core.models import RoutineBridgeExercise, Exercise, Routine


# Helper Serializers
class ExerciseSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Exercise
        fields = ('name',)


# Main Serializers
class RoutineBridgeSerializer(serializers.HyperlinkedModelSerializer):
    exercise = serializers.HyperlinkedRelatedField(view_name='api:exercise-detail', many=False, read_only=False,
                                                   queryset=Exercise.objects.all())
    routine = serializers.HyperlinkedRelatedField(view_name='api:routine-detail', many=False, read_only=False,
                                                  queryset=Routine.objects.all())

    class Meta:
        model = RoutineBridgeExercise
        fields = ('exercise', 'routine', 'sets')
