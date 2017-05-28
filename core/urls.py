from django.conf.urls import url

from core import views

urlpatterns = [
    url(r'^$', views.view_routines, name='view_routines'),
    url(r'^add_routine/$', views.create_routine, name='create_routine'),
    url(r'^select_routine/$', views.select_routine, name='select_routine'),
]
