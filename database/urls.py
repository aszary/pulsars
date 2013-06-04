__author__ = 'aszary'
from django.conf.urls import patterns, url

from database import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^pulsars/(?P<id>\d+)', views.pulsars, name='pulsars'),
    url(r'^pulsars', views.pulsars, name='pulsars'),
    url(r'^xray', views.x_ray, name='x_ray'),
    url(r'^download', views.get_atnf, name='get_atnf'),
    url(r'^sync_malov', views.sync_malov, name='sync_malov'),
    url(r'^sync', views.sync_atnf, name='sync_atnf'),
    url(r'^latex/table_bb', views.table_bb, name='table_bb'),
    url(r'^latex/table_psrs', views.table_psrs, name='table_psrs'),
    url(r'^latex/table_pl', views.table_pl, name='table_pl'),
    url(r'^latex/custom', views.custom_data, name='custom_data'),
    url(r'^plots/radio/malov', views.malov_radio, name='malov_radio'),
    url(r'^plots/radio/xi_sd_age', views.xi_sd_age_radio, name='xi_sd_age_radio'),
    url(r'^plots/radio/xi_sd', views.xi_sd_radio, name='xi_sd_radio'),
    url(r'^plots/radio/xi_age', views.xi_age_radio, name='xi_age_radio'),
    url(r'^plots/radio/l_sd_three', views.l_sd_radio_three, name='l_sd_radio_three'),
    url(r'^plots/radio/l_sd', views.l_sd_radio, name='l_sd_radio'),
    url(r'^plots/radio/ll_sd', views.ll_sd_radio, name='ll_sd_radio'),
    url(r'^plots/radio/flux_sd', views.flux_sd_radio, name='flux_sd_radio'),
    url(r'^plots/radio/checks', views.checks_radio, name='checks_radio'),
    url(r'^plots/radio', views.radio, name='radio'),
    url(r'^plots/xi_xray_gamma', views.xi_xray_gamma, name='xi_xray_gamma'),
    url(r'^plots/xi_age', views.xi_age, name='xi_age'),
    url(r'^plots/bb_pl', views.bb_pl, name='bb_pl'),
    url(r'^plots/xi_field', views.xi_field, name='xi_field'),
    url(r'^plots/xi_sd', views.xi_sd, name='xi_sd'),
    url(r'^plots/pl_sd', views.pl_sd, name='pl_sd'),
    url(r'^plots/b_parameter', views.b_parameter, name='b_parameter'),
    url(r'^plots/b_age', views.b_age, name='b_age'),
    url(r'^plots/t6_b14', views.t6_b14, name='t6_b14'),
    url(r'^plots/custom', views.custom, name='custom'),
)

