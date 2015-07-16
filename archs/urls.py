from django.conf.urls import patterns, include, url
from . import views
from handlers import getBuildingsHandler

urlpatterns = patterns('',
    url(r'^getBuildings/$', views.get_building, name='get_building'),
    url(r'^getBuilding/$', getBuildings_Handler),
)
