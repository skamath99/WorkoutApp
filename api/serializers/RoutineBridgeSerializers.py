from rest_framework import serializers

from api.serializers.RoutineSerializers import RoutineListSerializer
from core.models import RoutineBridgeExercise, Exercise


# Helper Serializers
class ExerciseSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Exercise
        fields = ('name',)


#Main Serializers
class RoutineBridgeSerializer(serializers.HyperlinkedModelSerializer):
    exercise = ExerciseSerializer()
    routine = RoutineListSerializer()

    class Meta:
        model = RoutineBridgeExercise
        fields = ('exercise', 'routine', 'sets')
