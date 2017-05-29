from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers

from apitests.ReverseRelationTests import views

router = routers.DefaultRouter()
router.register(r'bakery', views.BakeryViewSet, 'bakery')

urlpatterns = [
    url(r'^', include(router.urls)),
]