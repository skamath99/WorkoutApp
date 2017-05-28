from rest_framework import serializers

from core.models import Routine, Exercise


class ExerciseForRoutineListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:exercise-detail')

    class Meta:
        model = Exercise
        fields = (
            'url',
            'name',
            'sets',
        )


class RoutineListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:routine-detail')

    class Meta:
        model = Routine
        fields = (
            'url',
            'name',
        )


class RoutineDetailSerializer(serializers.HyperlinkedModelSerializer):
    exercises = ExerciseForRoutineListSerializer(source='get_exercises', many=True, read_only=True)

    class Meta:
        model = Routine
        fields = (
            'name',
            'exercises'
        )
