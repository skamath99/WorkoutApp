from rest_framework import viewsets

from api.serializers import RoutineDetailSerializer
from api.serializers import RoutineListSerializer
from core.models import Routine


class RoutineViewSet(viewsets.ModelViewSet):
    queryset = Routine.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return RoutineListSerializer
        if self.action == 'retrieve':
            return RoutineDetailSerializer
        else:
            return RoutineListSerializer
