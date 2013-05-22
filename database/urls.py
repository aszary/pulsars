__author__ = 'aszary'
from django.conf.urls import patterns, url

from database import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^psrs/(?P<id>\d+)', views.psrs, name='psrs'),
    url(r'^psrs', views.psrs, name='psrs'),
    url(r'^x-ray', views.x_ray, name='x-ray'),
    url(r'^download', views.get_atnf, name='get_atnf'),
    url(r'^sync', views.sync_atnf, name='sync_atnf'),
    url(r'^latex/table_bb', views.table_bb, name='table_bb'),
    url(r'^latex/table_psrs', views.table_psrs, name='table_psrs'),
    url(r'^latex/table_pl', views.table_pl, name='table_pl'),
    url(r'^plots/xray_age', views.xray_age, name='xray_age'),
    url(r'^plots/radio', views.radio, name='radio'),
)

