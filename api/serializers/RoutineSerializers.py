from rest_framework import serializers


from core.models import Routine, RoutineBridgeExercise, Exercise


# Helper Serializers
class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ('name',)


class RoutineBridgeExerciseSerializer(serializers.ModelSerializer):

    exercise = serializers.StringRelatedField()

    class Meta:
        model = RoutineBridgeExercise
        fields = ('exercise', 'sets')


# Main Serializers

class RoutineListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:routine-detail')

    class Meta:
        model = Routine
        fields = ('url', 'name')


class RoutineDetailSerializer(serializers.ModelSerializer):
    exercises = RoutineBridgeExerciseSerializer(many=True)

    class Meta:
        model = Routine
        fields = ('name', 'exercises')
