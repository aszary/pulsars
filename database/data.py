#! /usr/bin/env python
from sys import path
import os
from math import pi, sin

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
        self.m = 1.4 *1.9891e33
        self.r = 1e6
        self.gr = (1 - 2. * c.G * self.m / (self.r * c.c ** 2.)) ** 0.5

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
        fi[0][0].ordinal = 99
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
        su.p2_minus = 6.
        su.p3 = 7.
        su.p3_plus = 1.
        su.p3_minus = 1.
        su.p4 = 8.71093017305
        su.article = 'http://adsabs.harvard.edu/abs/2006A%26A...445..243W'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    B0834+06      ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B0834+06', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=1,
                                fits_num=[1], components_num=[[2]])
        ge.alpha = 60.7
        ge.beta = 4.5
        ge.rho = 7.1
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2008ApJ...686..497G'
        ar[0].cite = '\cite{2008_Gil}'
        ar[0].info = ('page 6, no inf -> surface conversion, r_bb calculated '
                      'from L \eq 4 A \sigma T^4, 1 sigma errors taken, '
                      'BB(2/3)+PL(1/3) BB+PL fits not included in database '
                      '(poor statistics..., no l_nonth), A_{\perp}')
        ar[0].dist = 0.643
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].t = self.ev_to_k(170)
        co[0][0][0].t_plus = self.ev_to_k(65)
        co[0][0][0].t_minus = self.ev_to_k(55)
        co[0][0][0].r = self.radius_from_lt_simple(8.6e28 / 4.,
                                                   co[0][0][0].t) /ca.f ** 0.5
        co[0][0][0].r_plus = 5643.465323
        co[0][0][0].r_minus = 1528.715528
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][0].lum_plus = 1.9e28
        co[0][0][0].lum_minus = 0.5e28
        co[0][0][1].spec_type = 'PL'
        # TODO add Photon Index!!
        #co[0][0][1].pl =
        #co[0][0][1].pl_plus =
        #co[0][0][1].pl_minus =
        co[0][0][1].lum = co[0][0][0].lum_plus
        # TODO add lum errors
        #co[0][0][1].lum_plus =
        #co[0][0][1].lum_minus =
        ad.dist_dm_cl = 0.643
        ad.dist_dm_cl_plus = 0.723 - 0.643
        ad.dist_dm_cl_minus = 0.643 - 0.567
        ad.articles = ('http://adsabs.harvard.edu/abs/2006A%26A...445..243W;'
                      'http://adsabs.harvard.edu/abs/1997MNRAS.288..631K;'
                      'http://adsabs.harvard.edu/abs/1988MNRAS.234..477L')
        su.info = 'other values for p2 and p3 in paper 40deg, 21 P0'
        su.p2 = 20.
        su.p2_plus = 55.
        su.p2_minus = 9.
        su.p3 = 2.2
        su.p3_plus = 0.2
        su.p3_minus = 0.2
        su.p4 = 38.4678024056707
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   B0943+10       ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B0943+10', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=3,
                                fits_num=[2,0,3], components_num=[[1,1], [],
                                                                  [2,1,1]])
        ge.alpha = 11.58
        ge.beta = -4.29
        ge.rho = 4.5
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2005ApJ...624L.109Z'
        ar[0].cite = '\cite{2005_Zhang}'
        ar[0].info = ('page 2, no inf -> surface conversion, cos(theta)=0.97,'
                      ' (dist=630  was used), A and T errors from graph '
                      '(T_max 0.36keV T_min 0.175keV A_max 5.8e3 A_min 2.9e2),'
                      ' in paper L_bol for cap (A used as A_{\perp}?)')
        ar[0].dist = 0.63
        fi[0][0].spectrum = 'BB'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].t = 3.1e6
        co[0][0][0].t_plus = self.ev_to_k(0.36e3-self.k_to_ev(3.1e6))
        co[0][0][0].t_minus = self.ev_to_k(self.k_to_ev(3.1e6)-0.175e3)
        co[0][0][0].r = self.radius_from_lt_simple(
            4.9e+28 / 2.,co[0][0][0].t) / ca.f ** 0.5
        a_ = pi * co[0][0][0].r ** 2.
        co[0][0][0].r_plus = self.radius_from_area(5.8e7 - a_)
        co[0][0][0].r_minus = self.radius_from_area(a_ - 2.9e6)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][0].lum_plus = 0.6e28 / ca.f
        co[0][0][0].lum_minus = 1.6e28 / ca.f
        fi[0][1].spectrum = 'PL'
        fi[0][1].ordinal = 99
        co[0][1][0].spec_type = 'PL'
        co[0][1][0].pl = 2.6
        co[0][1][0].pl_plus = 0.7
        co[0][1][0].pl_minus = 0.5
        co[0][1][0].lum = 2.4e29
        co[0][1][0].lum_plus = 0.8e29
        co[0][1][0].lum_minus = 0.7e29
        ar[1].article = 'http://adsabs.harvard.edu/abs/2006ApJ...636..406K'
        ar[1].cite = '\cite{2006_Kargaltsev}}'
        ad.dist_dm_cl = 0.631
        ad.dist_dm_cl_plus = 0.744 - 0.631
        ad.dist_dm_cl_minus = 0.631 - 0.527
        ad.articles = 'http://adsabs.harvard.edu/abs/2001MNRAS.326.1249A;' \
                      'http://adsabs.harvard.edu/abs/2001MNRAS.322..438D'
        ar[2].article = 'http://adsabs.harvard.edu/abs/2013Sci...339..436H'
        ar[2].cite = '\cite{2013_Hermsen}'
        ar[2].info = ('two modes -> data from presentation check article!'
                     '(radio quiescent mode)')
        ar[2].dist = 0.63
        # TODO get values from paper
        fi[2][0].spectrum = 'BB + PL'
        co[2][0][0].spec_type = 'BB'
        co[2][0][0].t = self.ev_to_k(0.277e3)
        co[2][0][0].t_plus = self.ev_to_k(0.012e3)
        co[2][0][0].t_minus = self.ev_to_k(0.012e3)
        #co[2][0][0].r =
        #co[2][0][0].r_plus =
        #co[2][0][0].r_minus =
        #co[2][0][0].lum =
        #co[2][0][0].lum_plus =
        #co[2][0][0].lum_minus =
        co[2][0][1].spec_type = 'PL'
        co[2][0][1].pl = 2.6
        co[2][0][1].pl_plus = 0.34
        co[2][0][1].pl_minus = 0.34
        #co[2][0][1].lum =
        #co[2][0][1].lum_plus =
        #co[2][0][1].lum_minus =
        fi[2][1].spectrum = 'BB'
        co[2][1][0].spec_type = 'BB'
        co[2][1][0].t = self.ev_to_k(0.250e3)
        co[2][1][0].t_plus = self.ev_to_k(0.006e3)
        co[2][1][0].t_minus = self.ev_to_k(0.006e3)
        #co[2][1][0].r =
        #co[2][1][0].r_plus =
        #co[2][1][0].r_minus =
        #co[2][1][0].lum =
        #co[2][1][0].lum_plus =
        #co[2][1][0].lum_minus =
        fi[2][2].spectrum = 'PL'
        co[2][2][0].spec_type = 'PL'
        co[2][2][0].pl = 2.29
        co[2][2][0].pl_plus = 0.16
        co[2][2][0].pl_minus = 0.16
        #co[2][2][0].lum =
        #co[2][2][0].lum_plus =
        #co[2][2][0].lum_minus =
        su.p2 = 18.
        su.p3 = 2.0285601425812803
        su.article = 'http://adsabs.harvard.edu/abs/1997MNRAS.288..631K'
        su.info = 'P_2 = 10.5[deg] in second paper...'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #     B0950+08     ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B0950+08', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=3,
                                fits_num=[1, 0, 0], components_num=[[2], [],
                                                                  []])
        ge.alpha = 105.4
        ge.beta = 22.1
        #ge.rho = 0. ???
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2004ApJ...616..452Z'
        ar[0].cite = '\cite{2004_Zavlin}'
        ar[0].info = ('page 7, PL+BB (good for eff. vs. age)  A_{\perp} '
                      '(R is in fact R_{\perp})')
        ar[0].dist = 0.262
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_inf(5000, ca.f)
        co[0][0][0].r_plus = self.radius_from_inf(3200, ca.f)
        co[0][0][0].r_minus = self.radius_from_inf(3200, ca.f)
        co[0][0][0].t = 1.75e6 / self.gr
        co[0][0][0].t_plus = 0.22e6 / self.gr
        co[0][0][0].t_minus = 0.22e6 / self.gr
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][0].lum_plus = 0.8e29 / self.gr ** 2. / ca.f
        co[0][0][0].lum_minus = 0.8e29 / self.gr ** 2. / ca.f
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 1.31
        co[0][0][1].pl_plus = 0.14
        co[0][0][1].pl_minus = 0.14
        # no inf conversion?
        co[0][0][1].lum = 9.7e29
        co[0][0][1].lum_plus = 0.1e29
        co[0][0][1].lum_minus = 0.1e29
        ar[1].article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        ar[1].cite = '\cite{2007_Zavlin}'
        ar[2].article = 'http://adsabs.harvard.edu/abs/2004ApJ...615..908B'
        ar[2].cite = '\cite{2004_Becker}'
        ad.dist_dm_cl = 0.255
        ad.dist_dm_cl_plus = 0.271 - 0.255
        ad.dist_dm_cl_minus = 0.255 - 0.224
        ad.dist_pi = 0.262
        ad.dist_pi_plus = 0.267 - 0.262
        ad.dist_pi_minus = 0.262 - 0.257
        ad.articles = ('http://adsabs.harvard.edu/abs/2007A%26A...469..607W;'
                       'http://adsabs.harvard.edu/abs/1997MNRAS.288..631K;'
                       'http://adsabs.harvard.edu/abs/1980A%26A....86....7W')
        su.p2 = -500. # ??
        su.p2_plus = 100.
        su.p2_minus = 300.
        su.p3 = 6.5
        su.p3_plus = 2.2
        su.p3_minus = 2.2
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    B1133+16      ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1133+16', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=1,
                                fits_num=[2], components_num=[[1, 1]])
        ge.alpha = 52.5
        ge.beta = 4.5
        ge.rho = 7.4
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2006ApJ...636..406K'
        ar[0].cite = '\cite{2006_Kargaltsev}'
        ar[0].info = ('page 2/3, PL, BB, no inf -> surface conversion, '
                      'cos(th.) = 0.47, T is taken from graph (in paper '
                      'T = 2.8MK), PL and BB separate fits, A_{\perp}')
        ar[0].dist = 0.357
        fi[0][0].spectrum = 'BB'
        fi[0][0].ordinal  = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_area(5e6) / ca.f ** 0.5
        co[0][0][0].r_plus = self.radius_from_area(3e6) / ca.f ** 0.5
        co[0][0][0].r_minus = self.radius_from_area(22e5) / ca.f ** 0.5
        co[0][0][0].t = self.ev_to_k(0.28e3)
        co[0][0][0].t_plus = self.ev_to_k(0.04e3)
        co[0][0][0].t_minus = self.ev_to_k(0.03e3)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][0].lum_plus = 0.5e28
        co[0][0][0].lum_minus = 0.6e28
        fi[0][1].spectrum = 'PL'
        fi[0][1].ordinal  = 99
        co[0][1][0].spec_type = 'PL'
        co[0][1][0].pl = 2.51
        co[0][1][0].pl_plus = 0.36
        co[0][1][0].pl_minus = 0.33
        co[0][1][0].lum, co[0][1][0].lum_plus, co[0][1][0].lum_minus = \
            self.lnonth_powers([[29.46,0.37,0.60], [28.66,0.29,0.51]])
        ad.dist_dm_cl = 0.333
        ad.dist_dm_cl_plus = 0.363 - 0.333
        ad.dist_dm_cl_minus = 0.333 - 0.304
        ad.dist_pi = 0.357
        ad.dist_pi_plus = 0.370 - 0.350
        ad.dist_pi_minus = 0.350 - 0.330
        ad.articles = ('http://adsabs.harvard.edu/abs/1997MNRAS.288..631K;'
                       'http://adsabs.harvard.edu/abs/2006A%26A...445..243W;'
                       'http://adsabs.harvard.edu/abs/1988MNRAS.234..477L')
        su.p2 = 130
        su.p2_plus = 55
        su.p2_minus = 90
        su.p3 = 3
        su.p3_plus = 2
        su.p3_minus = 2
        su.info = 'second fit in paper P_2=200, P_3=3'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    B1257+12      ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1257+12', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=1,
                                fits_num=[2], components_num=[[1, 1]])
        pu.comment = 'sol'
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2007ApJ...664.1072P'
        ar[0].cite = '\cite{2007_Pavlov}'
        ar[0].info = ('page 2, 8, PL, BB? recalculated from 500pc to 447pc '
                      '(l_bol is different), high errors for pi distance '
                      '(assumed 0.4),a lot of milisecond pulsar data in paper '
                      'l_bol = L_bol /gr^4?? A_{\perp}')
        ar[0].dist = 0.447
        fi[0][0].spectrum = 'BB'
        fi[0][0].ordinal  = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_area(2.1e3 * 1e4) * (447. / 500.)
        co[0][0][0].r_plus = self.radius_from_area(1.9e3 * 1e4) * (447. / 500.)
        co[0][0][0].r_minus = self.radius_from_area(0.9e3 * 1e4) * (447. /500.)
        co[0][0][0].t = self.ev_to_k(0.215e3)
        co[0][0][0].t_plus = self.ev_to_k(0.025e3)
        co[0][0][0].t_minus = self.ev_to_k(0.023e3)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        fi[0][1].spectrum = 'PL'
        fi[0][1].ordinal  = 99
        co[0][1][0].spec_type = 'PL'
        co[0][1][0].pl = 2.75
        co[0][1][0].pl_plus = 0.34
        co[0][1][0].pl_minus = 0.36
        co[0][1][0].lum = 2.47e29
        co[0][1][0].lum_plus = 0.5e29
        co[0][1][0].lum_minus = 0.48e29
        ad.dist_dm_cl = 0.447
        ad.dist_dm_cl_plus= 0.447 - 0.379
        ad.dist_dm_cl_minus = 0.519 - 0.447
        ad.dist_pi = 0.8
        ad.dist_pi_plus = 0.4
        ad.dist_pi_minus = 0.4
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #     J1740-5340A  ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J1740-5340A', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 0], components_num=[[2], []])
        pu.comment = 'NGC 6397'
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2010ApJ...709..241B'
        ar[0].cite = '\cite{2010_Bogdanov}'
        ar[0].info = ('page 5, 3, PL + BB , A_{\perp}')
        ar[0].dist = 2.4
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = 0.15e5 * (3.4 / 2.4)
        co[0][0][0].r_plus = 0.09e5
        co[0][0][0].r_minus = 0.13e5
        co[0][0][0].t = self.ev_to_k(0.19e3)
        co[0][0][0].t_plus = self.ev_to_k(0.09e3)
        co[0][0][0].t_minus = self.ev_to_k(0.04e3)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 1.56
        co[0][0][1].pl_plus = 0.18
        co[0][0][1].pl_minus = 0.23
        # TODO add nonthermal luminosities
        #co[0][0][1].lum =
        #co[0][0][1].lum_plus =
        #co[0][0][1].lum_minus =
        ar[1].article = 'http://adsabs.harvard.edu/abs/2002ApJ...581..470G'
        ar[1].cite = '\cite{2002_Grindlay}'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   B1929+10       ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1929+10', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=1,
                                fits_num=[1], components_num=[[2], [0]])
        ge.alpha = 35.97
        ge.beta = 25.55
        #ge.rho = 0. ??
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2008ApJ...685.1129M'
        ar[0].cite = '\cite{2008_Misanovic}'
        ar[0].info = ('page 33,42, PL+BB, inf -> surface conversion done, '
                      'f=0.897, Different paralax distance!! 0.33 +-0.01 or '
                      '0.361+-0.01 (newer paper used), l_bol  =  L_bol / (2 '
                      'f gr^2) used, l_bol = L_bol / 4 (sphere to spot '
                      'correction) l_bol = L_bol /gr^4??  A_{\perp}')
        ar[0].dist = 0.361
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_inf(3310, ca.f)
        co[0][0][0].r_plus = self.radius_from_inf(590, ca.f)
        co[0][0][0].r_minus = self.radius_from_inf(460, ca.f)
        co[0][0][0].t = self.ev_to_k(0.30e3) / self.gr
        co[0][0][0].t_plus = self.ev_to_k(0.02e3) / self.gr
        co[0][0][0].t_minus = self.ev_to_k(0.03e3) / self.gr
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 1.73
        co[0][0][1].pl_plus = 0.46
        co[0][0][1].pl_minus = 0.66
        co[0][0][1].lum = 1.7e30
        #co[0][0][1].lum_plus =
        #co[0][0][1].lum_minus =
        ad.dist_dm_cl = 0.335
        ad.dist_dm_cl_plus = 0.388 - 0.335
        ad.dist_dm_cl_minus = 0.335 - 0.282
        ad.dist_pi = 0.361
        ad.dist_pi_plus = 0.340 - 0.330
        ad.dist_pi_minus = 0.330 - 0.320
        ad.articles = ('http://adsabs.harvard.edu/abs/2006A%26A...445..243W;'
                       'http://adsabs.harvard.edu/abs/1997MNRAS.288..631K;'
                       'http://adsabs.harvard.edu/abs/2001ApJ...553..341E')
        su.p2 = 90
        su.p2_plus = 140
        su.p2_minus = 8
        su.p3 = 4.4
        su.p3_plus = 0.8
        su.p3_minus = 0.8
        su.article = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #     J0633+1746   ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J0633+1746', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 1], components_num=[[3], [3]])
        pu.comment = 'Geminga'
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2005ApJ...633.1114J'
        ar[0].cite = '\cite{2005_Jackson}'
        ar[0].info = ('page 26, PL+BB, no inf -> surface conversion,  Geminga '
                      'pulsar, NO L_bol, dist_bb etc.!!, L_bol calculated for '
                      'spot (only hot spot component was used), L_bol_sphere2 '
                      'is very high!')
        ar[0].dist = 0.157
        fi[0][0].spectrum = 'BB + BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = 6200.
        co[0][0][0].r_plus = 3400.
        co[0][0][0].r_minus = 3400.
        co[0][0][0].t = 1.71e6
        co[0][0][0].t_plus = 0.23e6
        co[0][0][0].t_minus = 0.23e6
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'BB'
        co[0][0][1].r = 11.17e5
        co[0][0][1].r_plus = 1.09e5
        co[0][0][1].r_minus = 1.09e5
        co[0][0][1].t = 0.48e6
        co[0][0][1].t_plus = 0.002e6
        co[0][0][1].t_minus = 0.002e6
        co[0][0][1].lum = self.lbol_radius(co[0][0][1].t, co[0][0][1].r)
        co[0][0][2].spec_type = 'PL'
        co[0][0][2].pl = 1.684
        co[0][0][2].pl_plus = 0.06
        co[0][0][2].pl_minus = 0.06
        co[0][0][2].lum, co[0][0][2].lum_plus, co[0][0][2].lum_minus = \
            self.lnonth_powers([[29.90,0.2,0.35],[29.98,0.2,0.35]])
        ar[1].num = 1
        ar[1].article = 'http://adsabs.harvard.edu/abs/2005ApJ...625..307K'
        ar[1].cite = '\cite{2005_Kargaltsev}'
        ar[1].info = ('page 8, PL+BB, no inf -> surface conversion, Geminga,'
                      ' two component bb fit, R, R+ and R- recalculated for '
                      'distance (0.157, 0.2 not used)! R_bb (best dist), check'
                      ' PSR_J0633+1746 for newer paper, L_bol calculated for '
                      'spot (only hot spot component was used), L_bol_sphere '
                      'is very high!')
        ar[1].dist = 0.157
        fi[1][0].spectrum = 'BB + BB + PL'
        co[1][0][0].spec_type = 'BB'
        co[1][0][0].r = 4600. * (157./200.)
        co[1][0][0].r_plus = 1200. * (157./200.)
        co[1][0][0].r_minus = 1200. * (157./200.)
        co[1][0][0].t = 2.32e6
        co[1][0][0].t_plus = 0.08e6
        co[1][0][0].t_minus = 0.08e6
        co[1][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[1][0][1].spec_type = 'BB'
        co[1][0][1].r = 12.9e5 * (157./200.)
        co[1][0][1].r_plus = 1e5 * (157./200.)
        co[1][0][1].r_minus = 1e5 * (157./200.)
        co[1][0][1].t = 0.49e6
        co[1][0][1].t_plus = 0.01e6
        co[1][0][1].t_minus = 0.01e6
        co[1][0][1].lum = self.lbol_radius(co[0][0][1].t, co[0][0][1].r)
        co[1][0][2].spec_type = 'PL'
        co[1][0][2].pl = 1.56
        co[1][0][2].pl_plus = 0.24
        co[1][0][2].pl_minus = 0.24
        co[1][0][2].lum = 1.3e30
        co[1][0][2].lum_plus = 0.2e30
        co[1][0][2].lum_minus = 0.2e30
        ad.dist_dm_cl = 3.907
        ad.dist_dm_cl_plus = 5.573 - 3.907
        ad.dist_dm_cl_minus = 3.907 - 2.795
        ad.dist_pi = 0.157
        ad.dist_pi_plus = 0.059
        ad.dist_pi_minus = 0.034
        ad.articles = ('http://adsabs.harvard.edu/abs/2007astro.ph..2426Z;'
                       'http://adsabs.harvard.edu/abs/2005ApJ...623.1051D')
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    J0821-4300      ##################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J0821-4300', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=1,
                                fits_num=[1], components_num=[[2],])
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2010ApJ...724.1316G'
        ar[0].cite = '\cite{2010_Gotthelf}'
        ar[0].info = ('page 6, no inf -> surface conversion, 10 km radius '
                      'taken R = 10*sin(beta), READ WHIOLE PAPER!!!   '
                      'A_{\perp}')
        ar[0].dist = 2.2
        fi[0][0].spectrum = 'BB + BB'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.r * sin(7./180. * pi)
        co[0][0][0].r_plus = 0.11 * co[0][0][0].r
        co[0][0][0].r_minus = 0.11 * co[0][0][0].r
        co[0][0][0].t = self.ev_to_k(0.540e3)
        co[0][0][0].t_plus = 0.03 * co[0][0][0].t
        co[0][0][0].t_minus = 0.03 * co[0][0][0].t
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'BB'
        co[0][0][1].r = self.r * sin(37./180. * pi)
        co[0][0][1].r_plus = 0.06 * co[0][0][1].r
        co[0][0][1].r_minus = 0.06 * co[0][0][1].r
        co[0][0][1].t = self.ev_to_k(280)
        co[0][0][1].t_plus = 0.03 * co[0][0][1].t
        co[0][0][1].t_minus = 0.03 * co[0][0][1].t
        co[0][0][1].lum = self.lbol_radius(co[0][0][1].t, co[0][0][1].r)
        ad.best_age = 3.7e3
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    J0538+2817    ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J0538+2817', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=3,
                                fits_num=[2, 0, 0], components_num=[[1 ,1],
                                                                    [0], [0]])
        pu.comment = 'SNR S147'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2003ApJ...591..380M'
        ar[0].cite = '\cite{2003_Mcgowan}'
        ar[0].info = ('age 22 (second fit for best N_H), inf -> surface '
                      'conversion done, no PL, no equation for L_bol (R_bb)'
                      ' paralax distance taken from the newest paper, no '
                      'equation -> assumed A_{\perp}')
        ar[0].dist = 1.2
        fi[0][0].spectrum = 'BB'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_inf(0.87e5)
        co[0][0][0].r_plus = self.radius_from_inf(0.05e5)
        co[0][0][0].r_minus = self.radius_from_inf(0.05e5)
        co[0][0][0].t = 2.12e6 / self.gr
        co[0][0][0].t_plus = 0.04e6 / self.gr
        co[0][0][0].t_minus = 0.04e6 / self.gr
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        fi[0][1].spectrum = 'AT'
        co[0][1][0].spec_type = 'AT'
        co[0][1][0].t = 1.1e6
        co[0][1][0].r = 10.5e5
        co[0][1][0].b_atm = 1e12
        ar[1].article = 'http://adsabs.harvard.edu/abs/2004MmSAI..75..458Z'
        ar[1].cite = '\cite{2004_Zavlin}'
        ar[2].article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        ar[2].cite = '\cite{2007_Zavlin}'
        ad.dist_dm_cl = 1.206
        ad.dist_dm_cl_plus = 1.438 - 1.206
        ad.dist_dm_cl_minus = 1.206 - 0.972
        ad.dist_pi = 1.30
        ad.dist_pi_plus = 0.22
        ad.dist_pi_minus = 0.16
        ad.best_age = 30e3
        ad.articles = 'http://adsabs.harvard.edu/abs/2009ApJ...698..250C'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    B0656+14      ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B0656+14', additional=True,
                                calculations=True, geometry=True,
                                subpulse=True,
                                articles_num=4,
                                fits_num=[2, 0, 0, 0],
                                components_num=[[3, 1], [], [], []])
        ar[0].article = 'http://adsabs.harvard.edu/abs/2005ApJ...623.1051D'
        ar[0].cite = '\cite{2005_Deluca}'
        ar[0].info = ('page 25, no inf -> surface conversion, two component '
                      'bb fit, L_bol for spot... A_{\perp}')
        ar[0].dist = 0.288
        fi[0][0].spectrum = 'BB + BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = 180000
        co[0][0][0].r_plus = 15000
        co[0][0][0].r_minus = 15000
        co[0][0][0].t = 1.25e6
        co[0][0][0].t_plus = 0.03e6
        co[0][0][0].t_minus = 0.03e6
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'BB'
        co[0][0][1].r = 20.9e5
        co[0][0][1].r_plus = 2.7e5
        co[0][0][1].r_minus = 3.8e5
        co[0][0][1].t = 6.5e5
        co[0][0][1].t_plus = 0.1e5
        co[0][0][1].t_minus = 0.1e5
        co[0][0][1].lum = self.lbol_radius(co[0][0][1].t, co[0][0][1].r)
        co[0][0][2].spec_type = 'PL'
        co[0][0][2].pl = 2.1
        co[0][0][2].pl_plus = 0.3
        co[0][0][2].pl_minus = 0.3
        co[0][0][2].lum = 1.8e30
        # TODO add errors
        #co[0][0][2].lum_plus =
        #co[0][0][2].lum_minus =
        fi[0][1].spectrum = 'AT'
        co[0][1][0].spec_type = 'AT'
        co[0][1][0].t = 0.8e6
        co[0][1][0].r = 7.5e5
        ar[1].article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        ar[1].cite = '\cite{2007_Zavlin}'
        ar[2].article = 'http://adsabs.harvard.edu/abs/1996A%26A...313..565P'
        ar[2].cite = '\cite{1996_Possenti}'
        ar[3].article = 'http://adsabs.harvard.edu/abs/2002nsps.conf..273P'
        ar[3].cite = '\cite{2002_Pavlov}'
        ad.dist_dm_cl = 0.669
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   B0833-45       ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B0833-45', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=4,
                                fits_num=[2, 0, 0, 1],
                                components_num=[[2, 1], [], [], [3]])
        pu.comment = 'Vela'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        ar[0].cite = '\cite{2007_Zavlin_b}'
        ar[0].info = ('page 16 , inf -> surface conversion, Vela, assumed'
                      ' A_{\perp}, last paper (p. 16)')
        ar[0].dist = 0.210
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_inf(2.1e5)
        co[0][0][0].r_plus = self.radius_from_inf(0.2e5)
        co[0][0][0].r_minus = self.radius_from_inf(0.2e5)
        co[0][0][0].t = self.t_from_inf(1.49e6)
        co[0][0][0].t_plus = self.t_from_inf(0.04e6)
        co[0][0][0].t_minus = self.t_from_inf(0.04e6)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 2.7
        co[0][0][1].pl_plus = 0.4
        co[0][0][1].pl_minus = 0.4
        co[0][0][1].lum = 4.2e32
        # TODO add nonthermal lum errs.
        #co[0][0][1].lum_plus =
        #co[0][0][1].lum_minus =
        fi[0][1].spectrum = 'AT'
        co[0][1][0].spec_type = 'AT'
        co[0][1][0].t = 0.68e6
        co[0][1][0].r = 10e5
        ar[1].article = 'http://adsabs.harvard.edu/abs/2001ApJ...552L.129P'
        ar[1].cite = '\cite{2001_Pavlov}'
        ar[2].article = 'http://adsabs.harvard.edu/abs/2002nsps.conf..273P'
        ar[2].cite = '\cite{2002_Pavlov}'
        ar[3].article = 'http://adsabs.harvard.edu/abs/2007ApJ...669..570M'
        ar[3].cite = '\cite{2007_Manzali}'
        ar[3].info = ('page 1,20, (L_bol) no inf -> surface conversion, new '
                      'paper for Vela (Chandra observations), another good fit'
                      ' in paper, A_{\perp}')
        ar[3].dist = 0.287
        fi[3][0].spectrum = 'BB + BB + PL'
        fi[3][0].ordinal = 99
        co[3][0][0].spec_type = 'BB'
        co[3][0][0].r = 0.73e5
        co[3][0][0].r_plus = 0.09e5
        co[3][0][0].r_minus = 0.07e5
        co[3][0][0].t = 2.16e6
        co[3][0][0].t_plus = 0.06e6
        co[3][0][0].t_minus = 0.07e6
        co[3][0][0].lum = self.lbol_radius(co[3][0][0].t, co[3][0][0].r)
        co[3][0][1].spec_type = 'BB'
        co[3][0][1].r = 5.06e5
        co[3][0][1].r_plus = 0.42e5
        co[3][0][1].r_minus = 0.28e5
        co[3][0][1].t = 1.06e6
        co[3][0][1].t_plus = 0.03e6
        co[3][0][1].t_minus = 0.03e6
        co[3][0][1].lum = self.lbol_radius(co[3][0][1].t, co[3][0][1].r)
        co[3][0][2].spec_type = 'PL'
        co[3][0][2].pl = 2.2
        co[3][0][2].pl_plus = 0.4
        co[3][0][2].pl_minus = 0.3
        co[3][0][2].lum = 5.74e32
        ad.dist_dm_cl = 0.236
        ad.dist_pi = 0.287
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    B1055-52      ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1055-52', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=3,
                                fits_num=[1, 0, 0],
                                components_num=[[3], [], []])
        ar[0].article = 'http://adsabs.harvard.edu/abs/2005ApJ...623.1051D'
        ar[0].cite = '\cite{2005_Deluca}'
        ar[0].info = ('page 25, no inf -> surface conversion, two component'
                      ' bb fit, no L_bol, diffrent values in second paper?!'
                      ' ... A_{\perp}')
        ar[0].dist = 0.75
        fi[0][0].spectrum = 'BB + BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = 46000
        co[0][0][0].r_plus = 6000
        co[0][0][0].r_minus = 6000
        co[0][0][0].t = 1.79e6
        co[0][0][0].t_plus = 0.06e6
        co[0][0][0].t_minus = 0.06e6
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'BB'
        co[0][0][1].r = 12.3e5
        co[0][0][1].r_plus = 1.5e5
        co[0][0][1].r_minus = 0.7e5
        co[0][0][1].t = 7.9e5
        co[0][0][1].t_plus = 0.3e5
        co[0][0][1].t_minus = 0.3e5
        co[0][0][1].lum = self.lbol_radius(co[0][0][1].t, co[0][0][1].r)
        co[0][0][2].spec_type = 'PL'
        co[0][0][2].pl = 1.7
        co[0][0][2].pl_plus = 0.1
        co[0][0][2].pl_minus = 0.1
        co[0][0][2].lum = 8.1e30
        # TODD complete
        #co[0][0][2].lum_plus =
        #co[0][0][2].lum_minus =
        ar[1].article = 'http://adsabs.harvard.edu/abs/2002nsps.conf..273P'
        ar[1].cite = '\cite{2002_Pavlov}'
        ar[2].article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        ar[2].cite = '\cite{2007_Zavlin}'
        ad.dist_dm_cl = 0.726
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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
        su.p2_minus =
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

    def lnonth_powers(self, pow_):
        l_nth = 0.
        l_nth_plus = 0.
        l_nth_minus = 0.
        l_nth_min = 0.
        l_nth_max = 0.
        for p in pow_:
            l_nth += 10. ** p[0]
            l_nth_max += 10 ** (p[0]+p[1])
            l_nth_min += 10 ** (p[0]-p[2])
        l_nth_plus = l_nth_max - l_nth
        l_nth_minus = l_nth - l_nth_min
        return l_nth, l_nth_plus, l_nth_minus

    def radius_from_inf(self, r_inf, f=None):
        if f is  not None:
            return r_inf * f ** (-0.5) * self.gr
        else:
            return r_inf * self.gr

    def t_from_inf(self, t_inf):
        return t_inf / self.gr

    def radius_from_lt_simple(self, l_bol, t):
        return (l_bol / (c.sigma * t ** 4. * pi)) ** 0.5

    def radius_from_area(self, a):
        return (a / pi) ** 0.5

    def lbol_radius(self, t, r):
        """ Bolometric luminosity for  hot spot sigma T^4 A (radius)"""
        return c.sigma * t ** 4. * pi * r ** 2.

    def ev_to_k(self, t_ev):
        """ change electronoVolts to Kelvins
        """
        return t_ev / 8.61734315e-5

    def k_to_ev(self, t_k):
        return t_k * 8.61734315e-5


def main():
    p = Pulsars()
    p.add_pulsars()
    #p.remove_all()
    print 'Bye'


if __name__ == '__main__':
    main()
