import os
from shutil import copyfile
os.environ['MPLCONFIGDIR'] = '/tmp'

import matplotlib as mp
mp.use('Agg')
import matplotlib.pyplot as pl

from pulsars.settings import MEDIA_ROOT

def xray_age(fits):
    lbb_lnts, ages, ordinals = xray_age_calculate(fits)

    mp.rcdefaults()
    mp.rc('font', size=7)
    names_font = 5

    #pl.figure(figsize=(2.95276,2.3622)) #7.5x6
    pl.figure(figsize=(3.14961, 1.9464567)) #8x4.944cm (golden ratio)
    pl.subplots_adjust(left=0.147, bottom=0.179, right=0.99, top=0.99)
    pl.loglog()
    pl.plot(ages, lbb_lnts, 'o', color='black', ms=2.)
    for i in xrange(len(ordinals)):
        pl.text(ages[i], lbb_lnts[i], '%d'%ordinals[i], fontsize=names_font)

    pl.xlabel(r"$\tau \,  [ {\rm yr} ]$ ")
    pl.ylabel(r"$L_{\rm bol} / L_{\rm NT}$")
    ax = pl.axis()
    pl.axis([ax[0], 9e8, ax[2], 3e1])

    file_name = 'database/plots/xray_age.'
    full_path = MEDIA_ROOT + file_name
    pl.savefig(full_path + 'eps')
    pl.savefig(full_path + 'pdf')
    pl.savefig(full_path + 'svg')
    copyfile(full_path+'eps', '/home/aszary/work/1_x-ray/images/xray_age.eps')
    copyfile(full_path+'eps', '/home/aszary/work/6_outer/images/xray_age.eps')
    return full_path + 'svg', file_name +'svg'

def xray_age_calculate(fits):
    lbb_lnts = []
    ages = []
    ordinals = []
    for fit in fits:
        bb = fit.components.filter(spec_type='BB').order_by('r')
        pl = fit.components.filter(spec_type='PL')
        print len(bb), len(pl), bb[0].r
        try:
            lbb_lnts.append(bb[0].lum / pl[0].lum)
            ages.append(fit.psr_id.additionals.get(num=0).best_age)
            ordinals.append(fit.ordinal)
        except TypeError:
            print 'No lum for %s?' % fit.psr_id.Name
    return lbb_lnts, ages, ordinals

