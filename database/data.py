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
from database.const.const import CGS as c


class Pulsars:

    def __init__(self):
        pass

    def add_pulsars(self):

        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='J0108-1431', additional=True,
                                calculations=True, articles_num=1,
                                fits_num=[1], components_num=[[2]])
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2012ApJ...761..117P'
        ar[0].cite = '\cite{2012_Posselt}'
        ar[0].info = ('page 4, 5(lum) BB + PL (51 counts) no inf -> surface '
                      'conversion, '
                      'second BB fit taken (0.73 c. d.), A_{\perp} here '
                      '[last update: 2013-05-15]')
        ar[0].dist = 0.210
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = 43e2
        co[0][0][0].r_plus = 24e2
        co[0][0][0].r_minus = 14e2
        co[0][0][0].t = self.ev_to_k(0.11e3)
        co[0][0][0].t_plus = self.ev_to_k(0.03e3)
        co[0][0][0].t_minus = self.ev_to_k(0.01e3)
        # from BB fit (assuming distance)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 3.1
        co[0][0][1].pl_plus = 0.5
        co[0][0][1].pl_minus = 0.2
        co[0][0][1].lum = 3.7e28
        co[0][0][1].lum_plus = 3.2e28
        co[0][0][1].lum_minus = 2.1e28
        ad.dist_dm_cl = 0.184
        ad.dist_dm_plus = 0.194 - 0.184
        ad.dist_dm_minus = 0.184 - 0.167
        ad.dist_pi = 0.210
        ad.dist_pi_plus = 0.090
        ad.dist_pi_minus = 0.050
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)

        pu, ad, ge, su, ca, ar, fi, co = \
            self.create_records(name='B0628-28', additional=True,
                                calculations=True, articles_num=2,
                                fits_num=[2, 2], components_num=[[2, 1], [2, 2]])
        ar[0].num = 0
        ar[0].article = 'http://adsabs.harvard.edu/abs/2005ApJ...630L..57'
        ar[0].cite = '\cite{2005_Tepedelenl}'
        ar[0].info = ('page 5, no inf -> surface conversion, looks like '
                      'A_{\perp}, P3 not mesured [last update: 2013-05-15]')
        ar[0].dist = 1.45
        fi[0][0].spectrum = 'BB + PL'
        co[0][0][0].spec_type = 'BB'
        co[0][0][0].r = 59e2
        co[0][0][0].r_plus = 65e2
        co[0][0][0].r_minus = 46e2
        co[0][0][0].t = 3.28e6
        co[0][0][0].t_plus = 1.31e6
        co[0][0][0].t_minus = 0.62e6
        # from BB fit (assuming distance)
        co[0][0][0].lum = self.lbol_radius(co[0][0][0].t, co[0][0][0].r)
        co[0][0][1].spec_type = 'PL'
        co[0][0][1].pl = 2.98
        co[0][0][1].pl_plus = 0.91
        co[0][0][1].pl_minus = 0.65
        co[0][0][1].lum = 1.67e30
        co[0][0][1].lum_plus = 0.91e30
        co[0][0][1].lum_minus = 0.62e30
        fi[0][1].spectrum = 'PL'
        co[0][1][0].spec_type = 'PL'
        ar[1].num = 1
        ar[1].article = 'http://adsabs.harvard.edu/abs/2005ApJ...633..367B'
        ar[1].cite = '\cite{2005_Becker}'
        ar[1].info = ('...')
        fi[1][0].spectrum = '??'
        co[1][0][0].spec_type = 'BB'
        co[1][0][1].spec_type = 'PL'
        fi[1][1].spectrum = '?? 2'
        co[1][1][0].spec_type = 'BB'
        co[1][1][1].spec_type = 'PL'
        ad.dist_dm_cl = 1.444
        ad.dist_dm_plus = 1.444 - 1.167
        ad.dist_dm_minus = 1.709 - 1.444
        self.save_records(pu, ad, ge, su, ca, ar, fi, co)


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
                c0 = Calculations.objects.get(psr_id=p0)
            except ObjectDoesNotExist:
                c0 = Calculations(psr_id=p0)
        else:
            c0 = None

        articles = []
        fits = []
        components = []

        for i in xrange(articles_num):
            try:
                x0 = XrayArticle.objects.get(psr_id=p0, num=i)
            except ObjectDoesNotExist:
                x0 = XrayArticle(psr_id=p0, num=i)
            articles.append(x0)
            fits.append([])
            components.append([])
            for j in xrange(fits_num[i]):
                try:
                    f0 = XrayFit.objects.get(article_id=x0, num=j)
                except ObjectDoesNotExist:
                    f0 = XrayFit(article_id=x0, num=j)
                fits[-1].append(f0)
                components[-1].append([])
                for k in xrange(components_num[i][j]):
                    try:
                        c0 = XrayComponent.objects.get(fit_id=f0, num=k)
                    except ObjectDoesNotExist:
                        c0 = XrayComponent(fit_id=f0, num=k)
                    components[-1][-1].append(c0)
                    print i, j, k

        return p0, a0, g0, s0, c0, articles, fits, components

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
                print 'article saved %d' % i
            for j, f in enumerate(fi[i]):
                if f is not None:
                    f.save()
                    print 'fit saved %d' % j
                for k, c in enumerate(co[i][j]):
                    if c is not None:
                        c.save()
                        print 'component saved %d' % k

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
    print 'Bye'


if __name__ == '__main__':
    main()
