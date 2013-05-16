#! /usr/bin/env python
# -*- coding: utf-8 -*-
__author__="andrzej"
__date__ ="$2008-09-29 18:11:55$"
################################################################################
from math import pi

################################################################################
class CGS:

    meter_si = 1e2
    kg_si = 1e3

    h_bar = 1.0545726663e-27
    h = 6.626075540e-27
    c = 29979245800.0
    e = 4.803206814e-10 #esu
    q_i = 26. * 4.803206814e-10
    m = 9.109389754e-28
    m_e = 9.109389754e-28
    m_p = 1.672623110e-24
    m_n = 1.674928610e-24
    m_i = 26. * m_p + 30. * m_n

    G = 6.6725985e-8

    B_crit = m**2*c**3/(e*h_bar)

    b = 0.28977685 # Wien's displacment constant

    k = 1.38065812e-16 # Boltzmann constant
    sigma = pi**2.*k**4./(60.*h_bar**3.*c**2.) #Stefan-Boltzman constant
    sigma = 5.6705119e-5 #more accurate

    sigma_th = 8.*pi/3. *(e**2./(m*c**2.))**2. #Thompson cross section
    sigma_th = 6.6524586e-25 #more accurate

    alpha = e**2./(h_bar*c) #Fine structure constant
    alpha = 7.297352537650e-3 #more accurate

    a_0 = h_bar / (m * c * alpha) # Bhor radius
    #a_0 = 52.9177e-10 # more accurate

    lambda_c = h/(m*c) #Electron Compton wavelength
    lambda_c= 2.4263102175e-10 #more accurate


class SI:

    meter_si = 1.
    kg_si = 1.

    h_bar = 1.054571628e-34
    h = 6.62606896e-34
    c = 299792458.0
    e = 1.602176487e-19
    m = 9.10938215e-31
    epsilon_0 = 8.854187817e-12
    mu_0 = 12.566370614e-7

    G =6.67428e-11

    b = 2.8977685e-3 # Wien's displacment constant
    k =	1.3806504e-23 # Boltzmann constant

    alpha = e**2./(h_bar*c*4.*pi*epsilon_0) #Fine structure constant
    alpha = 7.2973525376e-3 #more accurate

    lambda_c = h/(c*m) #Electron Compton wavelength
    lambda_c = 2.4263102175e-12 #more accurate



################################################################################
def main():

    c = CGS
    print c.m_i / c.m_e
    print 79*"-"

    print "CGS units:"
    for var in dir(CGS):
        if not var.startswith("_"):
            print "%s=%e"%(var,getattr(CGS,var))

    print 79*"-"
    print 79*"-"

    print "SI units:"
    for var in dir(SI):
        if not var.startswith("_"):
            print "%s=%e"%(var,getattr(SI,var))

    print 79*"-"

    print 'Bye'
    pass

################################################################################
if __name__ == '__main__':
    main()
