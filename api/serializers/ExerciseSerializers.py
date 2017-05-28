from rest_framework import serializers

from core.models import Exercise, Routine


class ExerciseSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api:exercise-detail')
    routine = serializers.SlugRelatedField(slug_field="name", queryset=Routine.objects.all())

    class Meta:
        model = Exercise
        fields = (
            'url',
            'routine',
            'name',
            'sets',
        )
