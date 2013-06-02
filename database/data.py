#! /usr/bin/env python
from sys import path
import os
from math import pi, sin

# pretend to run from project main dir
path[0] = "/".join(os.path.abspath(__file__).split("/")[:-2])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pulsars.settings")
from django.core.exceptions import ObjectDoesNotExist
#import pulsars.settings
from database.models import Pulsar, XrayArticle, Additional, XrayFit, XrayComponent, Geometry, Subpulse, Calculation
from database.calcs.const.const import CGS as c
from database.calcs.hot_spots import HotSpots


class Pulsars:

    def __init__(self):
        self.m = 1.4 *1.9891e33
        self.r = 1e6
        self.gr = (1 - 2. * c.G * self.m / (self.r * c.c ** 2.)) ** 0.5

    def add_pulsars(self):

        #    J0108-1431    ####################################################
        p = Pulsar.objects.get(name='J0108-1431')
        a1 = self.article_get_add(p, num=0)
        a1.articile = 'http://adsabs.harvard.edu/abs/2012ApJ...761..117P'
        a1.cite = '\cite{2012_Posselt}'
        a1.info = ('page 4, 5(lum) BB + PL (51 counts) no inf -> surface conversion, second BB fit taken (0.73 c. d.), A_{\perp} here [last update: 2013-05-15]')
        a1.dist = 0.210
        a1.save()
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 43e2
        c1.r_plus = 24e2
        c1.r_minus = 14e2
        c1.t = self.ev_to_k(0.11e3)
        c1.t_plus = self.ev_to_k(0.03e3)
        c1.t_minus = self.ev_to_k(0.01e3)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 3.1
        c2.pl_plus = 0.5
        c2.pl_minus = 0.2
        c2.lum = 3.7e28
        c2.lum_plus = 3.2e28
        c2.lum_minus = 2.1e28
        ad = self.additional_get_add(p, num=0)
        ad.dist_dm_cl = 0.184
        ad.dist_dm_cl_plus = 0.194 - 0.184
        ad.dist_dm_cl_minus = 0.184 - 0.167
        ad.dist_pi = 0.210
        ad.dist_pi_plus = 0.090
        ad.dist_pi_minus = 0.050
        a2 = self.article_get_add(p, num=1)
        a2.article = 'http://adsabs.harvard.edu/abs/2009ApJ...691..458P'
        a2.cite = '\cite{2009_Pavlov}'
        a2.info = ('page 4, BB, PL (not enought counts for BB+PL) recalculated for distance 0.184')
        a2.dist = 0.184
        f2 = self.fit_get_add(a2, num=0)
        f2.spectrum = 'BB'
        c3 = self.component_get_add(f2, 0)
        c3.spec_type = 'BB'
        c3.r = self.radius_from_area(53e4) * (184./130.)
        c3.r_plus = self.radius_from_area(32e4) * (184./130.)
        c3.r_minus = self.radius_from_area(21e4)* (184./130.)
        c3.t = self.ev_to_k(279)
        c3.t_plus = self.ev_to_k(35)
        c3.t_minus = self.ev_to_k(28)
        c3.lum = self.lbol_radius(c1.t, c1.r)
        f3 = self.fit_get_add(a2, num=1)
        f3.spectrum = 'PL'
        c4 = self.component_get_add(f3, num=0)
        c4.spec_type = 'PL'
        c4.pl = 2.2
        c4.pl_plus = 0.31
        c4.pl_minus = 0.28
        c4.lum = 2.1e28
        c4.lum_plus = 3.8e+28
        self.save_records([a1, a2, f1, f2, f3, c1, c2, c3, c4, ad], p)
        self.calculate(p)

        #     B0628-28     ####################################################
        p = Pulsar.objects.get(name='B0628-28')
        ge = self.geometry_get_add(p, 0)
        ge.alpha = 70.
        ge.beta = -12.
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca = self.calculation_get_add(p, 0)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2005ApJ...630L..57'
        a1.cite = '\cite{2005_Tepedelenl}'
        a1.info = ('page 5, no inf -> surface conversion, looks like A_{\perp}, P3 not mesured')
        a1.dist = 1.45
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 59e2 / ca.f ** 0.5
        c1.r_plus = 65e2 / ca.f ** 0.5
        c1.r_minus = 46e2 / ca.f ** 0.5
        c1.t = 3.28e6
        c1.t_plus = 1.31e6
        c1.t_minus = 0.62e6
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 2.98
        c2.pl_plus = 0.91
        c2.pl_minus = 0.65
        c2.lum = 1.67e30
        c2.lum_plus = 0.91e30
        c2.lum_minus = 0.62e30
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2005ApJ...633..367B'
        a2.cite = '\cite{2005_Becker}'
        a2.info = ('...')
        ad = self.additional_get_add(p, 0)
        ad.dist_dm_cl = 1.444
        ad.dist_dm_cl_plus= 1.444 - 1.167
        ad.dist_dm_cl_minus = 1.709 - 1.444
        ad.articles = 'http://adsabs.harvard.edu/abs/2005ApJ...633..367B'
        su = self.subpulse_get_add(p, 0)
        su.p2 = 30.
        su.p2_plus = 60.
        su.p2_minus = 6.
        su.p3 = 7.
        su.p3_plus = 1.
        su.p3_minus = 1.
        su.p4 = 8.71093017305
        su.article = 'http://adsabs.harvard.edu/abs/2006A%26A...445..243W'
        self.save_records([ge, ca, ad, su, a1, a2, f1, c1, c2], p)
        self.calculate(p)

        #    B0834+06      ####################################################
        p = Pulsar.objects.get(name='B0834+06')
        ge = self.geometry_get_add(p)
        ge.alpha = 60.7
        ge.beta = 4.5
        ge.rho = 7.1
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca = self.calculation_get_add(p)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2008ApJ...686..497G'
        a1.cite = '\cite{2008_Gil}'
        a1.info = ('page 6, no inf -> surface conversion, r_bb calculated from L \eq 4 A \sigma T^4, 1 sigma errors taken, BB(2/3)+PL(1/3) BB+PL fits not included in database (poor statistics..., no l_nonth), A_{\perp}')
        a1.dist = 0.643
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.t = self.ev_to_k(170)
        c1.t_plus = self.ev_to_k(65)
        c1.t_minus = self.ev_to_k(55)
        c1.r = self.radius_from_lt_simple(8.6e28 / 4., c1.t) /ca.f ** 0.5
        c1.r_plus = 5643.465323
        c1.r_minus = 1528.715528
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c1.lum_plus = 1.9e28
        c1.lum_minus = 0.5e28
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        # TODO add Photon Index!!
        #co[0][0][1].pl =
        #co[0][0][1].pl_plus =
        #co[0][0][1].pl_minus =
        c2.lum = c1.lum
        # TODO add lum errors
        #co[0][0][1].lum_plus =
        #co[0][0][1].lum_minus =
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 0.643
        ad.dist_dm_cl_plus = 0.723 - 0.643
        ad.dist_dm_cl_minus = 0.643 - 0.567
        ad.articles = ('http://adsabs.harvard.edu/abs/2006A%26A...445..243W;http://adsabs.harvard.edu/abs/1997MNRAS.288..631K;http://adsabs.harvard.edu/abs/1988MNRAS.234..477L')
        su = self.subpulse_get_add(p)
        su.info = 'other values for p2 and p3 in paper 40deg, 21 P0'
        su.p2 = 20.
        su.p2_plus = 55.
        su.p2_minus = 9.
        su.p3 = 2.2
        su.p3_plus = 0.2
        su.p3_minus = 0.2
        su.p4 = 38.4678024056707
        self.save_records([ge, ca, ad, su, a1, f1, c1, c2], p)
        self.calculate(p)

        #   B0943+10       ####################################################
        p = Pulsar.objects.get(name='B0943+10')
        ge = self.geometry_get_add(p)
        ge.alpha = 11.58
        ge.beta = -4.29
        ge.rho = 4.5
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca = self.calculation_get_add(p)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        a1 = self.article_get_add(p, 0)
        a1.num = 0
        a1.article = 'http://adsabs.harvard.edu/abs/2005ApJ...624L.109Z'
        a1.cite = '\cite{2005_Zhang}'
        a1.info = ('page 2, no inf -> surface conversion, cos(theta)=0.97, (dist=630  was used), A and T errors from graph (T_max 0.36keV T_min 0.175keV A_max 5.8e3 A_min 2.9e2) in paper L_bol for cap (A used as A_{\perp}?)')
        a1.dist = 0.63
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.t = 3.1e6
        c1.t_plus = self.ev_to_k(0.36e3-self.k_to_ev(3.1e6))
        c1.t_minus = self.ev_to_k(self.k_to_ev(3.1e6)-0.175e3)
        c1.r = self.radius_from_lt_simple(4.9e+28 / 2., c1.t) / ca.f ** 0.5
        a_ = pi * c1.r ** 2.
        c1.r_plus = self.radius_from_area(5.8e7 - a_)
        c1.r_minus = self.radius_from_area(a_ - 2.9e6)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c1.lum_plus = 0.6e28 / ca.f
        c1.lum_minus = 1.6e28 / ca.f
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'PL'
        f2.ordinal = 99
        c2 = self.component_get_add(f2, 0)
        c2.spec_type = 'PL'
        c2.pl = 2.6
        c2.pl_plus = 0.7
        c2.pl_minus = 0.5
        c2.lum = 2.4e29
        c2.lum_plus = 0.8e29
        c2.lum_minus = 0.7e29
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2006ApJ...636..406K'
        a2.cite = '\cite{2006_Kargaltsev}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 0.631
        ad.dist_dm_cl_plus = 0.744 - 0.631
        ad.dist_dm_cl_minus = 0.631 - 0.527
        ad.articles = 'http://adsabs.harvard.edu/abs/2001MNRAS.326.1249A;http://adsabs.harvard.edu/abs/2001MNRAS.322..438D'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/2013Sci...339..436H'
        a3.cite = '\cite{2013_Hermsen}'
        a3.info = ('two modes -> data from presentation check article!(radio quiescent mode)')
        a3.dist = 0.63
        # TODO get values from paper
        f3 = self.fit_get_add(a3, 0)
        f3.spectrum = 'BB + PL'
        c3 = self.component_get_add(f3, 0)
        c3.spec_type = 'BB'
        c3.t = self.ev_to_k(0.277e3)
        c3.t_plus = self.ev_to_k(0.012e3)
        c3.t_minus = self.ev_to_k(0.012e3)
        #c3.r =
        #c3.r_plus =
        #c3.r_minus =
        #c3.lum =
        #c3.lum_plus =
        #c3.lum_minus =
        c4 = self.component_get_add(f3, 1)
        c4.spec_type = 'PL'
        c4.pl = 2.6
        c4.pl_plus = 0.34
        c4.pl_minus = 0.34
        #c4.lum =
        #c4.lum_plus =
        #c4.lum_minus =
        f4 = self.fit_get_add(a3, 1)
        f4.spectrum = 'BB'
        c5 = self.component_get_add(f4, 0)
        c5.spec_type = 'BB'
        c5.t = self.ev_to_k(0.250e3)
        c5.t_plus = self.ev_to_k(0.006e3)
        c5.t_minus = self.ev_to_k(0.006e3)
        #c5.r =
        #c5.r_plus =
        #c5.r_minus =
        #c5.lum =
        #c5.lum_plus =
        #c5.lum_minus =
        f5 = self.fit_get_add(a3, 2)
        f5.spectrum = 'PL'
        c6 = self.component_get_add(f5, 0)
        c6.spec_type = 'PL'
        c6.pl = 2.29
        c6.pl_plus = 0.16
        c6.pl_minus = 0.16
        #c6.lum =
        #c6.lum_plus =
        #c6.lum_minus =
        su = self.subpulse_get_add(p)
        su.p2 = 18.
        su.p3 = 2.0285601425812803
        su.article = 'http://adsabs.harvard.edu/abs/1997MNRAS.288..631K'
        su.info = 'P_2 = 10.5[deg] in second paper...'
        self.save_records([ge, ca, ad, su, a1, a2, a3, f1, f2, f3, f4, f5,
                           c1, c2, c3, c4, c5, c6], p)
        self.calculate(p)

        #     B0950+08     ####################################################
        p = Pulsar.objects.get(name='B0950+08')
        ge = self.geometry_get_add(p)
        ge.alpha = 105.4
        ge.beta = 22.1
        #ge.rho = 0. ???
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca = self.calculation_get_add(p)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2004ApJ...616..452Z'
        a1.cite = '\cite{2004_Zavlin}'
        a1.info = ('page 7, PL+BB (good for eff. vs. age)  A_{\perp} (R is in fact R_{\perp}) PL luminosity from Becker 2009 (review) - very small errors in original paper!!')
        a1.dist = 0.262
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(5000, ca.f)
        c1.r_plus = self.radius_from_inf(3200, ca.f)
        c1.r_minus = self.radius_from_inf(3200, ca.f)
        c1.t = 1.75e6 / self.gr
        c1.t_plus = 0.22e6 / self.gr
        c1.t_minus = 0.22e6 / self.gr
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c1.lum_plus = 0.8e29 / self.gr ** 2. / ca.f
        c1.lum_minus = 0.8e29 / self.gr ** 2. / ca.f
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.31
        c2.pl_plus = 0.14
        c2.pl_minus = 0.14
        #c2.lum = 9.7e29
        #c2.lum_plus = 0.1e29
        #c2.lum_minus = 0.1e29
        c2.lum, c2.lum_plus, c2.lum_minus = \
            self.lnonth_powers([[29.80, 0.22, 0.36], [29.61, 0.19, 0.33]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        a2.cite = '\cite{2007_Zavlin}'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/2004ApJ...615..908B'
        a3.cite = '\cite{2004_Becker}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 0.255
        ad.dist_dm_cl_plus = 0.271 - 0.255
        ad.dist_dm_cl_minus = 0.255 - 0.224
        ad.dist_pi = 0.262
        ad.dist_pi_plus = 0.267 - 0.262
        ad.dist_pi_minus = 0.262 - 0.257
        ad.articles = ('http://adsabs.harvard.edu/abs/2007A%26A...469..607W;http://adsabs.harvard.edu/abs/1997MNRAS.288..631K;http://adsabs.harvard.edu/abs/1980A%26A....86....7W')
        su = self.subpulse_get_add(p)
        su.p2 = -500. # ??
        su.p2_plus = 100.
        su.p2_minus = 300.
        su.p3 = 6.5
        su.p3_plus = 2.2
        su.p3_minus = 2.2
        su.article = ''
        self.save_records([ge, ca, ad, su, a1, a2, a3, f1, c1, c2], p)
        self.calculate(p)

        #    B1133+16      ####################################################
        p = Pulsar.objects.get(name='B1133+16')
        ge = self.geometry_get_add(p)
        ge.alpha = 52.5
        ge.beta = 4.5
        ge.rho = 7.4
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca = self.calculation_get_add(p)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        a1 = self.article_get_add(p, 0)
        a1.num = 0
        a1.article = 'http://adsabs.harvard.edu/abs/2006ApJ...636..406K'
        a1.cite = '\cite{2006_Kargaltsev}'
        a1.info = ('page 2/3, PL, BB, no inf -> surface conversion, cos(th.) = 0.47, T is taken from graph (in paper T = 2.8MK), PL and BB separate fits, A_{\perp}')
        a1.dist = 0.357
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB'
        f1.ordinal  = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_area(5e6) / ca.f ** 0.5
        c1.r_plus = self.radius_from_area(3e6) / ca.f ** 0.5
        c1.r_minus = self.radius_from_area(22e5) / ca.f ** 0.5
        c1.t = self.ev_to_k(0.28e3)
        c1.t_plus = self.ev_to_k(0.04e3)
        c1.t_minus = self.ev_to_k(0.03e3)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c1.lum_plus = 0.5e28
        c1.lum_minus = 0.6e28
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'PL'
        f2.ordinal  = 99
        c2 = self.component_get_add(f2, 0)
        c2.spec_type = 'PL'
        c2.pl = 2.51
        c2.pl_plus = 0.36
        c2.pl_minus = 0.33
        c2.lum, c2.lum_plus, c2.lum_minus = \
            self.lnonth_powers([[29.46,0.37,0.60], [28.66,0.29,0.51]])
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 0.333
        ad.dist_dm_cl_plus = 0.363 - 0.333
        ad.dist_dm_cl_minus = 0.333 - 0.304
        ad.dist_pi = 0.357
        ad.dist_pi_plus = 0.370 - 0.350
        ad.dist_pi_minus = 0.350 - 0.330
        ad.articles = ('http://adsabs.harvard.edu/abs/1997MNRAS.288..631K;http://adsabs.harvard.edu/abs/2006A%26A...445..243W;http://adsabs.harvard.edu/abs/1988MNRAS.234..477L')
        su = self.subpulse_get_add(p)
        su.p2 = 130
        su.p2_plus = 55
        su.p2_minus = 90
        su.p3 = 3
        su.p3_plus = 2
        su.p3_minus = 2
        su.info = 'second fit in paper P_2=200, P_3=3'
        self.save_records([ge, ca, ad, su, a1, f1, f2, c1, c2], p)
        self.calculate(p)

        #    B1257+12      ####################################################
        p = Pulsar.objects.get(name='B1257+12')
        p.comment = 'sol'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2007ApJ...664.1072P'
        a1.cite = '\cite{2007_Pavlov}'
        a1.info = ('page 2, 8, PL, BB? recalculated from 500pc to 447pc (l_bol is different), high errors for pi distance (assumed 0.4),a lot of milisecond pulsar data in paper l_bol = L_bol /gr^4?? A_{\perp}')
        a1.dist = 0.447
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB'
        f1.ordinal  = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_area(2.1e3 * 1e4) * (447. / 500.)
        c1.r_plus = self.radius_from_area(1.9e3 * 1e4) * (447. / 500.)
        c1.r_minus = self.radius_from_area(0.9e3 * 1e4) * (447. /500.)
        c1.t = self.ev_to_k(0.215e3)
        c1.t_plus = self.ev_to_k(0.025e3)
        c1.t_minus = self.ev_to_k(0.023e3)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'PL'
        f2.ordinal  = 99
        c2 = self.component_get_add(f2, 0)
        c2.spec_type = 'PL'
        c2.pl = 2.75
        c2.pl_plus = 0.34
        c2.pl_minus = 0.36
        c2.lum = 2.47e29
        c2.lum_plus = 0.5e29
        c2.lum_minus = 0.48e29
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 0.447
        ad.dist_dm_cl_plus= 0.447 - 0.379
        ad.dist_dm_cl_minus = 0.519 - 0.447
        ad.dist_pi = 0.8
        ad.dist_pi_plus = 0.4
        ad.dist_pi_minus = 0.4
        self.save_records([ad, a1, f1, f2, c1, c2], p)
        self.calculate(p)

        #     J1740-5340A  ####################################################
        p = Pulsar.objects.get(name='J1740-5340A')
        p.comment = 'NGC 6397'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2010ApJ...709..241B'
        a1.cite = '\cite{2010_Bogdanov}'
        a1.info = ('page 5, 3, PL + BB , A_{\perp}')
        a1.dist = 2.4
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        # ordinal?
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 0.15e5 * (3.4 / 2.4)
        c1.r_plus = 0.09e5
        c1.r_minus = 0.13e5
        c1.t = self.ev_to_k(0.19e3)
        c1.t_plus = self.ev_to_k(0.09e3)
        c1.t_minus = self.ev_to_k(0.04e3)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.56
        c2.pl_plus = 0.18
        c2.pl_minus = 0.23
        # TODO add nonthermal luminosities
        #c2.lum =
        #c2.lum_plus =
        #c2.lum_minus =
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2002ApJ...581..470G'
        a2.cite = '\cite{2002_Grindlay}'
        self.save_records([a1, a2, f1, c1, c2], p)
        self.calculate(p)

        #   B1929+10       ####################################################
        p = Pulsar.objects.get(name='B1929+10')
        ge = self.geometry_get_add(p)
        ge.alpha = 35.97
        ge.beta = 25.55
        #ge.rho = 0. ??
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca = self.calculation_get_add(p)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2008ApJ...685.1129M'
        a1.cite = '\cite{2008_Misanovic}'
        a1.info = ('page 33,42, PL+BB, inf -> surface conversion done, f=0.897, Different paralax distance!! 0.33 +-0.01 or 0.361+-0.01 (newer paper used), l_bol  =  L_bol / (2 f gr^2) used, l_bol = L_bol / 4 (sphere to spot correction) l_bol = L_bol /gr^4??  A_{\perp} PL luminosity from Becker 2009 (review) (0.1-10keV)')
        a1.dist = 0.361
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(3310, ca.f)
        c1.r_plus = self.radius_from_inf(590, ca.f)
        c1.r_minus = self.radius_from_inf(460, ca.f)
        c1.t = self.ev_to_k(0.30e3) / self.gr
        c1.t_plus = self.ev_to_k(0.02e3) / self.gr
        c1.t_minus = self.ev_to_k(0.03e3) / self.gr
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.73
        c2.pl_plus = 0.46
        c2.pl_minus = 0.66
        #c2.lum = 1.7e30
        #c2.lum_plus =0.15e30
        #c2.lum_minus =0.22e30
        c2.lum, c2.lum_plus, c2.lum_minus = \
            self.lnonth_powers([[31.12, 0.2, 0.33], [30.07, 0.18, 0.33]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2006ApJ...645.1421B'
        a2.cite = '\cite{2006_Becker}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 0.335
        ad.dist_dm_cl_plus = 0.388 - 0.335
        ad.dist_dm_cl_minus = 0.335 - 0.282
        ad.dist_pi = 0.361
        ad.dist_pi_plus = 0.340 - 0.330
        ad.dist_pi_minus = 0.330 - 0.320
        ad.articles = ('http://adsabs.harvard.edu/abs/2006A%26A...445..243W;http://adsabs.harvard.edu/abs/1997MNRAS.288..631K;http://adsabs.harvard.edu/abs/2001ApJ...553..341E')
        su = self.subpulse_get_add(p)
        su.p2 = 90
        su.p2_plus = 140
        su.p2_minus = 8
        su.p3 = 4.4
        su.p3_plus = 0.8
        su.p3_minus = 0.8
        su.article = ''
        self.save_records([ge, ca, ad, su, a1, a2, f1, c1, c2], p)
        self.calculate(p)

        #     J0633+1746   ####################################################
        p = Pulsar.objects.get(name='J0633+1746')
        p.comment = 'Geminga'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2005ApJ...633.1114J'
        a1.cite = '\cite{2005_Jackson}'
        a1.info = ('page 26, PL+BB, no inf -> surface conversion,  Geminga pulsar, NO L_bol, dist_bb etc.!!, L_bol calculated for spot (only hot spot component was used), L_bol_sphere2 is very high!')
        a1.dist = 0.157
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 6200.
        c1.r_plus = 3400.
        c1.r_minus = 3400.
        c1.t = 1.71e6
        c1.t_plus = 0.23e6
        c1.t_minus = 0.23e6
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'BB'
        c2.r = 11.17e5
        c2.r_plus = 1.09e5
        c2.r_minus = 1.09e5
        c2.t = 0.48e6
        c2.t_plus = 0.002e6
        c2.t_minus = 0.002e6
        c2.lum = self.lbol_radius(c2.t, c2.r)
        c3 = self.component_get_add(f1, 2)
        c3.spec_type = 'PL'
        c3.pl = 1.684
        c3.pl_plus = 0.06
        c3.pl_minus = 0.06
        c3.lum, c3.lum_plus, c3.lum_minus = \
            self.lnonth_powers([[29.90,0.2,0.35],[29.98,0.2,0.35]])
        a2 = self.article_get_add(p, 1)
        a2.num = 1
        a2.article = 'http://adsabs.harvard.edu/abs/2005ApJ...625..307K'
        a2.cite = '\cite{2005_Kargaltsev}'
        a2.info = ('page 8, PL+BB, no inf -> surface conversion, Geminga, two component bb fit, R, R+ and R- recalculated for distance (0.157, 0.2 not used)! R_bb (best dist), check PSR_J0633+1746 for newer paper, L_bol calculated for spot (only hot spot component was used), L_bol_sphere is very high!')
        a2.dist = 0.157
        f2 = self.fit_get_add(a2, 0)
        f2.spectrum = 'BB + BB + PL'
        c4 = self.component_get_add(f2, 0)
        c4.spec_type = 'BB'
        c4.r = 4600. * (157./200.)
        c4.r_plus = 1200. * (157./200.)
        c4.r_minus = 1200. * (157./200.)
        c4.t = 2.32e6
        c4.t_plus = 0.08e6
        c4.t_minus = 0.08e6
        c4.lum = self.lbol_radius(c4.t, c4.r)
        c5 = self.component_get_add(f2, 1)
        c5.spec_type = 'BB'
        c5.r = 12.9e5 * (157./200.)
        c5.r_plus = 1e5 * (157./200.)
        c5.r_minus = 1e5 * (157./200.)
        c5.t = 0.49e6
        c5.t_plus = 0.01e6
        c5.t_minus = 0.01e6
        c5.lum = self.lbol_radius(c5.t, c5.r)
        c6 = self.component_get_add(f2, 2)
        c6.spec_type = 'PL'
        c6.pl = 1.56
        c6.pl_plus = 0.24
        c6.pl_minus = 0.24
        c6.lum = 1.3e30
        c6.lum_plus = 0.2e30
        c6.lum_minus = 0.2e30
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 3.907
        ad.dist_dm_cl_plus = 5.573 - 3.907
        ad.dist_dm_cl_minus = 3.907 - 2.795
        ad.dist_pi = 0.157
        ad.dist_pi_plus = 0.059
        ad.dist_pi_minus = 0.034
        ad.articles = ('http://adsabs.harvard.edu/abs/2007astro.ph..2426Z;http://adsabs.harvard.edu/abs/2005ApJ...623.1051D')
        self.save_records([ad, a1, a2, f1, f2, c1, c2, c3, c4, c5, c6], p)
        self.calculate(p)

        #    J0821-4300      ##################################################
        p = Pulsar.objects.get(name='J0821-4300')
        a1 = self.article_get_add(p, 0)
        a1.num = 0
        a1.article = 'http://adsabs.harvard.edu/abs/2010ApJ...724.1316G'
        a1.cite = '\cite{2010_Gotthelf}'
        a1.info = ('page 6, no inf -> surface conversion, 10 km radius taken R = 10*sin(beta), READ WHIOLE PAPER!!!  A_{\perp}')
        a1.dist = 2.2
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + BB'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.r * sin(7./180. * pi)
        c1.r_plus = 0.11 * c1.r
        c1.r_minus = 0.11 * c1.r
        c1.t = self.ev_to_k(0.540e3)
        c1.t_plus = 0.03 * c1.t
        c1.t_minus = 0.03 * c1.t
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'BB'
        c2.r = self.r * sin(37./180. * pi)
        c2.r_plus = 0.06 * c2.r
        c2.r_minus = 0.06 * c2.r
        c2.t = self.ev_to_k(280)
        c2.t_plus = 0.03 * c2.t
        c2.t_minus = 0.03 * c2.t
        c2.lum = self.lbol_radius(c2.t, c2.r)
        ad = self.additional_get_add(p)
        ad.best_age = 3.7e3
        self.save_records([ad, a1, f1, c1, c2], p)
        self.calculate(p)

        #    J0538+2817    ####################################################
        p = Pulsar.objects.get(name='J0538+2817')
        p.comment = 'SNR S147'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2003ApJ...591..380M'
        a1.cite = '\cite{2003_Mcgowan}'
        a1.info = ('age 22 (second fit for best N_H), inf -> surface conversion done, no PL, no equation for L_bol (R_bb) paralax distance taken from the newest paper, no equation -> assumed A_{\perp}')
        a1.dist = 1.2
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(0.87e5)
        c1.r_plus = self.radius_from_inf(0.05e5)
        c1.r_minus = self.radius_from_inf(0.05e5)
        c1.t = 2.12e6 / self.gr
        c1.t_plus = 0.04e6 / self.gr
        c1.t_minus = 0.04e6 / self.gr
        c1.lum = self.lbol_radius(c1.t, c1.r)
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'AT'
        c2 = self.component_get_add(f2, 0)
        c2.spec_type = 'AT'
        c2.t = 1.1e6
        c2.r = 10.5e5
        c2.b_atm = 1e12
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2004MmSAI..75..458Z'
        a2.cite = '\cite{2004_Zavlin}'
        a2.article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        a2.cite = '\cite{2007_Zavlin}'
        ad.dist_dm_cl = 1.206
        ad.dist_dm_cl_plus = 1.438 - 1.206
        ad.dist_dm_cl_minus = 1.206 - 0.972
        ad.dist_pi = 1.30
        ad.dist_pi_plus = 0.22
        ad.dist_pi_minus = 0.16
        ad.best_age = 30e3
        ad.articles = 'http://adsabs.harvard.edu/abs/2009ApJ...698..250C'
        self.save_records([ad, a1, a2, f1, f2, c1, c2], p)
        self.calculate(p)

        #    B0656+14      ####################################################
        p = Pulsar.objects.get(name='B0656+14')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2005ApJ...623.1051D'
        a1.cite = '\cite{2005_Deluca}'
        a1.info = ('page 25, no inf -> surface conversion, two component bb fit, L_bol for spot... A_{\perp} PL lum from Becker 2009 (review) 0.1-10keV')
        a1.dist = 0.288
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 180000
        c1.r_plus = 15000
        c1.r_minus = 15000
        c1.t = 1.25e6
        c1.t_plus = 0.03e6
        c1.t_minus = 0.03e6
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'BB'
        c2.r = 20.9e5
        c2.r_plus = 2.7e5
        c2.r_minus = 3.8e5
        c2.t = 6.5e5
        c2.t_plus = 0.1e5
        c2.t_minus = 0.1e5
        c2.lum = self.lbol_radius(c2.t, c2.r)
        c3 = self.component_get_add(f1, 2)
        c3.spec_type = 'PL'
        c3.pl = 2.1
        c3.pl_plus = 0.3
        c3.pl_minus = 0.3
        # 1.8e30
        c3.lum, c3.lum_plus, c3.lum_minus = \
            self.lnonth_powers([[30.38, 0.35, 0.54], [30.01, 0.26, 0.47]])
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'AT'
        c4 = self.component_get_add(f2, 0)
        c4.spec_type = 'AT'
        c4.t = 0.8e6
        c4.r = 7.5e5
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        a2.cite = '\cite{2007_Zavlin}'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/1996A%26A...313..565P'
        a3.cite = '\cite{1996_Possenti}'
        a4 = self.article_get_add(p, 3)
        a4.article = 'http://adsabs.harvard.edu/abs/2002nsps.conf..273P'
        a4.cite = '\cite{2002_Pavlov}'
        a5 = self.article_get_add(p, 4)
        a5.article = 'http://adsabs.harvard.edu/abs/2002nsps.conf...64B'
        a5.cite = '\cite{2002_Becker}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 0.669
        self.save_records([ad, a1, a2, a3, a4, a5, f1, f2, c1, c2, c3, c4], p)
        self.calculate(p)

        #   B0833-45       ####################################################
        p = Pulsar.objects.get(name='B0833-45')
        p.comment = 'Vela'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        a1.cite = '\cite{2007_Zavlin_b}'
        a1.info = ('page 16 , inf -> surface conversion, Vela, assumed A_{\perp}, last paper (p. 16) PL luminosities from Becker 2009 (review) 0.1-10 keV')
        a1.dist = 0.210
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(2.1e5)
        c1.r_plus = self.radius_from_inf(0.2e5)
        c1.r_minus = self.radius_from_inf(0.2e5)
        c1.t = self.t_from_inf(1.49e6)
        c1.t_plus = self.t_from_inf(0.04e6)
        c1.t_minus = self.t_from_inf(0.04e6)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 2.7
        c2.pl_plus = 0.4
        c2.pl_minus = 0.4
        #c2.lum = 4.2e32
        c2.lum, c2.lum_plus, c2.lum_minus = \
            self.lnonth_powers([[32.81, 0.25, 0.44], [31.79, 0.37, 0.67]])
        # TODO add nonthermal lum errs.
        #c2.lum_plus =
        #c2.lum_minus =
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'AT'
        c3  = self.component_get_add(f2, 0)
        c3.spec_type = 'AT'
        c3.t = 0.68e6
        c3.r = 10e5
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2001ApJ...552L.129P'
        a2.cite = '\cite{2001_Pavlov}'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/2002nsps.conf..273P'
        a3.cite = '\cite{2002_Pavlov}'
        a4 = self.article_get_add(p, 3)
        a4.article = 'http://adsabs.harvard.edu/abs/2007ApJ...669..570M'
        a4.cite = '\cite{2007_Manzali}'
        a4.info = ('page 1,20, (L_bol) no inf -> surface conversion, new paper for Vela (Chandra observations), another good fit in paper, A_{\perp} PL luminosities from Becker 2009 (review) 0.1-10 keV')
        a4.dist = 0.287
        f3 = self.fit_get_add(a4, 0)
        f3.spectrum = 'BB + BB + PL'
        f3.ordinal = 99
        c4 = self.component_get_add(f3, 0)
        c4.spec_type = 'BB'
        c4.r = 0.73e5
        c4.r_plus = 0.09e5
        c4.r_minus = 0.07e5
        c4.t = 2.16e6
        c4.t_plus = 0.06e6
        c4.t_minus = 0.07e6
        c4.lum = self.lbol_radius(c4.t, c4.r)
        c5 = self.component_get_add(f3, 1)
        c5.spec_type = 'BB'
        c5.r = 5.06e5
        c5.r_plus = 0.42e5
        c5.r_minus = 0.28e5
        c5.t = 1.06e6
        c5.t_plus = 0.03e6
        c5.t_minus = 0.03e6
        c5.lum = self.lbol_radius(c5.t, c5.r)
        c6 = self.component_get_add(f3, 2)
        c6.spec_type = 'PL'
        c6.pl = 2.2
        c6.pl_plus = 0.4
        c6.pl_minus = 0.3
        #c6.lum = 5.74e32
        c6.lum, c6.lum_plus, c6.lum_minus = \
            self.lnonth_powers([[32.81, 0.25, 0.44], [31.79, 0.37, 0.67]])
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 0.236
        ad.dist_pi = 0.287
        self.save_records([ad, a1, a2, a3, a4, f1, f2, f3,  c1, c2, c3, c4,
                           c5, c6], p)
        self.calculate(p)

        #    B1055-52      ####################################################
        p = Pulsar.objects.get(name='B1055-52')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2005ApJ...623.1051D'
        a1.cite = '\cite{2005_Deluca}'
        a1.info = ('page 25, no inf -> surface conversion, two component bb fit, no L_bol, diffrent values in second paper?! ... A_{\perp} PL luminositeies from Becker 2009 (review) in 0.1-10keV')
        a1.dist = 0.75
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 46000
        c1.r_plus = 6000
        c1.r_minus = 6000
        c1.t = 1.79e6
        c1.t_plus = 0.06e6
        c1.t_minus = 0.06e6
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'BB'
        c2.r = 12.3e5
        c2.r_plus = 1.5e5
        c2.r_minus = 0.7e5
        c2.t = 7.9e5
        c2.t_plus = 0.3e5
        c2.t_minus = 0.3e5
        c2.lum = self.lbol_radius(c2.t, c2.r)
        c3 = self.component_get_add(f1, 2)
        c3.spec_type = 'PL'
        c3.pl = 1.7
        c3.pl_plus = 0.1
        c3.pl_minus = 0.1
        #c3.lum = 8.1e30
        c3.lum, c3.lum_plus, c3.lum_minus = \
            self.lnonth_powers([[30.70, 0.22, 0.35], [30.72, 0.58, 0.33]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2002nsps.conf..273P'
        a2.cite = '\cite{2002_Pavlov}'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        a3.cite = '\cite{2007_Zavlin}'
        a4 = self.article_get_add(p, 3)
        a4.article = 'http://adsabs.harvard.edu/abs/2002nsps.conf...64B'
        a4.cite = '\cite{2002_Becker}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 0.726
        self.save_records([ad, a1, a2, a3, a4, f1, c1, c2, c3], p)
        self.calculate(p)

        #   J1119-6127     ####################################################
        p = Pulsar.objects.get(name='J1119-6127')
        p.comment = 'G292.2-0.5'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2007Ap%26SS.308...89G'
        a1.cite = '\cite{2007_Gonzalez}'
        a1.info = ('page 3, no inf -> surface conversion, component is pulsing; fixed size in atmospheric fit (1.6kpc distance)')
        a1.dist = 8.4
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(3.4e5)
        c1.r_plus = self.radius_from_inf(1.8e5)
        c1.r_minus = self.radius_from_inf(0.3e5)
        c1.t = self.t_from_inf(2.4e6)
        c1.t_plus = self.t_from_inf(0.3e6)
        c1.t_minus = self.t_from_inf(0.2e6)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.5
        c2.pl_plus = 0.3
        c2.pl_minus = 0.2
        c2.lum =  0.9e33
        c2.lum_plus = 0.5e33
        c2.lum_minus = 0.1e33
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2008ApJ...684..532S'
        a2.cite = '\cite{2008_Safi-Harb}'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        a3.cite = '\cite{2007_Zavlin}'
        a4 = self.article_get_add(p, 3)
        a4.article = 'http://adsabs.harvard.edu/abs/2005ApJ...630..489G'
        a4.cite = '\cite{2005_Gonzalez}'
        self.save_records([a1, a2, a3, a4, f1, c1, c2], p)
        self.calculate(p)

        #    J1210-5226    ####################################################
        p = Pulsar.objects.get(name='J1210-5226')
        p.comment = 'G296.5+10.0'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2002nsps.conf..273P'
        a1.cite = '\cite{2002_Pavlov}'
        a1.info = ('page 10, radio quiet, no inf -> surface conversion, uncertainness in distance evaluation, no radio signal \dot{P} 1e-14 1e-17  A_{\perp}')
        a1.dist = 2.45
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(1.6e5)
        c1.t = self.t_from_inf(2.9e6)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'AT'
        c2 = self.component_get_add(f2, 0)
        c2.spec_type = 'AT'
        c2.r = self.radius_from_inf(11e5)
        c2.t = self.t_from_inf(1.6e6)
        self.save_records([a1, f1, f2, c1, c2], p)
        self.calculate(p)

        #   J1357-6429     ####################################################
        p = Pulsar.objects.get(name='J1357-6429')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2007ApJ...665L.143Z'
        a1.cite = '\cite{2007_Zavlin}'
        a1.info = ('page 3, no inf -> surface conversion, A_{\perp}PL luminosities from Becker 2009 (review) in 0.1-10keV')
        a1.dist = 2.5
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(2.5e5)
        c1.r_plus = self.radius_from_inf(0.5e5)
        c1.r_minus = self.radius_from_inf(0.5e5)
        c1.t = self.t_from_inf(1.7e6)
        c1.t_plus = self.t_from_inf(0.2e6)
        c1.t_minus = self.t_from_inf(0.2e6)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.3
        c2.pl_plus = 0.2
        c2.pl_minus = 0.2
        #c2.lum = 1.4e32
        c2.lum, c2.lum_plus, c2.lum_minus = \
            self.lnonth_powers([[31.66, 0.22, 0.45], [32.03, 0.22, 0.45]])
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'AT'
        c3 = self.component_get_add(f2, 0)
        c3.r = 10e5
        c3.t = 1e6
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2012ApJ...744...81C'
        a2.cite = '\cite{2012_Chang}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 2.5
        self.save_records([ad, a1, a2, f1, f2, c1, c2, c3], p)
        self.calculate(p)

        #   B1706-44       ####################################################
        p = Pulsar.objects.get(name='B1706-44')
        p.comment = 'G343.1-02.3'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2002ApJ...567L.125G'
        a1.cite = '\cite{2002_Gotthelf}'
        a1.info = ('page 5, no inf -> surface conversion, thermal + non-thermal components A_{\perp}')
        a1.dist = 2.5
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(3.6e5)
        c1.r_plus = self.radius_from_inf(0.9e5)
        c1.r_minus = self.radius_from_inf(0.9e5)
        c1.t = self.t_from_inf(1.66e6)
        c1.t_plus = self.t_from_inf(0.17e6)
        c1.t_minus = self.t_from_inf(0.15e6)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 2.0
        c2.pl_plus = 0.5
        c2.pl_minus = 0.5
        c2.lum = 1.45e32
        c2.lum_plus = 0.46e32
        c2.lum_minus = 0.08e32
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'AT'
        c3 = self.component_get_add(f2, 0)
        c3.r = 12e5
        c3.t = 1e6
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        a2.cite = '\cite{2007_Zavlin}'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/2006ApJ...639..377M'
        a3.cite = '\cite{2006_McGowan}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 2.311
        self.save_records([ad, a1, a2, a3, f1, f2, c1, c2, c3], p)
        self.calculate(p)

        #   J1809-1917     ####################################################
        p = Pulsar.objects.get(name='J1809-1917')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2007ApJ...670..655K'
        a1.cite = '\cite{2007_Kargaltsev}'
        a1.info = ('page 5, 7(graph), no inf -> surface conversion, dist_dm_cl from paper A_{\perp}')
        a1.dist = 3.5
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_area(2.84e6*1e4)
        c1.r_plus = self.radius_from_area(2.66e6*1e4)
        c1.r_minus = self.radius_from_area(1.51e6*1e4)
        c1.t = self.ev_to_k(0.17e3)
        c1.t_plus = self.ev_to_k(0.03e3)
        c1.t_minus = self.ev_to_k(0.03e3)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.23
        c2.pl_plus = 0.62
        c2.pl_minus = 0.62
        c2.lum = 0.37e32
        c2.lum_plus = 0.12e32
        c2.lum_minus = 0.1e32
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 3.5
        self.save_records([ad, a1, f1, c1, c2], p)
        self.calculate(p)

        #   B1823-13       ####################################################
        p = Pulsar.objects.get(name='B1823-13')
        p.comment = 'Vela-like'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2008ApJ...675..683P'
        a1.cite = '\cite{2008_Pavlov}'
        a1.info = ('page 13, no inf -> surface conversion, very bad photon statistics, R_BB fixed in fits - larger R_BB fit in paper, A_{\perp} PL luminosities from Becker 2009')
        a1.dist = 4
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_area(20e10)
        # TODO add errors
        #c1.r_plus =
        #c1.r_minus =
        c1.t = self.ev_to_k(139.)
        c1.t_plus = self.ev_to_k(9.)
        c1.t_minus = self.ev_to_k(6.)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.7
        c2.pl_plus = 0.7
        c2.pl_minus = 0.7
        #c2.lum = 0.6e32
        c2.lum, c2.lum_plus, c2.lum_minus = \
            self.lnonth_powers([[31.8, 0.52, 0.73], [31.55, 0.38, 0.62]])
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 3.9
        self.save_records([ad, a1, f1, c1, c2], p)
        self.calculate(p)

        #    B1916+14      ####################################################
        p = Pulsar.objects.get(name='B1916+14')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2009ApJ...704.1321Z'
        a1.cite = '\cite{2009_Zhu}'
        a1.info = ('page 12, BB, no inf -> surface conversion, check table for more pulsars, A_{\perp}')
        a1.dist = 2.1
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 0.8e5
        c1.r_plus = 0.1e5
        c1.r_minus = 0.1e5
        c1.t = self.ev_to_k(0.13e3)
        c1.t_plus = self.ev_to_k(0.01e3)
        c1.t_minus = self.ev_to_k(0.01e3)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'PL'
        f2.ordinal = 99
        c2 = self.component_get_add(f2, 0)
        c2.spec_type = 'PL'
        c2.pl = 3.5
        c2.pl_plus = 1.6
        c2.pl_minus = 0.7
        c2.lum = 1e32
        # TODO add errors
        #c2.lum_plus =
        #c2.lum_minus =
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 2.059
        self.save_records([ad, a1, f1, f2, c1, c2], p)
        self.calculate(p)

        #    J2043+2740    ####################################################
        p = Pulsar.objects.get(name='J2043+2740')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2004ApJ...615..908B'
        a1.cite = '\cite{2004_Becker}'
        a1.info = ('page 27, R_BB fixed in fits - larger R_BB fit in paper, inf -> surface conversion done (see text T_inf), different values in second paper ?, errors from bb fit,  A_{\perp}?')
        a1.dist = 1.8
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(0.467e5)
        c1.r_plus = self.radius_from_inf(0.2e5)
        c1.r_minus = self.radius_from_inf(0.2e5)
        c1.t = self.t_from_inf(self.ev_to_k(0.125e3))
        c1.t_plus = self.t_from_inf(self.ev_to_k(0.03e3))
        c1.t_minus = self.t_from_inf(self.ev_to_k(0.03e3))
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 2.8
        c2.pl_plus = 1
        c2.pl_minus = 0.8
        c2.lum, c2.lum_plus, c2.lum_minus = self.lnonth_powers([[31.40,0.22,0.45],[29.90,0.22,0.45]])
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'AT'
        c3 = self.component_get_add(f2, 0)
        c3.t = 0.6e6
        c3.r = 9.0e5
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        a2.cite = '\cite{2007_Zavlin}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 1.802
        self.save_records([ad, a1, a2, f1, f2, c1, c2, c3], p)
        self.calculate(p)

        #    B2334+61      ####################################################
        p = Pulsar.objects.get(name='B2334+61')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2006ApJ...639..377M'
        a1.cite = '\cite{2006_McGowan}'
        a1.info = ('pag 4,14, inf -> surface conversion done, no pulsation, different values in second paper ? (, R_bb 1.66e5 from text different fit?) A_{\perp}? no data (R_bb) for BB+PL (BB params from text), spectrum dominated by BB PL luminosity overestimated?')
        a1.dist = 3.1
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(1.66e5)
        c1.r_plus = self.radius_from_inf(0.59e5)
        c1.r_minus = self.radius_from_inf(0.39e5)
        c1.t = self.t_from_inf(1.62e6)
        c1.t_plus = self.t_from_inf(0.35e6)
        c1.t_minus = self.t_from_inf(0.58e6)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 2.2
        c2.pl_plus = 3.0
        c2.pl_minus = 1.4
        c2.lum = 3.1e-14 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        c2.lum_plus = 1.3e-14 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        c2.lum_minus = 1.2e-14 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'AT'
        c3 = self.component_get_add(f2, 0)
        c3.spec_type = 'AT'
        c3.t = 0.76e6
        c3.r = 10e5
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2007astro.ph..2426Z'
        a2.cite = '\cite{2007_Zavlin}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 3.131
        self.save_records([ad, a1, a2, f1, f2, c1, c2, c3], p)
        self.calculate(p)

        #    J0205+6449    ####################################################
        p = Pulsar.objects.get(name='J0205+6449')
        p.comment = '3C58'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2004ApJ...616..403S'
        a1.cite = '\cite{2004_Slane}'
        a1.info = ('page 8 (in text), different value in table (page 9) - R_bb set to star radius there, PL from table, redshifted or unredshifted? PL luminositiy from Becker 2009 (review) in 0.1-10keV')
        a1.dist = 3.2
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(10.7e5)
        # TODO add errors
        #c1.r_plus = self.radius_from_inf()
        #c1.r_minus = self.radius_from_inf()
        c1.t = self.t_from_inf(1.3e6)
        #c1.t_plus = self.t_from_inf()
        #c1.t_minus = self.t_from_inf()
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.78
        c2.pl_plus = 0.02
        c2.pl_minus = 0.04
        #c2.lum = 1.02e-12 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        c2.lum, c2.lum_plus, c2.lum_minus = self.lnonth_powers([[32.64, 0.22, 0.45], [32.68, 0.22, 0.45]])
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'AT'
        c3 = self.component_get_add(f2, 0)
        c3.spec_type = 'AT'
        c3.t = 1.08e6
        c3.r = 10e5
        self.save_records([a1, f1, f2, c1, c2, c3], p)
        self.calculate(p)

        #     B0355+54     ####################################################
        p = Pulsar.objects.get(name='B0355+54')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2007Ap%26SS.308..309M'
        a1.cite = '\cite{2007_McGowan}'
        a1.info = ('page (312), inf -> surface conversion done (is it ok?)')
        a1.dist = 1.04
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(0.12e5)
        c1.r_plus = self.radius_from_inf(0.16e5)
        c1.r_minus = self.radius_from_inf(0.07e5)
        c1.t = self.t_from_inf(2.32e6)
        c1.t_plus = self.t_from_inf(1.16e6)
        c1.t_minus = self.t_from_inf(0.81e6)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.
        c2.pl_plus = 0.2
        c2.pl_minus = 0.2
        c2.lum, c2.lum_plus, c2.lum_minus = self.lnonth_powers([[30.21,0.64,0.71],[30.83,0.57,0.33]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/1994ApJ...437..458S'
        a2.cite = '\cite{1994_Slane}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 1.447
        ad.dist_pi = 1.04
        ad.dist_pi_plus = 0.21
        ad.dist_pi_minus = 0.16
        self.save_records([ad, a1, a2, f1, c1, c2], p)
        self.calculate(p)

        #   B0531+21       ####################################################
        p = Pulsar.objects.get(name='B0531+21')
        p.comment = 'Crab'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a1.cite = '\cite{2009_Becker}'
        a1.info = ('page 41 (Becker), (no BB fit, PL dominated)')
        a1.dist = p.dist
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.63
        c1.pl_plus = 0.07
        c1.pl_minus = 0.07
        c1.lum = 8.912509381337513e+35
        c1.lum_plus = 4.5771194445791014e+35
        c1.lum_minus = 3.0240728277815817e+35
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2011ApJ...743..139W'
        a2.cite = '\cite{2011_Weisskopf}'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/2004ApJ...601.1050W'
        a3.cite = '\cite{2004_Weisskopf}'
        a4 = self.article_get_add(p, 3)
        a4.article = 'http://adsabs.harvard.edu/abs/1997A%26A...326..682B'
        a4.cite = '\cite{1997_Becker}'
        a5 = self.article_get_add(p, 4)
        a5.article = 'http://adsabs.harvard.edu/abs/2001A%26A...365L.212W'
        a5.cite = '\cite{2001_Willingale}'
        self.save_records([a1, a2, a3, a4, a5, f1, c1], p)
        self.calculate(p)

        #     B1951+32     ####################################################
        p = Pulsar.objects.get(name='B1951+32')
        p.comment = 'CTB 80'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2005ApJ...628..931L'
        a1.cite = '\cite{2005_Li}'
        a1.info = ('page 3, no inf -> surface conversion done')
        a1.dist = 2.0
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 2.2e5
        c1.r_plus = 1.4e5
        c1.r_minus = 0.8e5
        c1.t = self.ev_to_k(0.13e3)
        c1.t_plus = self.ev_to_k(0.02e3)
        c1.t_minus = self.ev_to_k(0.02e3)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.63
        c2.pl_plus = 0.03
        c2.pl_minus = 0.05
        c2.lum = .5e-12 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        c2.lum_plus = 9.30906e+32
        c2.lum_minus = 1.7687e+32
        ad = self.additional_get_add(p, 0)
        ad.dist_dm_cl = 3.137
        self.save_records([ad, a1, f1, c1, c2], p)
        self.calculate(p)

        #    B1509-58      ####################################################
        p = Pulsar.objects.get(name='B1509-58')
        p.comment = 'Crab-like pulsar'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2001A%26A...375..397C'
        a1.cite = '\cite{2001_Cusumano}'
        a1.info = ('PL only ... check cite order')
        a1.dist = 4.181
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.19
        c1.pl_plus = 0.04
        c1.pl_minus = 0.04
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[34.64,0.19,0.35],[35.12,0.2,0.37]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a2.cite = '\cite{2009_Becker}'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/2006ApJ...640..929D'
        a3.cite = '\cite{2006_DeLaney}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 4.181
        ad.dist_dm_cl_plus= 4.784 - ad.dist_dm_cl
        ad.dist_dm_cl_minus = ad.dist_dm_cl - 3.570
        self.save_records([ad, a1, a2, a3, f1, c1], p)
        self.calculate(p)

        #     J1930+1852   ####################################################
        p = Pulsar.objects.get(name='J1930+1852')
        p.comment = 'Crab-like pulsar'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2007ApJ...663..315L'
        a1.cite = '\cite{2007_Lu}'
        a1.info = ('??')
        a1.dist = 5.
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.2
        c1.pl_plus = 0.2
        c1.pl_minus = 0.2
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[33.42,0.22,0.45],[33.75,0.22,0.45]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2002ApJ...574L..71C'
        a2.cite = '\cite{2002_Camilo}'
        self.save_records([a1, a2, f1, c1], p)
        self.calculate(p)

        #    J1617-5055    ####################################################
        p = Pulsar.objects.get(name='J1617-5055')
        p.comment = 'Crab-like pulsar'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2009ApJ...690..891K'
        a1.cite = '\cite{2009_Kargaltsev}'
        a1.info = ('page (899, table) underestimated errors in Karg paper for PL? PL luminosity from Becker 2009 (review)')
        a1.dist = 6.5
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.14
        c1.pl_plus = 0.06
        c1.pl_minus = 0.06
        #c1.lum = 17.92e33
        #c1.lum_plus = 0.07e33
        #c1.lum_minus = 0.07e33
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[33.85, 0.19, 0.35], [34.23, 0.18, 0.31]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2002nsps.conf...64B'
        a2.cite = '\cite{2002_Becker}'
        a2.info = ('')
        self.save_records([a1, a2, f1, c1], p)
        self.calculate(p)

        #    J1747-2958    ####################################################
        p = Pulsar.objects.get(name='J1747-2958')
        p.comment = 'Mouse'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a1.cite = '\cite{2009_Becker}'
        a1.info = ('PL fit values from Becker paper')
        a1.dist = 5.
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.8
        c1.pl_plus = 0.08
        c1.pl_minus = 0.08
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[33.82,0.26,0.23],[33.75,0.24,0.23]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2004ApJ...616..383G'
        a2.cite = '\cite{2004_Gaensler}'
        a2.info = ('page 8 (BB)')
        f2 = self.fit_get_add(a2, 0)
        f2.spectrum = 'BB'
        #f2.ordinal = 99
        c2 = self.component_get_add(f2, 0)
        c2.spec_type = 'BB'
        # TODO where are BB parameters
        #c2.r =
        #c2.r_plus =
        #c2.r_minus =
        #c2.t =
        #c2.t_plus =
        #c2.t_minus =
        #c2.lum = self.lbol_radius(c2.t, c2.r)
        self.save_records([a1, a2, f1, f2, c1, c2], p)
        self.calculate(p)

        #    J1124-5916    ####################################################
        p = Pulsar.objects.get(name='J1124-5916')
        p.comment = 'Vela-like pulsar'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a1.cite = '\cite{2009_Becker}'
        a1.info = ('PL fit from Becker, only upper limit for BB')
        a1.dist = 6.
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 1)
        c1.spec_type = 'PL'
        c1.pl = 1.6
        c1.pl_plus = 0.1
        c1.pl_minus = 0.1
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[32.54,0.22,0.45],[32.66,0.22,0.45]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2003ApJ...591L.139H'
        a2.cite = '\cite{2003_Hughes}'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/2003ApJ...583L..91G'
        a3.cite = '\cite{2003_Gonzales}'
        self.save_records([a1, a2, a3, f1, c1], p)
        self.calculate(p)

        #   B1046-58       ####################################################
        p = Pulsar.objects.get(name='B1046-58')
        p.comment = 'Vela-like pulsar'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a1.cite = '\cite{2009_Becker}'
        a1.info = ('')
        a1.dist = 2.7
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.7
        c1.pl_plus = 0.4
        c1.pl_minus = 0.2
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[31.73,0.52,0.46],[31.75,0.3,0.43]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2006ApJ...652..569G'
        a2.cite = '\cite{2006_Gonzalez}'
        a2.info = ('')
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 2.714
        ad.dist_dm_cl_plus = 3.060 - ad.dist_dm_cl
        ad.dist_dm_cl_minus = ad.dist_dm_cl - 2.363
        self.save_records([ad, a1, a2, f1, c1], p)
        self.calculate(p)

        #     J1811-1925   ####################################################
        p = Pulsar.objects.get(name='J1811-1925')
        p.comment = 'G11.2-0.3'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a1.cite = '\cite{2009_Becker}'
        a1.info = ('different Gamma and flux in paper, radio quiet')
        a1.dist = 5.
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 0.97
        c1.pl_plus = 0.39
        c1.pl_minus = 0.32
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[33.23,0.29,0.4],[33.88,0.18,0.31]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2003ApJ...588..992R'
        a2.cite = '\cite{2003_Roberts}'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/2004AIPC..714..306R'
        a3.cite = '\cite{2004_Roberts}'
        self.save_records([a1, a2, a3, f1, c1], p)
        self.calculate(p)

        #  J0537-6910      ####################################################
        p = Pulsar.objects.get(name='J0537-6910')
        p.comment = 'N157B, LMC'
        a1 = self.article_get_add(p, 0)
        a1.num = 0
        a1.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a1.cite = '\cite{2009_Becker}'
        a1.dist = 47
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.8
        c1.pl_plus = 0.1
        c1.pl_minus = 0.1
        c1.lum,  c1.lum_plus, c1.lum_minus = self.lnonth_powers([[35.68,0.19,0.34],[35.61,0.2,0.37]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2005A%26A...431..659M'
        a2.cite = '\cite{2005_Mignani}'
        self.save_records([a1, a2, f1, c1], p)
        self.calculate(p)

        #    B1259-63      ####################################################
        p = Pulsar.objects.get(name='B1259-63')
        p.comment = 'Be-star bin'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a1.cite = '\cite{2009_Becker}'
        a1.info = ('PL fit from Becker, binary star -> variable flux')
        a1.dist = 2.
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.69
        c1.pl_plus = 0.04
        c1.pl_minus = 0.04
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[32.55,0.25,0.54], [32.58,0.39,0.51]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2009MNRAS.397.2123C'
        a2.cite = '\cite{2009_Chernyakova}'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/2006MNRAS.367.1201C'
        a3.cite = '\cite{2006_Chernyakova}'
        self.save_records([a1, a2, a3, f1, c1], p)
        self.calculate(p)

        #    J1420-6048    ####################################################
        p = Pulsar.objects.get(name='J1420-6048')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a1.cite = '\cite{2009_Becker}'
        a1.info = ('PL fit from Becker, some evidence for thermal emission')
        a1.dist = 8.
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.6
        c1.pl_plus = 0.04
        c1.pl_minus = 0.04
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[34.41,0.22,0.45], [34.52,0.22,0.45]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2001ApJ...561L.187R'
        a2.cite = '\cite{2001_Roberts}'
        self.save_records([a1, a2, f1, c1], p)
        self.calculate(p)

        #   B1800-21       ####################################################
        p = Pulsar.objects.get(name='B1800-21')
        p.comment = 'Vela-like pulsar'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2007ApJ...660.1413K'
        a1.cite = '\cite{2007_Kargaltsev}'
        a1.info = ('page 1, no R_BB (strong interstellar absorption) PL '
                   'luminosity from Becker 2009 (review) in 0.1-10keV')
        a1.dist = 4.
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        # TODO where is radius!!?
        #c1.r =
        #c1.r_plus =
        #c1.r_minus =
        c1.t = self.ev_to_k(0.2e3)
        c1.t_plus = self.ev_to_k(0.1e3)
        c1.t_minus = self.ev_to_k(0.1e3)
        #c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.4
        c2.pl_plus = 0.6
        c2.pl_minus = 0.6
        #c2.lum = 4e31
        c2.lum, c2.lum_plus, c2.lum_minus = self.lnonth_powers([[32.35, 0.49, 0.8], [32.64, 0.26, 0.53]])
        self.save_records([a1, f1, c1, c2], p)
        self.calculate(p)

        #   B1757-24       ####################################################
        p = Pulsar.objects.get(name='B1757-24')
        p.comment = 'Duck'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2001ApJ...562L.163K'
        a1.cite = '\cite{2001_Kaspi}'
        a1.info = ('page 9, thermal fit T=1e8')
        a1.dist = 5
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.6
        c1.pl_plus = 0.6
        c1.pl_minus = 0.5
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[33.1,0.54,0.53], [33.21,0.26,0.53]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a2.cite = '\cite{2009_Becker}'
        self.save_records([a1, a2, f1, c1], p)
        self.calculate(p)

        #    B0540-69      ####################################################
        p = Pulsar.objects.get(name='B0540-69')
        p.comment = 'N158A, LMC'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2001ApJ...546.1159K'
        a1.cite = '\cite{2001_Kaaret}'
        a1.info = ('page 7,')
        a1.dist = 55.
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.92
        c1.pl_plus = 0.11
        c1.pl_minus = 0.11
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[36.68,0.19,0.32], [36.49,0.21,0.37]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2008MNRAS.389..691C'
        a2.cite = '\cite{2008_Campana}'
        self.save_records([a1, a2, f1, c1], p)
        self.calculate(p)

        #   J1105-6107     ####################################################
        p = Pulsar.objects.get(name='J1105-6107')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/1998ApJ...497L..29G'
        a1.cite = '\cite{1998_Gotthelf}'
        a1.info = ('page 1, L from Becker')
        a1.dist = 7.
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.8
        c1.pl_plus = 0.4
        c1.pl_minus = 0.4
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[33.65,0.39,0.50], [33.57,0.18,0.31]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a2.cite = '\cite{2009_Becker}'
        self.save_records([a1, a2, f1, c1], p)
        self.calculate(p)

        #   B1853+01     ######################################################
        p = Pulsar.objects.get(name='B1853+01')
        p.comment = 'W44'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2002ApJ...579..404P'
        a1.cite = '\cite{2002_Petre}'
        a1.info = ('page 6, L from Becker ')
        a1.dist = 2.6
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.28
        c1.pl_plus = 0.48
        c1.pl_minus = 0.48
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[31.53,0.44,0.54], [31.92,0.19,0.34]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a2.cite = '\cite{2009_Becker}'
        self.save_records([a1, a2, f1, c1], p)
        self.calculate(p)

        #   J1509-5850     ####################################################
        p = Pulsar.objects.get(name='J1509-5850')
        p.comment = 'MSH 15-52'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2007A%26A...470..965H'
        a1.cite = '\cite{2007_Hui}'
        a1.info = ('page 2, L from Becker BB fit t=1e7, r=10m ')
        a1.dist = 2.56
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.
        c1.pl_plus = 0.2
        c1.pl_minus = 0.3
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[31.43,0.2,0.4], [31.55,0.35,0.54]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a2.cite = '\cite{2009_Becker}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 2.56
        self.save_records([ad, a1, a2, f1, c1], p)
        self.calculate(p)

        #    J2021+3651    ####################################################
        p = Pulsar.objects.get(name='J2021+3651')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2008ApJ...680.1417V'
        a1.cite = '\cite{2008_VanEtten}'
        a1.info = ('page 10, page 9 (in second paper)  remove from B/T plot, The distance to PSR J2021+3651 is intriguing , L from Becker BB ')
        a1.dist = 10.
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 7.0e5
        c1.r_plus = 4e5
        c1.r_minus = 1.7e5
        c1.t = self.t_from_inf(self.ev_to_k(0.16e3))
        c1.t_plus = self.t_from_inf(self.ev_to_k(0.02e3))
        c1.t_minus = self.t_from_inf(self.ev_to_k(0.02e3))
        c1.lum = self.lbol_radius(c1.t, c1.r)
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'PL'
        f2.ordinal = 99
        c2 = self.component_get_add(f2, 0)
        c2.spec_type = 'PL'
        c2.pl = 1.7
        c2.pl_plus = 0.3
        c2.pl_minus = 0.2
        c2.lum, c2.lum_plus, c2.lum_minus = self.lnonth_powers([[34.13,0.23,0.56], [33.97,0.18,0.33]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2004ApJ...612..389H'
        a2.cite = '\cite{2004_Hessels}'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a3.cite = '\cite{2009_Becker}'
        ad = self.additional_get_add(p)
        ad.articles = 'http://adsabs.harvard.edu/abs/2009ApJ...700.1059A'
        self.save_records([ad, a1, a2, a3, f1, f2, c1, c2], p)
        self.calculate(p)

        #      B1610-50    ####################################################
        p = Pulsar.objects.get(name='B1610-50')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2000ApJ...528..436P'
        a1.cite = '\cite{2000_Pivovaroff}'
        a1.info = ('X-ray emission from PSR B1610-50 is not detected ?? upper limits in Becker')
        a1.dist = 7.3
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a2.cite = '\cite{2009_Becker}'
        self.save_records([a1, a2], p)
        self.calculate(p)

        #   J1846-0258     ####################################################
        p = Pulsar.objects.get(name='J1846-0258')
        p.comment = 'Kes 75'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2008ApJ...686..508N'
        a1.cite = '\cite{2008_Ng}'
        a1.info = ('page 14 ')
        a1.dist = 6.
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(0.4e5)
        c1.r_plus = self.radius_from_inf(0.2e5)
        c1.r_minus = self.radius_from_inf(0.2e5)
        c1.t = self.t_from_inf(self.ev_to_k(0.9e3))
        c1.t_plus = self.t_from_inf(self.ev_to_k(0.2e3))
        c1.t_minus = self.t_from_inf(self.ev_to_k(0.2e3))
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.9
        c2.pl_plus = 0.1
        c2.pl_minus = 0.1
        c2.lum = 3.1e-11 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        c2.lum_plus = 0.6e-11 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        c2.lum_minus = 0.6e-11 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2003ApJ...582..783H'
        a2.cite = '\cite{2003_Helfand}'
        self.save_records([a1, a2, f1, c1, c2], p)
        self.calculate(p)

        #     B1719-37     ####################################################
        p = Pulsar.objects.get(name='B1719-37')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2004NuPhS.132..636O'
        a1.cite = '\cite{2004_Oosterbroek}'
        a1.info = ('page 3 (638), same fit in Beckers paper')
        a1.dist = 1.84
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = self.radius_from_inf(0.31e5)
        c1.r_plus = self.radius_from_inf(0.51e5)
        c1.r_minus = self.radius_from_inf(0.16e5)
        c1.t = self.t_from_inf(2.7e6)
        c1.t_plus = self.t_from_inf(0.7e6)
        c1.t_minus = self.t_from_inf(0.58e6)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a2.cite = '\cite{2009_Becker}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 1.835
        ad.dist_dm_cl_plus = 1.835 - 1.564
        ad.dist_dm_cl_minus = 2.132 - 1.835
        self.save_records([ad, a1, a2, f1, c1], p)
        self.calculate(p)

        #     J0631+1036   ####################################################
        p = Pulsar.objects.get(name='J0631+1036')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2002astro.ph..2055K'
        a1.cite = '\cite{2002_Kennea}'
        a1.info = ('no X-ray radiation (different source in first paper)')
        a1.dist = 6.56
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2001ApJ...551L.151T'
        a2.cite = '\cite{2001_Torii}'
        self.save_records([a1, a2], p)
        self.calculate(p)

        #    B0823+26      ####################################################
        p = Pulsar.objects.get(name='B0823+26')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2009ASSL..357...91B'
        a1.cite = '\cite{2009_Becker}'
        a1.info = ('')
        a1.dist = 0.34
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'PL'
        c1.pl = 1.58
        c1.pl_plus = 0.43
        c1.pl_minus = 0.33
        c1.lum, c1.lum_plus, c1.lum_minus = self.lnonth_powers([[29.36,0.69,0.56], [28.56,0.26,0.73]])
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2004ApJ...615..908B'
        a2.cite = '\cite{2004_Becker}'
        self.save_records([a1, a2, f1, c1], p)
        self.calculate(p)

        #    B2224+65      ####################################################
        p = Pulsar.objects.get(name='B2224+65')
        p.comment = 'Guitar'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2012ApJ...747...74H'
        a1.cite = '\cite{2012_Hui}'
        a1.info = ('page 4 (BB), page 19 (PL)')
        a1.dist = 2.
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 1.41e3 * 2.
        c1.r_plus = 2.8e2 * 2.
        c1.r_minus = 1.8e+03
        c1.t = self.ev_to_k(0.5e3)
        c1.t_plus = self.ev_to_k(0.1e3)
        c1.t_minus = self.ev_to_k(0.1e3)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'PL'
        f2.ordinal = 99
        c2 = self.component_get_add(f2, 0)
        c2.spec_type = 'PL'
        c2.pl = 2.2
        c2.pl_plus = 0.2
        c2.pl_minus = 0.3
        c2.lum = 3.4e-14 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        c2.lum_plus = 1.7e-14 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        c2.lum_minus = 1e-14 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2007A%26A...467.1209H'
        a2.cite = '\cite{2007_Hui_b}'
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 2.
        ad.dist_dm_cl_plus = 1.
        ad.dist_dm_cl_minus = 1.
        self.save_records([ad, a1, a2, f1, f2, c1, c2], p)
        self.calculate(p)

        #      B1451-68    ####################################################
        p = Pulsar.objects.get(name='B1451-68')
        ge = self.geometry_get_add(p)
        ge.article = 'http://adsabs.harvard.edu/abs/1993ApJS...85..145R'
        ge.alpha = 37
        ge.beta = -6.
        ge.rho = 10.9
        hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        ca = self.calculation_get_add(p)
        ca.f = hot_spot.f()
        ca.cos_i = hot_spot.c()
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2012ApJ...749..146P'
        a1.cite = '\cite{2012_Posselt}'
        a1.info = ('page 6')
        a1.dist = 0.48
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 13.8e2
        c1.r_plus = 24.2e2
        c1.r_minus = 12.3e2
        c1.t = self.ev_to_k(0.35e3)
        c1.t_plus = self.ev_to_k(0.12e3)
        c1.t_minus = self.ev_to_k(0.07e3)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.4
        c2.pl_plus = 0.5
        c2.pl_minus = 0.5
        c2.lum = 5.9e29
        c2.lum_plus = 4.9e29
        c2.lum_minus = 5e29
        ad = self.additional_get_add(p)
        ad.dist_dm_cl = 0.459
        ad.dist_dm_cl_plus = 0.403 - 0.459
        ad.dist_dm_cl_minus = 0.459 - 0.415
        ad.dist_pi = 0.48
        ad.dist_pi_plus = 0.08
        ad.dist_pi_minus = 0.06
        self.save_records([ge, ca, ad, a1, f1, c1, c2], p)
        self.calculate(p)

        #    J0437-4715    ####################################################
        p = Pulsar.objects.get(name='J0437-4715')
        ge = self.geometry_get_add(p)
        ge.alpha = 36.
        #ge.beta =
        #ge.rho =
        #hot_spot = HotSpots(ge.alpha / 180. * pi, ge.beta / 180. * pi)
        #ca.f = hot_spot.f()
        #ca.cos_i = hot_spot.c()
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2013ApJ...762...96B'
        a1.cite = '\cite{2013_Bogdanov}'
        a1.info = ('page 6, many other fits in paper')
        a1.dist = 0.1563
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 0.07e5
        c1.r_plus = 0.02e5
        c1.r_minus = 0.02e5
        c1.t = 2.9e6
        c1.t_plus = 0.05e6
        c1.t_minus = 0.06e6
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 0)
        c2.spec_type = 'PL'
        c2.pl = -0.11
        c2.pl_plus = 1.67
        c2.pl_minus = 1.74
        # TODO add nonthermal luminosities
        #c2.lum =
        #c2.lum_plus =
        #c2.lum_minus =
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'BB + ??'
        c3 = self.component_get_add(f2, 0)
        c3.spec_type = 'BB'
        c3.r = 0.39e5
        c3.r_plus = 0.17e5
        c3.r_minus = 0.14e5
        c3.t = 1.23e6
        c3.t_plus = 0.05e6
        c3.t_minus = 0.06e6
        c3.lum = self.lbol_radius(c3.t, c3.r)
        ad = self.additional_get_add(p)
        ad.dist_pi = 0.1563
        ad.dist_pi_plus = 0.0013
        ad.dist_pi_minus = 0.0013
        self.save_records([ge, ad, a1, f1, f2, c1, c2, c3], p)
        self.calculate(p)

        #    J2021+4026    ####################################################
        p = Pulsar.objects.get(name='J2021+4026')
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://arxiv.org/abs/1305.0998'
        a1.cite = '\cite{2013_Lin}'
        a1.info = ('page 6, BB+PL, BB + BB (sec BB is incorrect?), BB + PL')
        a1.dist = 1.5
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 251e2
        c1.r_plus = 537e2
        c1.r_minus = 132e2
        c1.t = self.ev_to_k(0.24e3)
        c1.t_plus = self.ev_to_k(0.06e3)
        c1.t_minus = self.ev_to_k(0.06e3)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.2
        c2.pl_plus = 1.7
        c2.pl_minus = 1.2
        c2.lum = 0.5e-13 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        # TODO no luminosities?
        #c2.lum_plus =
        #c2.lum_minus =
        f2 = self.fit_get_add(a1, 1)
        f2.spectrum = 'BB + BB?'
        c3 = self.component_get_add(f2, 0)
        c3.spec_type = 'BB'
        c3.r = 223e2
        c3.r_plus = 320e2
        c3.r_minus = 106e2
        c3.t = self.ev_to_k(0.25e3)
        c3.t_plus = self.ev_to_k(0.05e3)
        c3.t_minus = self.ev_to_k(0.05e3)
        c3.lum = self.lbol_radius(c3.t, c3.r)
        c4 = self.component_get_add(f2, 1)
        c4.spec_type = 'BB'
        c4.r = 3.6e2
        c4.r_plus = 6.4e2
        c4.r_minus = 2.5e2
        c4.t = self.ev_to_k(1.4e3)
        c4.t_plus = self.ev_to_k(1.8e3)
        c4.t_minus = self.ev_to_k(0.6e3)
        c4.lum = self.lbol_radius(c4.t, c4.r)
        f3 = self.fit_get_add(a1, 2)
        f3.spectrum = 'PL'
        c5 = self.component_get_add(f3, 0)
        c5.spec_type = 'PL'
        c5.pl = 1.2
        c5.pl_plus = 1.7
        c5.pl_minus = 1.2
        # TODO add nonthermal luminosities
        #c5.lum =
        #c5.lum_plus =
        #c5.lum_minus =
        self.save_records([a1, f1, f2, f3, c1, c2, c3, c4, c5], p)
        self.calculate(p)

        #    J0007+7303    ####################################################
        p = Pulsar.objects.get(name='J0007+7303')
        p.comment = 'CTA 1'
        a1 = self.article_get_add(p, 0)
        a1.article = 'http://adsabs.harvard.edu/abs/2010ApJ...725L...1L'
        a1.cite = '\cite{2010_Lin}'
        a1.info = ('page 4,')
        a1.dist = 1.4
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r = 1.39e5
        c1.r_plus = 0.68e5
        c1.r_minus = 0.43e5
        c1.t = self.ev_to_k(0.104e3)
        c1.t_plus = self.ev_to_k(0.013e3)
        c1.t_minus = self.ev_to_k(0.013e3)
        c1.lum = self.lbol_radius(c1.t, c1.r)
        #print c1.lum, 3.3e-14 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl = 1.52
        c2.pl_plus = 0.1
        c2.pl_minus = 0.09
        #c2.lum = 1.6e-13 * 4. * pi * (a1.dist * 1e3 * 3.0857e18) ** 2.
        # TODO add luminosity errors
        #c2.lum_plus =
        #c2.lum_minus =
        a2 = self.article_get_add(p, 1)
        a2.article = 'http://adsabs.harvard.edu/abs/2010ApJ...725L...6C'
        a2.cite = '\cite{2010_Caraveo}'
        a2.info = 'page 19'
        a3 = self.article_get_add(p, 2)
        a3.article = 'http://adsabs.harvard.edu/abs/2007ApJ...668.1154H'
        a3.cite = '\cite{2007_Halpern}'
        self.save_records([a1, a2, a3, f1, c1, c2], p)
        self.calculate(p)

        '''
        #        ####################################################
        p = Pulsar.objects.get(name='')
        a1 = self.article_get_add(p, 0)
        a1.article = ''
        a1.cite = '\cite{}'
        a1.info = ('')
        a1.dist =
        f1 = self.fit_get_add(a1, 0)
        f1.spectrum = 'BB + PL'
        f1.ordinal = 99
        c1 = self.component_get_add(f1, 0)
        c1.spec_type = 'BB'
        c1.r =
        c1.r_plus =
        c1.r_minus =
        c1.t = self.ev_to_k()
        c1.t_plus = self.ev_to_k()
        c1.t_minus = self.ev_to_k()
        c1.lum = self.lbol_radius(c1.t, c1.r)
        c2 = self.component_get_add(f1, 1)
        c2.spec_type = 'PL'
        c2.pl =
        c2.pl_plus =
        c2.pl_minus =
        c2.lum =
        c2.lum_plus =
        c2.lum_minus =
        self.save_records([a1, f1, c1, c2], p)
        self.calculate(p)
        '''


    def article_get_add(self, p,  num):
        try:
            a = p.xray_articles.get(num=num)
        except ObjectDoesNotExist:
            a = XrayArticle(num=num)
        a.save()
        p.xray_articles.add(a)
        return a

    def fit_get_add(self, a, num):
        try:
            f = a.fits.get(num=num)
        except ObjectDoesNotExist:
            f = XrayFit(num=num)
        f.save()
        a.fits.add(f)
        return f

    def component_get_add(self, f, num):
        try:
            c = f.components.get(num=num)
        except ObjectDoesNotExist:
            c = XrayComponent(num=num)
        c.save()
        f.components.add(c)
        return c

    def additional_get_add(self, p,  num=0):
        try:
            a = p.additionals.get(num=num)
        except ObjectDoesNotExist:
            a = Additional(num=num)
        a.save()
        p.additionals.add(a)
        return a

    def geometry_get_add(self, p,  num=0):
        try:
            g = p.geometries.get(num=num)
        except ObjectDoesNotExist:
            g = Geometry(num=num)
        g.save()
        p.geometries.add(g)
        return g

    def subpulse_get_add(self, p,  num=0):
        try:
            s = p.subpulses.get(num=num)
        except ObjectDoesNotExist:
            s = Subpulse(num=num)
        s.save()
        p.subpulses.add(s)
        return s

    def calculation_get_add(self, p, num=0):
        try:
            c = p.calculations.get(num=num)
        except ObjectDoesNotExist:
            c = Calculation(num=num)
        c.save()
        p.calculations.add(c)
        return c


    def sort_ordinals(self):

        fits = XrayFit.objects.filter(ordinal__gte=0,).filter(psr_id__p0__gt=0.01).order_by('psr_id__rajd')
        ord = 1
        # why I need to use res?!
        res = fits[0]
        res.ordinal = 1
        res.save()
        for i in xrange(1, len(fits)):
            if (fits[i-1].psr_id.name != fits[i].psr_id.name):
                ord += 1
                fits[i].ordinal = ord
            else:
                fits[i].ordinal = ord
            fits[i].save()
            #print fits[i].psr_id.name, ord, fits[i].id

    def save_records(self, list_, p):
        for l in list_:
            l.psr_id = p
            l.save()
        p.save()

    def remove_all(self):
        ca = Calculation.objects.all()
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
        su = Subpulse.objects.all()
        for s in su:
            s.delete()
        xa = XrayArticle.objects.all()
        for x in xa:
            x.delete()

    def calculate(self, p, num=0):

        ca = self.calculation_get_add(p, num=num)

        ca.dotp_15 = p.p1 / 1e-15
        ca.a_dp = 6.58429132402614e8 / float(p.p0)
        ca.r_dp = (ca.a_dp / pi ) ** 0.5
        ca.bsurf2 = 2.02 * 1e12 * float(p.p0) ** 0.5 * ca.dotp_15 ** 0.5
        ca.b_14dp = ca.bsurf2 / 1e14
        ca.l_sd = 3.94784176043574e31 * ca.dotp_15 / float(p.p0) ** 3.

        # first BB component with ordinal >= 0
        skip = False
        co = None
        articles = p.xray_articles.all()#filter(ordinal__gt=0)
        for a in articles:
            fits = a.fits.filter(ordinal__gt=0)
            for f in fits:
                components = f.components.filter(spec_type='BB').order_by('r')
                if len(components) > 0:
                    co = components[0]
                    skip = True
                    break
            if skip is True:
                break
        if co is not None and co.r is not None:
            ca.a = pi * co.r ** 2.
            ca.b = ca.a_dp / ca.a
            ca.b_14 = ca.b * ca.b_14dp
            try:
                r_min = co.r - co.r_minus
                a_min = pi * r_min ** 2.
                b_max = ca.a_dp / a_min
                ca.b_14_plus = (b_max - ca.b) * ca.b_14dp
            except TypeError:
                print 'Warning no r_minus..'
            try:
                r_max = co.r + co.r_plus
                a_max = pi * r_max ** 2.
                b_min = ca.a_dp / a_max
                ca.b_14_minus = (ca.b - b_min) * ca.b_14dp
            except TypeError:
                print 'Warning no r_plus..'
        else:
            print 'Warning no BB component ...'

        ad = self.additional_get_add(p, 0)
        if ad.best_age is None:
            ad.best_age = p.age
        ad.save()
        ca.save()

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
    #p.remove_all()
    p.add_pulsars()
    p.sort_ordinals()
    print 'Bye'


if __name__ == '__main__':
    main()
