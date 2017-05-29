from rest_framework import serializers

from apitests.models import Owner, Bakery


class OwnerSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()

    class Meta:
        model = Owner
        fields = ('first_name', 'last_name')


class BakerySerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    owners = OwnerSerializer(many=True)

    class Meta:
        model = Bakery
        fields = ('name', 'owners')
