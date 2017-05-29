from rest_framework import viewsets

from apitests.ReverseRelationTests.serializers import BakerySerializer
from apitests.models import Bakery


class BakeryViewSet(viewsets.ModelViewSet):
    queryset = Bakery.objects.all()
    serializer_class = BakerySerializer
