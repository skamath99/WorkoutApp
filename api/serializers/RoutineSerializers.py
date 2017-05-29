from rest_framework import serializers


from core.models import Routine, RoutineBridgeExercise


# Helper Serializers

class RoutineBridgeExerciseSerializer(serializers.ModelSerializer):
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