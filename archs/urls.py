from django.conf.urls import patterns, include, url
from . import views

urlpatterns = patterns('',
    url(r'^getBuildings/$', views.get_building, name='get_building'),
)
