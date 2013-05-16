#! /usr/bin/env python
from sys import path
import os
from math import pi

# pretend to run from project main dir
path[0] = "/".join(os.path.abspath(__file__).split("/")[:-2])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pulsars.settings")
from django.core.exceptions import ObjectDoesNotExist
#import pulsars.settings
from database.models import Pulsar, XrayArticle, Additional, XrayFit, \
    XrayComponent, Geometry, Subpulses, Calculations
from database.calcs.const.const import CGS as c
from database.calcs.hot_spots import HotSpots


class Pulsars:

    def __init__(self):
        pass

    def add_pulsars(self):

        #    J0108-1431    ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J0108-1431', additional=True,
                                calculations=True, articles_num=2,
                                fits_num=[1,2], components_num=[[2],[1,1]])
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2012ApJ...761..117P'
        ar[0].cite = '\cite{2012_Posselt}'
        ar[0].info = ('page 4, 5(lum) BB + PL (51 counts) no inf -> surface '
                      'conversion, '
                      'second BB fit taken (0.73 c. d.), A_{\perp} here '
                      '[last update: 2013-05-15]')
        ar[0].dist = 0.210
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = 43e2
        co[0][0][0].r_plus = 24e2
        co[0][0][0].r_minus = 14e2
        co[0][0][0].t = self.ev_to_k(0.11e3)
        co[0][0][0].t_plus = self.ev_to_k(0.03e3)
        co[0][0][0].t_minus = self.ev_to_k(0.01e3)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 3.1
        co[0][0][1].pl_plus = 0.5
        co[0][0][1].pl_minus = 0.2
        co[0][0][1].lum = 3.7e28
        co[0][0][1].lum_plus = 3.2e28
        co[0][0][1].lum_minus = 2.1e28
        ad.dist_dm_cl = 0.184
        ad.dist_dm_cl_plus = 0.194 - 0.184
        ad.dist_dm_cl_minus = 0.184 - 0.167
        ad.dist_pi = 0.210
        ad.dist_pi_plus = 0.090
        ad.dist_pi_minus = 0.050
        ar[1].num = 1
        ar[1].article = 'http://adsabs.harvard.edu/abs/2009ApJ...691..458P'
        ar[1].cite = '\cite{2009_Pavlov}'
        ar[1].info = ('page 4, BB, PL (not enought counts for BB+PL) '
                      'recalculated for distance 0.184')
        ar[1].dist = 0.184
        fi[1][0].spectrum = 'BB'
        co[1][0][0].spec_type = 'BB'
        co[1][0][0].r = self.radius_from_area(53e4) * (184./130.)
        co[1][0][0].r_plus = self.radius_from_area(32e4) * (184./130.)
        co[1][0][0].r_minus = self.radius_from_area(21e4)* (184./130.)
        co[1][0][0].t = self.ev_to_k(279)
        co[1][0][0].t_plus = self.ev_to_k(35)
        co[1][0][0].t_minus = self.ev_to_k(28)
        co[1][0][0].lum = self.lbol_radius(co[1][0][0].t, co[1][0][0].r)
        fi[1][1].spectrum = 'PL'
        co[1][1][0].spec_type = 'PL'
        co[1][1][0].pl = 2.2
        co[1][1][0].pl_plus = 0.31
        co[1][1][0].pl_minus = 0.28
        co[1][1][0].lum = 2.1e28
        co[1][1][0].lum_plus = 3.8e+28
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #     B0628-28     ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B0628-28', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1, 0], components_num=[[2], []])
        ge.alpha = 70.
        ge.beta = -12.
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2005ApJ...630L..57'
        ar[0].cite = '\cite{2005_Tepedelenl}'
        ar[0].info = ('page 5, no inf -> surface conversion, looks like '
                      'A_{\perp}, P3 not mesured')
        ar[0].dist = 1.45
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = 59e2 / ca.f ** 0.5
        co[0][0][0].r_plus = 65e2 / ca.f ** 0.5
        co[0][0][0].r_minus = 46e2 / ca.f ** 0.5
        co[0][0][0].t = 3.28e6
        co[0][0][0].t_plus = 1.31e6
        co[0][0][0].t_minus = 0.62e6
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 2.98
        co[0][0][1].pl_plus = 0.91
        co[0][0][1].pl_minus = 0.65
        co[0][0][1].lum = 1.67e30
        co[0][0][1].lum_plus = 0.91e30
        co[0][0][1].lum_minus = 0.62e30
        ar[1].article = 'http://adsabs.harvard.edu/abs/2005ApJ...633..367B'
        ar[1].cite = '\cite{2005_Becker}'
        ar[1].info = ('...')
        ad.dist_dm_cl = 1.444
        ad.dist_dm_cl_plus= 1.444 - 1.167
        ad.dist_dm_cl_minus = 1.709 - 1.444
        ad.articles = 'http://adsabs.harvard.edu/abs/2005ApJ...633..367B'
        su.p2 = 30.
        su.p2_plus = 60.
        su.p2 = 6.
        su.p3 = 7.
        su.p3_plus = 1.
        su.p3_minus = 1.
        su.p4 = 8.71093017305
        su.article = 'http://adsabs.harvard.edu/abs/2006A%26A...445..243W'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        t = '''
        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=2,
                                fits_num=[1,1], components_num=[[2], [0]])
        ge.alpha =
        ge.beta =
        ge.rho =
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = ''
        ar[0].cite = '\cite{}'
        ar[0].info = ()
        ar[0].dist =
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r =
        co[0][0][0].r_plus =
        co[0][0][0].r_minus =
        co[0][0][0].t =
        co[0][0][0].t_plus =
        co[0][0][0].t_minus =
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl =
        co[0][0][1].pl_plus =
        co[0][0][1].pl_minus =
        co[0][0][1].lum =
        co[0][0][1].lum_plus =
        co[0][0][1].lum_minus =
        ar[1].article = ''
        ar[1].cite = '\cite{}'
        ar[1].info = ('')
        ad.dist_dm_cl =
        ad.dist_dm_cl_plus=
        ad.dist_dm_cl_minus =
        ad.articles = ''
        su.p2 =
        su.p2_plus =
        su.p2 =
        su.p3 =
        su.p3_plus =
        su.p3_minus =
        su.p4 =
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)
        # '''

    def remove_all(self):
        ca = Calculations.objects.all()
        for c in ca:
            c.delete()
        xc = XrayComponent.objects.all()
        for x in xc:
            x.delete()
        xf = XrayFit.objects.all()
        for x in xf:
            x.delete()
        ad = Additional.objects.all()
        for a in ad:
            a.delete()
        ge = Geometry.objects.all()
        for g in ge:
            g.delete()
        su = Subpulses.objects.all()
        for s in su:
            su.delete()
        xa = XrayArticle.objects.all()
        for x in xa:
            x.delete()

    def create_records(self, name='', additional=False, geometry=False,
                       subpulse=False, calculations=False, articles_num=2,
                       fits_num=[2, 1], components_num=[[3, 2], [2]]):
        """ too much tea?
        """

        p0 = Pulsar.objects.get(Name=name)
        if additional is True:
            try:
                a0 = Additional.objects.get(psr_id=p0)
            except ObjectDoesNotExist:
                a0 = Additional(psr_id=p0)
        else:
            a0 = None
        if geometry is True:
            try:
                g0 = Geometry.objects.get(psr_id=p0)
            except ObjectDoesNotExist:
                g0 = Geometry(psr_id=p0)
        else:
            g0 = None
        if subpulse is True:
            try:
                s0 = Subpulses.objects.get(psr_id=p0)
            except ObjectDoesNotExist:
                s0 = Subpulses(psr_id=p0)
        else:
            s0 = None
        if calculations is True:
            try:
                ca = Calculations.objects.get(psr_id=p0)
            except ObjectDoesNotExist:
                ca = Calculations(psr_id=p0)
        else:
            ca = None

        articles = []
        fits = []
        components = []

        for i in xrange(articles_num):
            try:
                x0 = XrayArticle.objects.get(psr_id=p0, num=i)
            except ObjectDoesNotExist:
                x0 = XrayArticle(psr_id=p0, num=i)
            x0.save()
            articles.append(x0)
            fits.append([])
            components.append([])
            for j in xrange(fits_num[i]):
                try:
                    f0 = XrayFit.objects.get(article_id=x0, num=j)
                except ObjectDoesNotExist:
                    f0 = XrayFit(article_id=x0, num=j)
                fits[-1].append(f0)
                f0.save()
                components[-1].append([])
                for k in xrange(components_num[i][j]):
                    try:
                        c0 = XrayComponent.objects.get(fit_id=f0, num=k)
                    except ObjectDoesNotExist:
                        c0 = XrayComponent(fit_id=f0, num=k)
                    components[-1][-1].append(c0)

        return p0, a0, g0, s0, ca, articles, fits, components

    def save_records(self, pu, ad, ge, su, ca, ar, fi, co):
        if pu is not None:
            pu.save()
        if ad is not None:
            ad.save()
        if ge is not None:
            ge.save()
        if su is not None:
            su.save()
        if ca is not None:
            ca.save()
        for i, a in enumerate(ar):
            if a is not None:
                a.save()
            for j, f in enumerate(fi[i]):
                if f is not None:
                    f.save()
                for k, c in enumerate(co[i][j]):
                    if c is not None:
                        c.save()

    def calculate(self, pu, ad, ge, su, ca, ar, fi, co):
        ca.dotP_15 = pu.P1 / 1e-15
        ca.a_dp = 6.58429132402614e8 / float(pu.P0)
        ca.r_dp = (ca.a_dp / pi ) ** 0.5
        ca.bsurf2 = 2.02 * 1e12 * float(pu.P0) ** 0.5 * ca.dotP_15 ** 0.5
        ca.b_14dp = ca.bsurf2 / 1e14
        ca.l_sd = 3.94784176043574e31 * ca.dotP_15 / float(pu.P0) ** 3.
        # find the correct fit for hot spot...:
        ii, jj = (0, 0)
        co_bb = None
        for i in xrange(len(ar)):
            for j in xrange(len(fi[i])):
                if fi[i][j].ordinal is not None:
                    ii, jj = (i, j)
                    break
        for k in xrange(len(co[ii][jj])):
            if co[ii][jj][k].spec_type == 'BB' and co[ii][jj][k].r < ca.r_dp:
                co_bb = co[ii][jj][k]
                break
        if co_bb is not None:
            ca.a = pi * co_bb.r ** 2.
            ca.b = ca.a_dp / ca.a
            ca.b_14 = ca.b * ca.b_14dp
            r_min = co_bb.r - co_bb.r_minus
            r_max = co_bb.r + co_bb.r_plus
            a_min = pi * r_min ** 2.
            a_max = pi * r_max ** 2.
            b_max = ca.a_dp / a_min
            b_min = ca.a_dp / a_max
            ca.b_14_minus = (ca.b - b_min) * ca.b_14dp
            ca.b_14_plus = (b_max - ca.b) * ca.b_14dp
        if ad.best_age is None:
            ad.best_age = pu.Age

    def radius_from_area(self, a):
        return (a / pi) ** 0.5

    def lbol_radius(self, t, r):
        """ Bolometric luminosity for  hot spot sigma T^4 A (radius)"""
        return c.sigma * t ** 4. * pi * r ** 2.

    def ev_to_k(self, t_ev):
        """ change electronoVolts to Kelvins
        """
        return t_ev / 8.61734315e-5


def main():
    p = Pulsars()
    p.add_pulsars()
    #p.remove_all()
    print 'Bye'


if __name__ == '__main__':
    main()
