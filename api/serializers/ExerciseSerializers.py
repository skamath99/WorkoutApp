from rest_framework import serializers

from core.models import Exercise


class ExerciseSerializer(serializers.ModelSerializer):
    name = serializers.CharField()

    class Meta:
        model = Exercise
        fields = ('name',)