def radio_plots(psrs):
    res = []

    # get data
    s400_ = []
    s400_age_ = []
    s400_psr_ = []
    s1400_ = []
    s1400_age_ = []
    s1400_psr_ = []
    s2000_ = []
    s2000_age_ = []
    s2000_psr_ = []
    l400_ = []
    l1400_ = []
    l2000_ = []

    l400_lsd_ = []
    l400_lsd_age_ = []
    l400_lsd_psr_ = []
    l1400_lsd_ = []
    l1400_lsd_age_ = []
    l1400_lsd_psr_ = []
    l2000_lsd_ = []
    l2000_lsd_age_ = []
    l2000_lsd_psr_ = []
    l_lsd_ = []
    l_lsd_age_ = []
    l_lsd_field_ = []
    l_lsd_psr_ = []

    for p in psrs:
        if p.S400 != 0.:
            l400 = p.S400 / 1e3  * (p.Dist * 3.08567758e21) ** 2. * 1e-23
            s400_.append(p.S400)
            l400_.append(l400)
            s400_age_.append(p.Age)
            s400_psr_.append(p)
            if p.Edot > 0.:
                l400_lsd_.append(l400 / p.Edot)
                l400_lsd_age_.append(p.Age)
                l400_lsd_psr_.append(p)
        if p.S1400 != 0.:
            l1400 = p.S1400 / 1e3  * (p.Dist * 3.08567758e21) ** 2. * 1e-23
            s1400_.append(p.S1400)
            l1400_.append(l1400)
            s1400_age_.append(p.Age)
            s1400_psr_.append(p)
            if p.Edot > 0.:
                l = 7.4e27 * p.Dist ** 2. * p.S1400
                l_lsd_.append(l / p.Edot)
                l_lsd_age_.append(p.Age)
                l_lsd_field_.append(p.BSurf)
                l_lsd_psr_.append(p)
        if p.S2000 != 0.:
            l2000 = p.S2000 / 1e3  * (p.Dist * 3.08567758e21) ** 2. * 1e-23
            s2000_.append(p.S2000)
            l2000_.append(l2000)
            s2000_age_.append(p.Age)
            s2000_psr_.append(p)

    #recreate = True
    recreate = False

    res.append(plot_data(s400_age_, s400_, s400_psr_, 's400_age',
               xlab=r"$\tau \,  [ {\rm yr} ]$",
               ylab=r"$S_{400}$", recreate=recreate))
    res.append(plot_data(s400_age_, l400_, s400_psr_, 'l400_age',
               xlab=r"$\tau \,  [ {\rm yr} ]$",
               ylab=r"$L_{400}$", recreate=recreate ))
    res.append(plot_data(l400_lsd_age_, l400_lsd_, l400_lsd_psr_, 'l400_lsd_age',
               xlab=r"$\tau \,  [ {\rm yr} ]$",
               ylab=r"$L_{400} / L_{\rm SD}$", recreate=recreate ))

    res.append(plot_data(s1400_age_, s1400_, s1400_psr_, 's1400_age',
               xlab=r"$\tau \,  [ {\rm yr} ]$",
               ylab=r"$S_{1400}$", recreate=recreate ))
    res.append(plot_data(s1400_age_, l1400_, s1400_psr_, 'l1400_age',
               xlab=r"$\tau \,  [ {\rm yr} ]$",
               ylab=r"$L_{1400}$", recreate=recreate ))
    res.append(plot_data(l_lsd_age_, l_lsd_, l_lsd_psr_, 'l_lsd_age',
               xlab=r"$\tau \,  [ {\rm yr} ]$",
               ylab=r"$L_{\rm radio} / L_{\rm SD}$", recreate=recreate ))
    res.append(plot_data(l_lsd_field_, l_lsd_, l_lsd_psr_, 'l_lsd_field',
               xlab=r"$B_d \,  [ {\rm G} ]$",
               ylab=r"$L_{\rm radio} / L_{\rm SD}$", recreate=recreate ))

    res.append(plot_data(s2000_age_, s2000_, s2000_psr_, 's2000_age',
               xlab=r"$\tau \,  [ {\rm yr} ]$",
               ylab=r"$S_{2000}$", recreate=recreate ))
    res.append(plot_data(s2000_age_, l2000_, s2000_psr_, 'l2000_age',
               xlab=r"$\tau \,  [ {\rm yr} ]$",
               ylab=r"$L_{2000}$", recreate=recreate ))

    print res

    '''
    for p in psrs:
        s400s.append(p.S400)
        # in ergs
        l1400 = p.S1400 / 1e3  * (p.Dist * 3.08567758e21) ** 2. * 1e-23
        l400s.append(l400)
        ages.append(p.Age)
        if p.Edot != 0.:
            l400_lsd_.append(l400 / p.Edot)
            ages_lsd.append(p.Age)
        if p.Edot != 0. and p.S1400 != 0.:
            l_lsd_.append(7.4e27 * p.Dist ** 2. * p.S1400 / p.Edot)
            l1400_lsd_.append(l1400 / p.Edot)
            ages_lsd2.append(p.Age)
        if p.S1400 !=0:
            s1400s.append(p.S1400)
    '''

    #full_path = MEDIA_ROOT + file_name
    #copyfile(full_path+'eps', '/home/aszary/work/1_x-ray/images/s400_age.eps')
    #copyfile(full_path+'eps', '/home/aszary/work/6_outer/images/s400_age.eps')
    return res

def plot_data(x_, y_, psrs, name, xlab=r"$\tau \,  [ {\rm yr} ]$",
         ylab=r"$L_{1400} / L_{\rm SD}$", recreate=False):

    file_name = 'database/plots/%s.'%name
    full_path = MEDIA_ROOT + file_name

    if recreate:
        mp.rcdefaults()
        mp.rc('font', size=7)

        pl.figure(figsize=(3.14961, 1.9464567)) #8x4.944cm (golden ratio)
        pl.subplots_adjust(left=0.16, bottom=0.18, right=0.96, top=0.95)
        pl.loglog()
        for i in xrange(len(x_)):
            if psrs[i].Binary !='*':
                pl.plot(x_[i], y_[i], '^', mfc='blue', mec='blue', ms=1.5)
            else:
                pl.plot(x_[i], y_[i], 'o', mfc='black', ms=0.7)
            if psrs[i].Type.startswith('HE'):
                pl.plot(x_[i], y_[i], 'D', mfc='red', mec='red', ms=1.5)
        pl.xlabel(xlab)
        pl.ylabel(ylab)
        ax = pl.axis()
        #pl.axis([5e10, 5e13, ax[2], ax[3]])

        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')
    return [ full_path + 'svg', file_name + 'svg']



