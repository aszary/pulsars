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
                                calculations=True, geometry=False,
                                subpulse=False,
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

        #   J1119-6127     ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J1119-6127', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=4,
                                fits_num=[1, 0, 0, 0],
                                components_num=[[2], [], [], []])
        pu.comment = 'G292.2-0.5'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2007Ap%26SS.308...89G'
        ar[0].cite = '\cite{2007_Gonzalez}'
        ar[0].info = ('page 3, no inf -> surface conversion, component is '
                      'pulsing; fixed size in atmospheric fit (1.6kpc '
                      'distance)')
        ar[0].dist = 8.4
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_inf(3.4e5)
        co[0][0][0].r_plus = self.radius_from_inf(1.8e5)
        co[0][0][0].r_minus = self.radius_from_inf(0.3e5)
        co[0][0][0].t = self.t_from_inf(2.4e6)
        co[0][0][0].t_plus = self.t_from_inf(0.3e6)
        co[0][0][0].t_minus = self.t_from_inf(0.2e6)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 1.5
        co[0][0][1].pl_plus = 0.3
        co[0][0][1].pl_minus = 0.2
        co[0][0][1].lum =  0.9e33
        co[0][0][1].lum_plus = 0.5e33
        co[0][0][1].lum_minus = 0.1e33
        ar[1].article = 'http://adsabs.harvard.edu/abs/2008ApJ...684..532S'
        ar[1].cite = '\cite{2008_Safi-Harb}'
        ar[2].article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        ar[2].cite = '\cite{2007_Zavlin}'
        ar[3].article = 'http://adsabs.harvard.edu/abs/2005ApJ...630..489G'
        ar[3].cite = '\cite{2005_Gonzalez}'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    J1210-5226    ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J1210-5226', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=1,
                                fits_num=[2], components_num=[[1, 1]])
        pu.comment = 'G296.5+10.0'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2002nsps.conf..273P'
        ar[0].cite = '\cite{2002_Pavlov}'
        ar[0].info = ('page 10, radio quiet, no inf -> surface conversion, '
                      'uncertainness in distance evaluation, no radio signal'
                      ' \dot{P} 1e-14 1e-17  A_{\perp}')
        ar[0].dist = 2.45
        fi[0][0].spectrum = 'BB'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_inf(1.6e5)
        co[0][0][0].t = self.t_from_inf(2.9e6)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        fi[0][1].spectrum = 'AT'
        co[0][1][0].spec_type = 'AT'
        co[0][1][0].r = self.radius_from_inf(11e5)
        co[0][1][0].t = self.t_from_inf(1.6e6)
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   J1357-6429     ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J1357-6429', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[2, 0], components_num=[[2, 1], []])
        ar[0].article = 'http://adsabs.harvard.edu/abs/2007ApJ...665L.143Z'
        ar[0].cite = '\cite{2007_Zavlin}'
        ar[0].info = ('page 3, no inf -> surface conversion, A_{\perp}')
        ar[0].dist = 2.5
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_inf(2.5e5)
        co[0][0][0].r_plus = self.radius_from_inf(0.5e5)
        co[0][0][0].r_minus = self.radius_from_inf(0.5e5)
        co[0][0][0].t = self.t_from_inf(1.7e6)
        co[0][0][0].t_plus = self.t_from_inf(0.2e6)
        co[0][0][0].t_minus = self.t_from_inf(0.2e6)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 1.3
        co[0][0][1].pl_plus = 0.2
        co[0][0][1].pl_minus = 0.2
        co[0][0][1].lum = 1.4e32
        # TODO add errors
        #co[0][0][1].lum_plus =
        #co[0][0][1].lum_minus =
        fi[0][1].spectrum = 'AT'
        co[0][1][0].r = 10e5
        co[0][1][0].t = 1e6
        ar[1].article = 'http://adsabs.harvard.edu/abs/2012ApJ...744...81C'
        ar[1].cite = '\cite{2012_Chang}'
        ad.dist_dm_cl = 2.5
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   B1706-44       ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1706-44', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=3,
                                fits_num=[2, 0, 0],
                                components_num=[[2,1], [], []])
        pu.comment = 'G343.1-02.3'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2002ApJ...567L.125G'
        ar[0].cite = '\cite{2002_Gotthelf}'
        ar[0].info = ('page 5, no inf -> surface conversion, thermal + '
                      'non-thermal components A_{\perp}')
        ar[0].dist = 2.5
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_inf(3.6e5)
        co[0][0][0].r_plus = self.radius_from_inf(0.9e5)
        co[0][0][0].r_minus = self.radius_from_inf(0.9e5)
        co[0][0][0].t = self.t_from_inf(1.66e6)
        co[0][0][0].t_plus = self.t_from_inf(0.17e6)
        co[0][0][0].t_minus = self.t_from_inf(0.15e6)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 2.0
        co[0][0][1].pl_plus = 0.5
        co[0][0][1].pl_minus = 0.5
        co[0][0][1].lum = 1.45e32
        co[0][0][1].lum_plus = 0.46e32
        co[0][0][1].lum_minus = 0.08e32
        fi[0][1].spectrum = 'AT'
        co[0][1][0].r = 12e5
        co[0][1][0].t = 1e6
        ar[1].article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        ar[1].cite = '\cite{2007_Zavlin}'
        ar[1].article = 'http://adsabs.harvard.edu/abs/2006ApJ...639..377M'
        ar[1].cite = '\cite{2006_McGowan}'
        ad.dist_dm_cl = 2.311
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   J1809-1917     ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J1809-1917', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=1,
                                fits_num=[1], components_num=[[2]])
        ar[0].article = 'http://adsabs.harvard.edu/abs/2007ApJ...670..655K'
        ar[0].cite = '\cite{2007_Kargaltsev}'
        ar[0].info = ('page 5, 7(graph), no inf -> surface conversion, '
                      'dist_dm_cl from paper A_{\perp}')
        ar[0].dist = 3.5
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_area(2.84e6*1e4)
        co[0][0][0].r_plus = self.radius_from_area(2.66e6*1e4)
        co[0][0][0].r_minus = self.radius_from_area(1.51e6*1e4)
        co[0][0][0].t = self.ev_to_k(0.17e3)
        co[0][0][0].t_plus = self.ev_to_k(0.03e3)
        co[0][0][0].t_minus = self.ev_to_k(0.03e3)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 1.23
        co[0][0][1].pl_plus = 0.62
        co[0][0][1].pl_minus = 0.62
        co[0][0][1].lum = 0.37e32
        co[0][0][1].lum_plus = 0.12e32
        co[0][0][1].lum_minus = 0.1e32
        ad.dist_dm_cl = 3.5
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   B1823-13       ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1823-13', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=1,
                                fits_num=[1], components_num=[[2]])
        pu.comment = 'Vela-like'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2008ApJ...675..683P'
        ar[0].cite = '\cite{2008_Pavlov}'
        ar[0].info = ('page 13, no inf -> surface conversion, very bad '
                      'photon statistics, R_BB fixed in fits - larger R_BB '
                      'fit in paper, A_{\perp}')
        ar[0].dist = 4
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_area(20e10)
        # TODO add errors
        #co[0][0][0].r_plus =
        #co[0][0][0].r_minus =
        co[0][0][0].t = self.ev_to_k(139.)
        co[0][0][0].t_plus = self.ev_to_k(9.)
        co[0][0][0].t_minus = self.ev_to_k(6.)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 1.7
        co[0][0][1].pl_plus = 0.7
        co[0][0][1].pl_minus = 0.7
        co[0][0][1].lum = 0.6e32
        # TODO add errors
        #co[0][0][1].lum_plus =
        #co[0][0][1].lum_minus =
        ad.dist_dm_cl = 3.9
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    B1916+14      ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1916+14', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=1,
                                fits_num=[2], components_num=[[1,1]])
        ar[0].article = 'http://adsabs.harvard.edu/abs/2009ApJ...704.1321Z'
        ar[0].cite = '\cite{2009_Zhu}'
        ar[0].info = ('page 12, BB, no inf -> surface conversion, check table '
                      'for more pulsars, A_{\perp}')
        ar[0].dist = 2.1
        fi[0][0].spectrum = 'BB'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = 0.8e5
        co[0][0][0].r_plus = 0.1e5
        co[0][0][0].r_minus = 0.1e5
        co[0][0][0].t = self.ev_to_k(0.13e3)
        co[0][0][0].t_plus = self.ev_to_k(0.01e3)
        co[0][0][0].t_minus = self.ev_to_k(0.01e3)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        fi[0][1].spectrum = 'PL'
        fi[0][1].ordinal = 99
        co[0][1][0].spec_type = 'PL'
        co[0][1][0].pl = 3.5
        co[0][1][0].pl_plus = 1.6
        co[0][1][0].pl_minus = 0.7
        co[0][1][0].lum = 1e32
        # TODO add errors
        #co[0][0][1].lum_plus =
        #co[0][0][1].lum_minus =
        ad.dist_dm_cl = 2.059
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    J2043+2740    ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J2043+2740', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[2, 0], components_num=[[2, 1], []])
        ar[0].article = 'http://adsabs.harvard.edu/abs/2004ApJ...615..908B'
        ar[0].cite = '\cite{2004_Becker}'
        ar[0].info = ('page 27, R_BB fixed in fits - larger R_BB fit in paper,'
                      ' inf -> surface conversion done (see text T_inf), '
                      'different values in second paper ?, errors from bb fit,'
                      '  A_{\perp}?')
        ar[0].dist = 1.8
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_inf(0.467e5)
        co[0][0][0].r_plus = self.radius_from_inf(0.2e5)
        co[0][0][0].r_minus = self.radius_from_inf(0.2e5)
        co[0][0][0].t = self.t_from_inf(self.ev_to_k(0.125e3))
        co[0][0][0].t_plus = self.t_from_inf(self.ev_to_k(0.03e3))
        co[0][0][0].t_minus = self.t_from_inf(self.ev_to_k(0.03e3))
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 2.8
        co[0][0][1].pl_plus = 1
        co[0][0][1].pl_minus = 0.8
        co[0][0][1].lum, co[0][0][1].lum_plus, co[0][0][1].lum_minus = \
            self.lnonth_powers([[31.40,0.22,0.45],[29.90,0.22,0.45]])
        fi[0][1].spectrum = 'AT'
        co[0][1][0].t = 0.6e6
        co[0][1][0].r = 9.0e5
        ar[1].article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        ar[1].cite = '\cite{2007_Zavlin}'
        ad.dist_dm_cl = 1.802
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    B2334+61      ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B2334+61', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[2, 0], components_num=[[2,1], []])
        ar[0].article = 'http://adsabs.harvard.edu/abs/2006ApJ...639..377M'
        ar[0].cite = '\cite{2006_McGowan}'
        ar[0].info = ('pag 4,14, inf -> surface conversion done, no pulsation,'
                      ' different values in second paper ? (, R_bb 1.66e5 from'
                      ' text different fit?) A_{\perp}? no data (R_bb) for '
                      'BB+PL (BB params from text), spectrum dominated by BB')
        ar[0].dist = 3.1
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_inf(1.66e5)
        co[0][0][0].r_plus = self.radius_from_inf(0.59e5)
        co[0][0][0].r_minus = self.radius_from_inf(0.39e5)
        co[0][0][0].t = self.t_from_inf(1.62e6)
        co[0][0][0].t_plus = self.t_from_inf(0.35e6)
        co[0][0][0].t_minus = self.t_from_inf(0.58e6)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 2.2
        co[0][0][1].pl_plus = 3.0
        co[0][0][1].pl_minus = 1.4
        co[0][0][1].lum = 3.1e-14 * 4. * pi * (3.1e3 * 3.0857e18) ** 2.
        # TODO add errors
        #co[0][0][1].lum_plus =
        #co[0][0][1].lum_minus =
        fi[0][1].spectrum = 'AT'
        co[0][1][0].spec_type = 'AT'
        co[0][1][0].t = 0.76e6
        co[0][1][0].r = 10e5
        ar[1].article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        ar[1].cite = '\cite{2007_Zavlin}'
        ad.dist_dm_cl = 3.131
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    J0205+6449    ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J0205+6449', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=1,
                                fits_num=[2], components_num=[[2, 1]])
        pu.comment = '3C58'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2004ApJ...616..403S'
        ar[0].cite = '\cite{2004_Slane}'
        ar[0].info = ('page 8 (in text), different value in table (page 9) -'
                      ' R_bb set to star radius there, PL from table, '
                      'redshifted or unredshifted?')
        ar[0].dist = 3.2
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_inf(10.7e5)
        # TODO add errors
        #co[0][0][0].r_plus = self.radius_from_inf()
        #co[0][0][0].r_minus = self.radius_from_inf()
        co[0][0][0].t = self.t_from_inf(1.3e6)
        #co[0][0][0].t_plus = self.t_from_inf()
        #co[0][0][0].t_minus = self.t_from_inf()
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 1.78
        co[0][0][1].pl_plus = 0.02
        co[0][0][1].pl_minus = 0.04
        co[0][0][1].lum = 1.02e-12 * 4. * pi * (ar[0].dist * 1e3 *
                                                3.0857e18) ** 2.
        #co[0][0][1].lum_plus =
        #co[0][0][1].lum_minus =
        fi[0][1].spectrum = 'AT'
        co[0][1][0].spec_type = 'AT'
        co[0][1][0].t = 1.08e6
        co[0][1][0].r = 10e5
        #ad.dist_dm_cl =
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #     B0355+54     ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B0355+54', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 0], components_num=[[2], []])
        ar[0].article = 'http://adsabs.harvard.edu/abs/2007Ap%26SS.308..309M'
        ar[0].cite = '\cite{2007_McGowan}'
        ar[0].info = ('page (312), inf -> surface conversion done (is it ok?)')
        ar[0].dist = 1.04
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = self.radius_from_inf(0.12e5)
        co[0][0][0].r_plus = self.radius_from_inf(0.16e5)
        co[0][0][0].r_minus = self.radius_from_inf(0.07e5)
        co[0][0][0].t = self.t_from_inf(2.32e6)
        co[0][0][0].t_plus = self.t_from_inf(1.16e6)
        co[0][0][0].t_minus = self.t_from_inf(0.81e6)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 1.
        co[0][0][1].pl_plus = 0.2
        co[0][0][1].pl_minus = 0.2
        co[0][0][1].lum, co[0][0][1].lum_plus, co[0][0][1].lum_minus = \
            self.lnonth_powers([[30.21,0.64,0.71],[30.83,0.57,0.33]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/1994ApJ...437..458S'
        ar[1].cite = '\cite{1994_Slane}'
        ad.dist_dm_cl = 1.447
        ad.dist_pi = 1.04
        ad.dist_pi_plus = 0.21
        ad.dist_pi_minus = 0.16
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   B0531+21       ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B0531+21', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=5,
                                fits_num=[1, 0, 0, 0, 0],
                                components_num=[[1], [], [], [], []])
        pu.comment = 'Crab'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[0].cite = '\cite{2009_Becker}'
        ar[0].info = ('page 41 (Becker), (no BB fit, PL dominated)')
        ar[0].dist = pu.Dist
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.63
        co[0][0][0].pl_plus = 0.07
        co[0][0][0].pl_minus = 0.07
        co[0][0][0].lum = 8.912509381337513e+35
        co[0][0][0].lum_plus = 4.5771194445791014e+35
        co[0][0][0].lum_minus = 3.0240728277815817e+35
        ar[1].article = 'http://adsabs.harvard.edu/abs/2011ApJ...743..139W'
        ar[1].cite = '\cite{2011_Weisskopf}'
        ar[2].article = 'http://adsabs.harvard.edu/abs/2004ApJ...601.1050W'
        ar[2].cite = '\cite{2004_Weisskopf}'
        ar[3].article = 'http://adsabs.harvard.edu/abs/1997A%26A...326..682B'
        ar[3].cite = '\cite{1997_Becker}'
        ar[4].article = 'http://adsabs.harvard.edu/abs/2001A%26A...365L.212W'
        ar[4].cite = '\cite{2001_Willingale}'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #     B1951+32     ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1951+32', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=1,
                                fits_num=[1], components_num=[[2], []])
        pu.comment = 'CTB 80'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2005ApJ...628..931L'
        ar[0].cite = '\cite{2005_Li}'
        ar[0].info = ('page 3, no inf -> surface conversion done')
        ar[0].dist = 2.0
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = 2.2e5
        co[0][0][0].r_plus = 1.4e5
        co[0][0][0].r_minus = 0.8e5
        co[0][0][0].t = self.ev_to_k(0.13e3)
        co[0][0][0].t_plus = self.ev_to_k(0.02e3)
        co[0][0][0].t_minus = self.ev_to_k(0.02e3)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 1.63
        co[0][0][1].pl_plus = 0.03
        co[0][0][1].pl_minus = 0.05
        co[0][0][1].lum = .5e-12 * 4. * pi * (ar[0].dist * 1e3 *
                                              3.0857e18) ** 2.
        co[0][0][1].lum_plus = 9.30906e+32
        co[0][0][1].lum_minus = 1.7687e+32
        ad.dist_dm_cl = 3.137
        ad.articles = ''
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    B1509-58      ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1509-58', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=3,
                                fits_num=[1, 0, 0],
                                components_num=[[1], [], []])
        pu.comment = 'Crab-like pulsar'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2001A%26A...375..397C'
        ar[0].cite = '\cite{2001_Cusumano}'
        ar[0].info = ('PL only ... check cite order')
        ar[0].dist = 4.181
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.19
        co[0][0][0].pl_plus = 0.04
        co[0][0][0].pl_minus = 0.04
        co[0][0][0].lum, co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[34.64,0.19,0.35],[35.12,0.2,0.37]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[1].cite = '\cite{2009_Becker}'
        ar[2].article = 'http://adsabs.harvard.edu/abs/2006ApJ...640..929D'
        ar[2].cite = '\cite{2006_DeLaney}'
        ad.dist_dm_cl = 4.181
        ad.dist_dm_cl_plus= 4.784 - ad.dist_dm_cl
        ad.dist_dm_cl_minus = ad.dist_dm_cl - 3.570
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #     J1930+1852   ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J1930+1852', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 0], components_num=[[1], []])
        pu.comment = 'Crab-like pulsar'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2007ApJ...663..315L'
        ar[0].cite = '\cite{2007_Lu}'
        ar[0].info = ('??')
        ar[0].dist = 5.
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.2
        co[0][0][0].pl_plus = 0.2
        co[0][0][0].pl_minus = 0.2
        co[0][0][0].lum, co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[33.42,0.22,0.45],[33.75,0.22,0.45]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2002ApJ...574L..71C'
        ar[1].cite = '\cite{2002_Camilo}'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    J1617-5055    ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J1617-5055', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 0], components_num=[[1], []])
        pu.comment = 'Crab-like pulsar'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2009ApJ...690..891K'
        ar[0].cite = '\cite{2009_Kargaltsev}'
        ar[0].info = ('page (889, table)')
        ar[0].dist = 6.5
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.14
        co[0][0][0].pl_plus = 0.06
        co[0][0][0].pl_minus = 0.06
        co[0][0][0].lum = 17.92e33
        co[0][0][0].lum_plus = 0.07e33
        co[0][0][0].lum_minus = 0.07e33
        ar[1].article = 'http://adsabs.harvard.edu/abs/2002nsps.conf...64B'
        ar[1].cite = '\cite{2002_Becker}'
        ar[1].info = ('')
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    J1747-2958    ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J1747-2958', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 1], components_num=[[1], [1]])
        pu.comment = 'Mouse'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[0].cite = '\cite{2009_Becker}'
        ar[0].info = ('PL fit values from Becker paper')
        ar[0].dist = 5.
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.8
        co[0][0][0].pl_plus = 0.08
        co[0][0][0].pl_minus = 0.08
        co[0][0][0].lum, co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[33.82,0.26,0.23],[33.75,0.24,0.23]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2004ApJ...616..383G'
        ar[1].cite = '\cite{2004_Gaensler}'
        ar[1].info = ('page 8 (BB)')
        fi[1][0].spectrum = 'BB'
        #fi[1][0].ordinal = 99
        co[1][0][0].spec_type = 'BB'
        # TODO where are BB parameters
        #co[1][0][0].r =
        #co[1][0][0].r_plus =
        #co[1][0][0].r_minus =
        #co[1][0][0].t =
        #co[1][0][0].t_plus =
        #co[1][0][0].t_minus =
        #co[1][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    J1124-5916    ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J1124-5916', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=3,
                                fits_num=[1, 0, 0],
                                components_num=[[1], [], []])
        pu.comment = 'Vela-like pulsar'
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[0].cite = '\cite{2009_Becker}'
        ar[0].info = ('PL fit from Becker, only upper limit for BB')
        ar[0].dist = 6.
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.6
        co[0][0][0].pl_plus = 0.1
        co[0][0][0].pl_minus = 0.1
        co[0][0][0].lum, co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[32.54,0.22,0.45],[32.66,0.22,0.45]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2003ApJ...591L.139H'
        ar[1].cite = '\cite{2003_Hughes}'
        ar[2].article = 'http://adsabs.harvard.edu/abs/2003ApJ...583L..91G'
        ar[2].cite = '\cite{2003_Gonzales}'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   B1046-58       ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1046-58', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 0], components_num=[[1], []])
        pu.comment = 'Vela-like pulsar'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[0].cite = '\cite{2009_Becker}'
        ar[0].info = ('')
        ar[0].dist = 2.7
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.7
        co[0][0][0].pl_plus = 0.4
        co[0][0][0].pl_minus = 0.2
        co[0][0][0].lum, co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[31.73,0.52,0.46],[31.75,0.3,0.43]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2006ApJ...652..569G'
        ar[1].cite = '\cite{2006_Gonzalez}'
        ar[1].info = ('')
        ad.dist_dm_cl = 2.714
        ad.dist_dm_cl_plus = 3.060 - ad.dist_dm_cl
        ad.dist_dm_cl_minus = ad.dist_dm_cl - 2.363
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #     J1811-1925     ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J1811-1925', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=3,
                                fits_num=[1, 0, 0],
                                components_num=[[1], [], []])
        pu.comment = 'G11.2-0.3'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[0].cite = '\cite{2009_Becker}'
        ar[0].info = ('different Gamma and flux in paper, radio quiet')
        ar[0].dist = 5.
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 0.97
        co[0][0][0].pl_plus = 0.39
        co[0][0][0].pl_minus = 0.32
        co[0][0][0].lum, co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[33.23,0.29,0.4],[33.88,0.18,0.31]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2003ApJ...588..992R'
        ar[1].cite = '\cite{2003_Roberts}'
        ar[2].article = 'http://adsabs.harvard.edu/abs/2004AIPC..714..306R'
        ar[2].cite = '\cite{2004_Roberts}'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #  J0537-6910      ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J0537-6910', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 0], components_num=[[1], []])
        pu.comment = 'N157B, LMC'
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[0].cite = '\cite{2009_Becker}'
        ar[0].info = ('')
        ar[0].dist = 47
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.8
        co[0][0][0].pl_plus = 0.1
        co[0][0][0].pl_minus = 0.1
        co[0][0][0].lum,  co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[35.68,0.19,0.34],[35.61,0.2,0.37]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2005A%26A...431..659M'
        ar[1].cite = '\cite{2005_Mignani}'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    B1259-63      ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1259-63', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=3,
                                fits_num=[1, 0, 0],
                                components_num=[[1], [], []])
        pu.comment = 'Be-star bin'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[0].cite = '\cite{2009_Becker}'
        ar[0].info = ('PL fit from Becker, binary star -> variable flux')
        ar[0].dist = 2.
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.69
        co[0][0][0].pl_plus = 0.04
        co[0][0][0].pl_minus = 0.04
        co[0][0][0].lum, co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[32.55,0.25,0.54],[32.58,0.39,0.51]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2009MNRAS.397.2123C'
        ar[1].cite = '\cite{2009_Chernyakova}'
        ar[2].article = 'http://adsabs.harvard.edu/abs/2006MNRAS.367.1201C'
        ar[2].cite = '\cite{2006_Chernyakova}'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    J1420-6048    ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J1420-6048', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 0],
                                components_num=[[1], []])
        ar[0].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[0].cite = '\cite{2009_Becker}'
        ar[0].info = ('PL fit from Becker, some evidence for thermal emission')
        ar[0].dist = 8.
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.6
        co[0][0][0].pl_plus = 0.04
        co[0][0][0].pl_minus = 0.04
        co[0][0][0].lum, co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[34.41,0.22,0.45],[34.52,0.22,0.45]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2001ApJ...561L.187R'
        ar[1].cite = '\cite{2001_Roberts}'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   B1800-21       ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1800-21', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=1,
                                fits_num=[1], components_num=[[2]])
        pu.comment = 'Vela-like pulsar'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2007ApJ...660.1413K'
        ar[0].cite = '\cite{2007_Kargaltsev}'
        ar[0].info = ('page 1, no R_BB (strong interstellar absorption)')
        ar[0].dist = 4.
        fi[0][0].spectrum = 'BB + PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        # TODO where is radius!!?
        #co[0][0][0].r =
        #co[0][0][0].r_plus =
        #co[0][0][0].r_minus =
        co[0][0][0].t = self.ev_to_k(0.2e3)
        co[0][0][0].t_plus = self.ev_to_k(0.1e3)
        co[0][0][0].t_minus = self.ev_to_k(0.1e3)
        #co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 1.4
        co[0][0][1].pl_plus = 0.6
        co[0][0][1].pl_minus = 0.6
        co[0][0][1].lum = 4e31
        # TODO add errors
        #co[0][0][1].lum_plus =
        #co[0][0][1].lum_minus =
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   B1757-24       ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1757-24', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 0], components_num=[[1], [0]])
        pu.comment = 'Duck'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2001ApJ...562L.163K'
        ar[0].cite = '\cite{2001_Kaspi}'
        ar[0].info = ('page 9, thermal fit T=1e8')
        ar[0].dist = 5
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.6
        co[0][0][0].pl_plus = 0.6
        co[0][0][0].pl_minus = 0.5
        co[0][0][0].lum, co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[33.1,0.54,0.53],[33.21,0.26,0.53]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[1].cite = '\cite{2009_Becker}'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    B0540-69      ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B0540-69', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 0], components_num=[[1], []])
        pu.comment = 'N158A, LMC'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2001ApJ...546.1159K'
        ar[0].cite = '\cite{2001_Kaaret}'
        ar[0].info = ('page 7,')
        ar[0].dist = 55.
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.92
        co[0][0][0].pl_plus = 0.11
        co[0][0][0].pl_minus = 0.11
        co[0][0][0].lum, co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[36.68,0.19,0.32],[36.49,0.21,0.37]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2008MNRAS.389..691C'
        ar[1].cite = '\cite{2008_Campana}'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   J1105-6107     ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J1105-6107', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 0], components_num=[[1], [0]])
        ar[0].article = 'http://adsabs.harvard.edu/abs/1998ApJ...497L..29G'
        ar[0].cite = '\cite{1998_Gotthelf}'
        ar[0].info = ('page 1, L from Becker')
        ar[0].dist = 7.
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.8
        co[0][0][0].pl_plus = 0.4
        co[0][0][0].pl_minus = 0.4
        co[0][0][0].lum, co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[33.65,0.39,0.50],[33.57,0.18,0.31]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[1].cite = '\cite{2009_Becker}'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   B1853+01     ######################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B1853+01', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 0], components_num=[[1], [0]])
        pu.comment = 'W44'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2002ApJ...579..404P'
        ar[0].cite = '\cite{2002_Petre}'
        ar[0].info = ('page 6, L from Becker ')
        ar[0].dist = 2.6
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.28
        co[0][0][0].pl_plus = 0.48
        co[0][0][0].pl_minus = 0.48
        co[0][0][0].lum, co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[31.53,0.44,0.54],[31.92,0.19,0.34]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[1].cite = '\cite{2009_Becker}'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #   J1509-5850     ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J1509-5850', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=2,
                                fits_num=[1, 0], components_num=[[1], [0]])
        pu.comment = 'MSH 15-52'
        ar[0].article = 'http://adsabs.harvard.edu/abs/2007A%26A...470..965H'
        ar[0].cite = '\cite{2007_Hui}'
        ar[0].info = ('page 2, L from Becker BB fit t=1e7, r=10m ')
        ar[0].dist = 2.56
        fi[0][0].spectrum = 'PL'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'PL'
        co[0][0][0].pl = 1.
        co[0][0][0].pl_plus = 0.2
        co[0][0][0].pl_minus = 0.3
        co[0][0][0].lum, co[0][0][0].lum_plus, co[0][0][0].lum_minus = \
            self.lnonth_powers([[31.43,0.2,0.4],[31.55,0.35,0.54]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[1].cite = '\cite{2009_Becker}'
        ad.dist_dm_cl = 2.56
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        #    J2021+3651    ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J2021+3651', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
                                articles_num=3,
                                fits_num=[2, 0, 0],
                                components_num=[[1, 1], [], []])
        ar[0].article = 'http://adsabs.harvard.edu/abs/2008ApJ...680.1417V'
        ar[0].cite = '\cite{2008_VanEtten}'
        ar[0].info = ('page 10, page 9 (in second paper)  remove from B/T '
                      'plot, The distance to PSR J2021+3651 is intriguing ,'
                      ' L from Becker BB ')
        ar[0].dist = 10.
        fi[0][0].spectrum = 'BB'
        fi[0][0].ordinal = 99
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = 7.0e5
        co[0][0][0].r_plus = 4e5
        co[0][0][0].r_minus = 1.7e5
        co[0][0][0].t = self.t_from_inf(self.ev_to_k(0.16e3))
        co[0][0][0].t_plus = self.t_from_inf(self.ev_to_k(0.02e3))
        co[0][0][0].t_minus = self.t_from_inf(self.ev_to_k(0.02e3))
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        fi[0][1].spectrum = 'PL'
        fi[0][1].ordinal = 99
        co[0][1][0].spec_type = 'PL'
        co[0][1][0].pl = 1.7
        co[0][1][0].pl_plus = 0.3
        co[0][1][0].pl_minus = 0.2
        co[0][1][0].lum, co[0][1][0].lum_plus, co[0][1][0].lum_minus = \
            self.lnonth_powers([[34.13,0.23,0.56],[33.97,0.18,0.33]])
        ar[1].article = 'http://adsabs.harvard.edu/abs/2004ApJ...612..389H'
        ar[1].cite = '\cite{2004_Hessels}'
        ar[2].article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        ar[2].cite = '\cite{2009_Becker}'
        ad.articles = 'http://adsabs.harvard.edu/abs/2009ApJ...700.1059A'
        self.calculate(pu, ad, ge, su, ca, ar, fi, co)
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        t = '''
        #          ####################################################
        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='', additional=True,
                                calculations=True, geometry=False,
                                subpulse=False,
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
                                calculations=True, geometry=False,
                                subpulse=False,
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
                                calculations=True, geometry=False,
                                subpulse=False,
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
                                calculations=True, geometry=False,
                                subpulse=False,
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
                                calculations=True, geometry=False,
                                subpulse=False,
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
                                calculations=True, geometry=False,
                                subpulse=False,
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
                                calculations=True, geometry=False,
                                subpulse=False,
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
                                calculations=True, geometry=False,
                                subpulse=False,
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
                                calculations=True, geometry=False,
                                subpulse=False,
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
            s.delete()
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
        if co_bb is not None and co_bb.r is not None:
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
