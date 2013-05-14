__author__ = 'aszary'
from django.conf.urls import patterns, url

from database import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^all', views.all_, name='all'),
    url(r'^x-ray', views.x_ray, name='x-ray'),
    url(r'^download', views.get_atnf, name='get_atnf'),
    url(r'^sync', views.sync_atnf, name='sync_atnf'),
)

