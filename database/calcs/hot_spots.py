#! /usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
from math import sin, cos, acos, pi, fabs, tan

from numpy import linspace, zeros
from scipy.integrate import quad

# works only when imported from main app
from database.calcs.const.const import CGS as c
###############################################################################


class HotSpots:

    def __init__(self, alpha=0.1, beta=0.1, size=1e3):
        self.alpha = alpha
        self.beta = beta
        self.m = 1.4 *1.98892e33
        self.r_g = 2. * c.G * self.m / c.c**2.
        self.r = 1e6
        self.size = int(size)

    def lim_minus(self):
        #return pi - acos(cos(self.alpha+self.beta)*cos(self.alpha) /
        #                (sin(self.alpha+self.beta)*sin(self.alpha)))
        return pi - acos(1. / (tan(self.alpha+self.beta) * tan(self.alpha)))


    def lim_plus(self):
        #return pi + acos(cos(self.alpha+self.beta)*cos(self.alpha) /
        #                (sin(self.alpha+self.beta)*sin(self.alpha)))
        return pi + acos(1. / (tan(self.alpha+self.beta) * tan(self.alpha)))

    def primary_angle(self, x):
        return acos(sin(self.alpha)*cos(x)*sin(self.alpha+self.beta) +
                    cos(self.alpha)*cos(self.alpha+self.beta))

    def antipodal_angle(self, x):
        return acos(-sin(self.alpha)*cos(x)*sin(self.alpha+self.beta) -
                    cos(self.alpha)* cos(self.alpha+self.beta))

    def primary_cos(self, x):
        return (sin(self.alpha)*cos(x)*sin(self.alpha+self.beta) +
                    cos(self.alpha)*cos(self.alpha+self.beta))

    def antipodal_cos(self, x):
        return (-sin(self.alpha)*cos(x)*sin(self.alpha+self.beta) -
                    cos(self.alpha)* cos(self.alpha+self.beta))

    def pr_obs(self, x):
        return max([0, self.primary_cos(x)])

    def an_obs(self, x):
        return max([0, self.antipodal_cos(x)])

    def to_int(self, x):
        return max([self.pr_obs(x), self.an_obs(x)])

    def flux_1(self, x):
        res = self.primary_cos(x) * (1 - self.r_g / self.r) + self.r_g / self.r
        if res > - self.r_g / (self.r - self.r_g):
            return res
        else:
            return 0.

    def flux_1_obs(self, x):
        res = self.primary_cos(x) * (1 - self.r_g / self.r) + self.r_g / self.r
        return max([0., res])

    def flux_2(self, x):
        res =  self.antipodal_cos(x) * (1 - self.r_g / self.r) + self.r_g / self.r
        if res > - self.r_g / (self.r - self.r_g):
            return res
        else:
            return 0.

    def flux_2_obs(self, x):
        res =  self.antipodal_cos(x) * (1 - self.r_g / self.r) + self.r_g / self.r
        return max([0., res])

    def flux_12(self, x):
        return max([self.flux_1(x), 2. * self.r_g / self.r, self.flux_2(x)])


    # integrates
    def c(self):
        return quad(self.to_int, 0, 2.*pi)[0] / (2. * pi)

    def c_1(self):
        return quad(self.pr_obs, 0, 2.*pi)[0] / (2. * pi)

    def c_2(self):
        return quad(self.an_obs, 0, 2.*pi)[0] / (2. * pi)

    def f_1(self):
        return quad(self.flux_1_obs, 0, 2.*pi)[0] / (2. * pi)

    def f_2(self):
        return quad(self.flux_2_obs, 0, 2.*pi)[0] / (2. * pi)

    def f(self):
        return quad(self.flux_12, 0, 2.*pi)[0] / (2. * pi)



###############################################################################
def main():
    print 'Bye'

###############################################################################
if __name__ == '__main__':
    main()


