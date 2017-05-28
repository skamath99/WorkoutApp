from django.conf.urls import include, url
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'routines', views.RoutineViewSet, 'routine')
router.register(r'exercises', views.ExerciseViewSet, 'exercise')

urlpatterns = [
    url(r'^', include(router.urls)),
]
