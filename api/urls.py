from django.conf.urls import include, url
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'routines', views.RoutineViewSet, 'routine')
router.register(r'routinebridgeexercise', views.RoutineBridgeViewSet, 'routinebridgeexercise')
router.register(r'exercise', views.ExerciseViewSet, 'exercise')

urlpatterns = [
    url(r'^', include(router.urls)),
]
