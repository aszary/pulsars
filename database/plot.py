import os
from shutil import copyfile
from math import log10
from datetime import datetime
os.environ['MPLCONFIGDIR'] = '/tmp'

import matplotlib as mp
mp.use('Agg')
import matplotlib.pyplot as pl
import numpy as np
from django.core.exceptions import ObjectDoesNotExist

from models import XrayComponent
from pulsars.settings import MEDIA_ROOT
from calcs.interpolate import least_sq1D, least_sq2D, least_sq
from calcs.functions import get_t6

def bb_pl(fits, recreate=False):
    file_name = 'database/plots/bb_pl_age.'
    full_path = MEDIA_ROOT + file_name
    file_name2 = 'database/plots/bb_pl_field.'
    full_path2 = MEDIA_ROOT + file_name2

    if recreate is True:
        lbb_lnts, ages, bds, ordinals = get_bb_pl(fits)

        # vs age plot
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
        pl.ylabel(r"$L_{\rm BB} / L_{\rm PL}$")
        ax = pl.axis()
        pl.axis([ax[0], 9e8, ax[2], 3e1])
        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')

        # vs B_d plot
        mp.rcdefaults()
        mp.rc('font', size=7)
        names_font = 5
        #pl.figure(figsize=(2.95276,2.3622)) #7.5x6
        pl.figure(figsize=(3.14961, 1.9464567)) #8x4.944cm (golden ratio)
        pl.subplots_adjust(left=0.147, bottom=0.179, right=0.97, top=0.97)
        pl.loglog()
        pl.plot(bds, lbb_lnts, 'o', color='black', ms=2.)
        for i in xrange(len(ordinals)):
            pl.text(bds[i], lbb_lnts[i], '%d'%ordinals[i], fontsize=names_font)
        pl.xlabel(r"$B_{\rm d} \,  [ {\rm G} ]$ ")
        pl.ylabel(r"$L_{\rm BB} / L_{\rm PL}$")
        pl.savefig(full_path2 + 'eps')
        pl.savefig(full_path2 + 'pdf')
        pl.savefig(full_path2 + 'svg')

    try:
        copyfile(full_path+'eps', '/home/aszary/work/1_x-ray/images/bb_pl_age.eps')
        copyfile(full_path2+'eps', '/home/aszary/work/1_x-ray/images/bb_pl_field.eps')
    except IOError:
        print 'Warning: bb_pl_age and bb_pl_field copy error'
    return [[full_path + 'svg', file_name +'svg'], [full_path2+ 'svg', file_name2 +'svg']]

def get_bb_pl(fits):
    lbb_lnts = []
    ages = []
    bds = []
    ordinals = []
    for fit in fits:
        bb = fit.components.filter(spec_type='BB').order_by('r')
        pl = fit.components.filter(spec_type='PL')
        try:
            lbb_lnts.append(bb[0].lum / pl[0].lum)
            ages.append(fit.psr_id.additionals.get(num=0).best_age)
            bds.append(fit.psr_id.bsurf)
            ordinals.append(fit.ordinal)
        except TypeError:
            print 'No lum for %s?' % fit.psr_id.name
    return lbb_lnts, ages, bds, ordinals

def xi_age(fits, recreate=False):
    file_name = 'database/plots/xi_age.'
    full_path = MEDIA_ROOT + file_name

    if recreate is True:
        l_x, ages, ordinals, psrs = get_xi_age(fits)

        mp.rcdefaults()
        mp.rc('font', size=7)
        names_font = 5
        #pl.figure(figsize=(2.95276,2.3622)) #7.5x6
        pl.figure(figsize=(3.14961, 1.9464567)) #8x4.944cm (golden ratio)
        pl.subplots_adjust(left=0.147, bottom=0.179, right=0.99, top=0.99)
        pl.loglog()
        pl.plot(ages, l_x, 'o', color='black', ms=2.)
        #for i in xrange(len(ordinals)):
        #    pl.text(ages[i], l_x[i], '%d'%ordinals[i], fontsize=names_font)
        pl.xlabel(r"$\tau \,  [ {\rm yr} ]$ ")
        pl.ylabel(r"$(L_{\rm BB} + L_{\rm PL}) / L_{\rm SD}$")
        ax = pl.axis()
        pl.axis([ax[0], 9e8, ax[2], 3e1])
        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')

    #copyfile(full_path+'eps', '/home/aszary/work/1_x-ray/images/xray_age.eps')
    #copyfile(full_path+'eps', '/home/aszary/work/6_outer/images/xray_age.eps')
    return [[full_path + 'svg', file_name +'svg']]

def get_xi_age(fits):
    l_x = []
    ages = []
    ordinals = []
    psrs = []

    for fit in fits:
        bb = fit.components.filter(spec_type='BB').order_by('r')
        pl_co = fit.components.filter(spec_type='PL')
        lum = 0.
        for b in bb:
            if b.r < 5e5:
                try:
                    lum += b.lum
                except TypeError:
                    print 'Warning: no BB luminosity data for %s' % \
                           fit.psr_id.name
        for pp in pl_co:
            try:
                lum += pp.lum
            except:
                print 'Warning: no PL luminosity data for %s' % fit.psr_id.name
        if lum != 0.:
            l_x.append(lum / fit.psr_id.edot)
            ages.append(fit.psr_id.additionals.get(num=0).best_age)
            ordinals.append(fit.ordinal)
            psrs.append(fit.psr_id)
    return l_x, ages, ordinals, psrs


def xi_field(fits, recreate=False):
    file_name = 'database/plots/xi_field.'
    full_path = MEDIA_ROOT + file_name

    if recreate is True:
        l_x = []
        b_d_ = []
        ordinals = []
        psrs = []

        for fit in fits:
            bb = fit.components.filter(spec_type='BB').order_by('r')
            pl_co = fit.components.filter(spec_type='PL')
            lum = 0.
            for b in bb:
                if b.r < 5e5:
                    try:
                        lum += b.lum
                    except TypeError:
                        pass
            for pp in pl_co:
                try:
                    lum += pp.lum
                except TypeError:
                    pass
            if lum != 0.:
                l_x.append(lum / fit.psr_id.edot)
                b_d_.append(fit.psr_id.bsurf)
                ordinals.append(fit.ordinal)
                psrs.append(fit.psr_id)

        mp.rcdefaults()
        mp.rc('font', size=7)
        names_font = 5
        #pl.figure(figsize=(2.95276,2.3622)) #7.5x6
        pl.figure(figsize=(3.14961, 1.9464567)) #8x4.944cm (golden ratio)
        pl.subplots_adjust(left=0.147, bottom=0.179, right=0.99, top=0.99)
        pl.loglog()
        pl.plot(b_d_, l_x, 'o', color='black', ms=2.)
        #for i in xrange(len(ordinals)):
        #    pl.text(b_d_[i], l_x[i], '%d'%ordinals[i], fontsize=names_font)
        pl.xlabel(r"$B_{\rm d} \,  [ {\rm G} ]$ ")
        pl.ylabel(r"$(L_{\rm BB} + L_{\rm PL}) / L_{\rm SD}$")
        ax = pl.axis()
        #pl.axis([ax[0], 9e8, ax[2], 3e1])
        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')

    #copyfile(full_path+'eps', '/home/aszary/work/1_x-ray/images/xray_age.eps')
    #copyfile(full_path+'eps', '/home/aszary/work/6_outer/images/xray_age.eps')
    return [[full_path + 'svg', file_name +'svg']]


def xi_sd(fits, recreate=True):
    file_name = 'database/plots/xi_sd.'
    full_path = MEDIA_ROOT + file_name

    if recreate is True:
        xi_ = []
        l_sd_ = []
        ordinals = []
        psrs = []

        for fit in fits:
            bb = fit.components.filter(spec_type='BB').order_by('r')
            pl_co = fit.components.filter(spec_type='PL')
            lum = 0.
            for b in bb:
                if b.r < 5e5:
                    try:
                        lum += b.lum
                    except TypeError:
                        pass
            for pp in pl_co:
                try:
                    lum += pp.lum
                except TypeError:
                    pass
            if lum != 0.:
                xi_.append(log10(lum / fit.psr_id.edot))
                l_sd_.append(log10(fit.psr_id.edot))
                ordinals.append(fit.ordinal)
                psrs.append(fit.psr_id)

        fun = lambda v , x: v[0] * x + v[1]
        x2_, y2_, v2 = least_sq(l_sd_, xi_, fun, [1, 1.])

        mp.rcdefaults()
        mp.rc('font', size=7)
        mp.rc('legend', fontsize=6)
        names_font = 5
        #pl.figure(figsize=(2.95276,2.3622)) #7.5x6
        pl.figure(figsize=(3.14961, 1.9464567)) #8x4.944cm (golden ratio)
        pl.minorticks_on()
        pl.subplots_adjust(left=0.147, bottom=0.179, right=0.99, top=0.99)
        #pl.loglog()
        pl.plot(l_sd_, xi_, 'o', color='black', ms=2.)
        #for i in xrange(len(ordinals)):
        #    pl.text(b_d_[i], l_x[i], '%d'%ordinals[i], fontsize=names_font)
        li, = pl.plot(x2_, y2_, ls='--', c='black', lw=1., zorder=9999)
        li.set_dashes([2.5, 2.5])
        l0 = pl.legend([li], [r'$\xi_{\rm x-ray} \propto \dot{E}^{%.2f}$'%v2[0]], loc='lower left')
        pl.xlabel(r"$\log( \dot{E} ) \,  [ {\rm erg \, s^{-1}} ]$ ")
        pl.ylabel(r"$\log (\xi_{\rm x-ray})$")
        pl.ylim([-5.5, -0.5])
        pl.xlim([30.01, 38.99])
        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')

    #copyfile(full_path+'eps', '/home/aszary/work/1_x-ray/images/xray_age.eps')
    #copyfile(full_path+'eps', '/home/aszary/work/6_outer/images/xray_age.eps')
    return [[full_path + 'svg', file_name +'svg']]


def pl_sd(fits, recreate=False):
    file_name = 'database/plots/pl_sd.'
    full_path = MEDIA_ROOT + file_name

    if recreate is True:
        log_lsd_, log_lpl_, err_, ordinals, psrs, log_lsd_left_, log_lpl_left_,  err_left_, log_lsd_right_, log_lpl_right_, err_right_ = get_pl_sd(fits)

        fun = lambda v , x: v[0] * x + v[1]
        #x_, y_, v = least_sq(log_lsd_, log_lpl_, fun, [1, 1.])
        #x2_, y2_, v2 = least_sq1D(log_lsd_, log_lpl_, fun, np.array(err_[0])+np.array(err_[1]), [1, 1.])
        x3_, y3_, v3 = least_sq2D(log_lsd_, log_lpl_, fun, err_, [1, 1.])
        x4_, y4_, v4 = least_sq2D(log_lsd_left_, log_lpl_left_, fun, err_left_, [1, 1.])
        x5_, y5_, v5 = least_sq2D(log_lsd_right_, log_lpl_right_, fun, err_right_, [1, 1.])

        mp.rcdefaults()
        mp.rc('font', size=7)
        mp.rc('legend', fontsize=5)
        #mp.rc('axes', linewidth=0.5)
        names_font = 5
        #pl.figure(figsize=(2.95276,2.3622)) #7.5x6
        pl.figure(figsize=(3.14961, 1.9464567)) #8x4.944cm (golden ratio)
        pl.minorticks_on()
        pl.subplots_adjust(left=0.147, bottom=0.179, right=0.975, top=0.975)
        #pl.loglog()
        #pl.plot(log_lsd_, log_lpl_,ls='None', marker='s', mec='black',
        #        mfc='None', ms=3.)
        pl.plot(x3_, y3_, ls='-', c='red', lw=0.5, label=r'$\propto L_{\rm SD}^{%.2f}$'%v3[0])
        l, = pl.plot(x4_, y4_, ls='--', c='green', lw=0.5, label=r'$\propto L_{\rm SD}^{%.2f}$'%v4[0])
        l.set_dashes([2., 2.])
        l, = pl.plot(x5_, y5_, ls='--', c='blue', lw=0.5, label=r'$\propto L_{\rm SD}^{%.2f}$'%v5[0])
        l.set_dashes([0.5, 0.5])
        pl.errorbar(log_lsd_, log_lpl_, yerr=err_, ls='None', marker='.', mec='black', ecolor='black', lw=0.5, capsize=0., mfc='None', ms=3.)
        #for i in xrange(len(ordinals)):
        #    pl.text(b_d_[i], l_x[i], '%d'%ordinals[i], fontsize=names_font)
        pl.xlabel(r"$\log \left (L_{\rm SD} \right )$ ")
        pl.ylabel(r"$\log \left ( L_{\rm PL} \right )$")
        ax = pl.axis()
        pl.legend(loc='upper left')
        #pl.axis([ax[0], 9e8, ax[2], 3e1])
        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')
        try:
            copyfile(full_path+'eps', '/home/aszary/work/1_x-ray/images/pl_sd.eps')
        except IOError:
            print 'Warning: pl_sd.eps copy error'
    return [[full_path + 'svg', file_name +'svg']]


def get_pl_sd(fits, lr=35.):
    log_lsd_ = []
    log_lpl_ = []
    err_ = [[], []]
    log_lsd_left_ = []
    log_lpl_left_ = []
    err_left_ = [[], []]
    log_lsd_right_ = []
    log_lpl_right_ = []
    err_right_ = [[], []]

    ordinals = []
    psrs = []
    for fit in fits:
        pl_co = fit.components.get(spec_type='PL')
        lum = 0.
        try:
            lum += pl_co.lum
        except:
            print 'Warning no PL luminosity for %s' % fit.psr_id.name
        if (lum > 0. and pl_co.lum_plus is not None and
                    pl_co.lum_minus is not None):
            log_lpl_.append(log10(lum))
            log_lsd_.append(log10(fit.psr_id.edot))
            ordinals.append(fit.ordinal)
            psrs.append(fit.psr_id)
            plus = log10(lum+pl_co.lum_plus) - log10(lum)
            minus = log10(lum) - log10(lum-pl_co.lum_minus)
            err_[0].append(minus)
            err_[1].append(plus)
            if log_lsd_[-1] <= lr:
                log_lsd_left_.append(log_lsd_[-1])
                log_lpl_left_.append(log_lpl_[-1])
                err_left_[0].append(err_[0][-1])
                err_left_[1].append(err_[1][-1])
            else:
                log_lsd_right_.append(log_lsd_[-1])
                log_lpl_right_.append(log_lpl_[-1])
                err_right_[0].append(err_[0][-1])
                err_right_[1].append(err_[1][-1])
        else:
            print 'Warning no PL luminosity data for %s' %fit.psr_id.name
    return (log_lsd_, log_lpl_,  err_, ordinals, psrs,
            log_lsd_left_, log_lpl_left_,  err_left_,
            log_lsd_right_, log_lpl_right_,  err_right_)

def b_parameter(comps, recreate=False):
    res = []
    if recreate is True:
        b_, l_sd_, b_d_, age_, psr_ = get_b_parameters(comps)
    else:
        b_, l_sd_, b_d_, age_, psr_ = None, None, None, None, None

    #if recreate is True:
    res.append(plot_data(l_sd_, b_, psr_, 'b_lsd',
               xlab=r"$L_{\rm SD}$",
               ylab=r"$b$", recreate=recreate))
    res.append(plot_data(b_d_, b_, psr_, 'b_bd',
               xlab=r"$B_{\rm d}$",
               ylab=r"$b$", recreate=recreate))
    res.append(plot_data(age_, b_, psr_, 'b_age',
               xlab=r"$\tau \, [{\rm yr}]}$",
               ylab=r"$b = B_s / B_d$", recreate=recreate, loc_='upper left'))
    return res

def get_b_parameters(comps):
    b_ = []
    l_sd_ = []
    b_d_ = []
    age_ = []
    psr_ = []

    for co in comps:
        b_.append(co.psr_id.calculations.get(num=0).b)
        l_sd_.append(co.psr_id.edot)
        b_d_.append(co.psr_id.bsurf)
        age_.append(co.psr_id.age)
        psr_.append(co.psr_id)
        print co.psr_id.name, co.psr_id.type

    return b_, l_sd_, b_d_, age_, psr_

def t6_b14(comps, recreate=False):
    file_name = 'database/plots/t6_b14.'
    full_path = MEDIA_ROOT + file_name

    if recreate is True:
        t_6_, t6_err_, b_14_, b14_err_, psr_  = get_t6_b14(comps)
        # theoretical prediction
        b14_teor_ = np.logspace(log10(min(b_14_)), log10(5. * max(b_14_)), num=50)
        t6_teor_ = get_t6(b14_teor_)
        t6_teor2_ = t6_teor_ * 1.3
        t6_teor3_ = t6_teor_ * .7

        # plot options
        excludes = ['J2043+2740']
        colors = {'J0633+1746':'black', 'B0355+54':'blue', 'B0628-28':'black', 'B0834+06':'magenta',  'B0943+10':'green',  'B0950+08':'cyan', 'B1133+16':'blue',  'B1719-37':'red',  'B1929+10':'red', 'B2224+65':'black',  'J0108-1431':'red',  'J0633+1746':'brown', 'B1451-68':'brown', 'J2021+4026':'red'}
        txt_pos = {'J0633+1746':[0.11, 1.49], 'B0355+54':[0.3,2.86], 'B0628-28':[0.3,3.4], 'B0834+06':[0.29, 2.05],  'B0943+10':[6., 2.9],  'B0950+08':[0.08,2.4],      'B1133+16':[6., 3.4],  'B1719-37':[0.01,3.6],  'B1929+10':[0.27, 4.65],      'B2224+65':[0.8, 5.9],  'J0108-1431':[0.015, 1.4], 'B1451-68':[1.6, 4.2], 'J2021+4026':[0.013, 2.6]}

        mp.rcdefaults()
        mp.rc('font', size=7)
        mp.rc('legend', fontsize=7)
        names_font = 5
        #pl.figure(figsize=(2.95276,2.3622)) #7.5x6
        #pl.figure(figsize=(3.14961, 1.9464567)) #8x4.944cm (golden ratio)
        pl.figure(figsize=(3.14961, 3.14961)) #8x8cm (golden ratio)
        pl.subplots_adjust(left=0.1, bottom=0.12, right=0.97, top=0.98)
        pl.minorticks_on()
        pl.semilogx()
        l, = pl.plot(b14_teor_, t6_teor_, color='black', ls='--', lw=0.5, label='$T_6=1.1 (B_{14}^{1.1} + 0.3)$')
        l.set_dashes([3., 3.])
        #pl.plot(b14_teor_, t6_teor2_, color='black', ls='')
        #pl.plot(b14_teor_, t6_teor3_, color='black', ls='')
        pl.fill_between(b14_teor_, t6_teor2_, t6_teor3_, edgecolor='None', facecolor='#e6e6e6', alpha=1.0, zorder=0)
        for i in xrange(len(b_14_)):
            na = psr_[i].name
            if na not in excludes:
                pl.errorbar(b_14_[i], t_6_[i], lw=0.5, ms=2., marker='o', mec=colors[na], mfc=colors[na], color=colors[na], xerr=[[b14_err_[0][i]], [b14_err_[1][i]]], yerr=[[t6_err_[0][i]], [t6_err_[1][i]]])
                print psr_[i].name
                try:
                    xt = txt_pos[na][0]
                    yt = txt_pos[na][1]
                except KeyError:
                    xt = b_14_[i]
                    yt = t_6_[i]
                pl.text(xt, yt, '%s'%psr_[i].name, fontsize=names_font, color=colors[na])
        pl.xlabel(r"$B_{14}$ ")
        pl.ylabel(r"$T_6$")
        pl.legend(loc='upper left')
        ax = pl.axis()
        pl.axis([4e-3, 2e2, 1., 7.1])
        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')
        try:
            copyfile(full_path+'eps', '/home/aszary/work/1_x-ray/images/t6_b14.eps')
        except IOError:
            print 'Warninng: t6_b14.eps copy error'

    return [[full_path + 'svg', file_name +'svg']]

def get_t6_b14(comps):
    t_6_ = []
    t6_err_ = [[], []]
    b_14_ = []
    b14_err_ = [[], []]
    psr_ = []

    for co in comps:
        calcs = co.psr_id.calculations.get(num=0)
        if co.r < calcs.r_dp:
            b_14_.append(calcs.b_14)
            b14_err_[0].append(calcs.b_14_minus)
            b14_err_[1].append(calcs.b_14_plus)
            t_6_.append(co.t / 1e6)
            t6_err_[0].append(co.t_minus / 1e6)
            t6_err_[1].append(co.t_plus / 1e6)
            psr_.append(co.psr_id)

    return t_6_, t6_err_, b_14_, b14_err_, psr_


def radio_plots(psrs, recreate=False):
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
    l_sd2_ = []
    l_lsd_age_ = []
    l_lsd_field_ = []
    l_lsd_psr_ = []
    b_d_ = []
    age_ = []
    psr_ = []

    if recreate is True:
        for p in psrs:
            if p.s400 != 0.:
                l400 = p.s400 / 1e3  * (p.dist * 3.08567758e21) ** 2. * 1e-23
                s400_.append(p.s400)
                l400_.append(l400)
                s400_age_.append(p.age)
                s400_psr_.append(p)
                if p.edot > 0.:
                    l400_lsd_.append(l400 / p.edot)
                    l400_lsd_age_.append(p.age)
                    l400_lsd_psr_.append(p)
            if p.s1400 != 0.:
                l1400 = p.s1400 / 1e3  * (p.dist * 3.08567758e21) ** 2. * 1e-23
                s1400_.append(p.s1400)
                l1400_.append(l1400)
                s1400_age_.append(p.age)
                s1400_psr_.append(p)
                if p.edot > 0.:
                    l1400 = p.s1400 / 1e3  * (p.dist * 3.08567758e21) ** 2. * 1e-23
                    l = 7.4e27 * p.dist ** 2. * p.s1400
                    l_lsd_.append(l / p.edot)
                    l_lsd_age_.append(p.age)
                    l1400_lsd_.append(l1400 / p.edot)
                    l_lsd_field_.append(p.bsurf)
                    l_sd2_.append(p.edot)
                    l_lsd_psr_.append(p)
            if p.s2000 != 0.:
                l2000 = p.s2000 / 1e3  * (p.dist * 3.08567758e21) ** 2. * 1e-23
                s2000_.append(p.s2000)
                l2000_.append(l2000)
                s2000_age_.append(p.age)
                s2000_psr_.append(p)
            b_d_.append(p.bsurf)
            age_.append(p.age)
            psr_.append(p)

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
    res.append(plot_data(l_lsd_age_, l1400_lsd_, l_lsd_psr_, 'l1400_lsd_age',
               xlab=r"$\tau \,  [ {\rm yr} ]$",
               ylab=r"$L_{\rm 1400} / L_{\rm SD}$", recreate=recreate))
    res.append(plot_data(l_lsd_age_, l_lsd_, l_lsd_psr_, 'l_lsd_age',
               xlab=r"$\tau \,  [ {\rm yr} ]$",
               ylab=r"$L_{\rm radio} / L_{\rm SD}$", recreate=recreate ))
    res.append(plot_data(l_lsd_field_, l_lsd_, l_lsd_psr_, 'l_lsd_field',
               xlab=r"$B_{\rm d} \,  [ {\rm G} ]$",
               ylab=r"$L_{\rm radio} / L_{\rm SD}$", recreate=recreate))
    res.append(plot_data(l_sd2_, l_lsd_, l_lsd_psr_, 'l_lsd_sd',
               xlab=r"$L_{\rm SD}$",
               ylab=r"$L_{\rm radio} / L_{\rm SD}$", recreate=recreate))

    res.append(plot_data(s2000_age_, s2000_, s2000_psr_, 's2000_age',
               xlab=r"$\tau \,  [ {\rm yr} ]$",
               ylab=r"$S_{2000}$", recreate=recreate ))
    res.append(plot_data(s2000_age_, l2000_, s2000_psr_, 'l2000_age',
               xlab=r"$\tau \,  [ {\rm yr} ]$",
               ylab=r"$L_{2000}$", recreate=recreate ))
    res.append(plot_data(age_, b_d_, psr_, 'bd_age',
               xlab=r"$\tau \,  [ {\rm yr} ]$",
               ylab=r"$B_{\rm d}$", recreate=recreate ))

    #full_path = MEDIA_ROOT + file_name
    #copyfile(full_path+'eps', '/home/aszary/work/6_outer/images/s400_age.eps')
    return res

def custom(pulsars, recreate=False, copy_=False):
    file_name = 'database/plots/custom.'
    full_path = MEDIA_ROOT + file_name

    if recreate is True:
        x_ = []
        y_ = []
        psr_ = []
        # axis labels (for plot)
        x_lab = r'$ \log (\dot{E}) $' # $ \tau [{\rm yr}] $   $ L_{\rm SD} $
        y_lab = r'$\log (S_{\rm freq}) $' # $ b $'
        # get data
        for p in pulsars:
            co_bb, co_pl, calc, ad = get_custom(p)
            try:
                x = log10(float(p.edot))
                #x = log10(float(p.P0) ** (-3.))
                #x = float(ad.best_age)
                #x = float(p.P0)
                #y = co_bb[0].lum
                #y = calc.b#co_pl[0].lum / p.edot
                # L_{XXX MHz}
                #y = log10(p.s400 / 1e3  * (p.dist * 3.08567758e21) ** 2. * 1e-23 / p.edot)
                # L_radio
                #y =  log10(7.4e27 * p.dist ** 2. * p.s1400 / p.edot)
                y = log10(p.s1400 / 1e3 * 1e-23)
                print y#, log10(y)
            except (ValueError, ZeroDivisionError, IndexError, TypeError, UnboundLocalError, AttributeError):
                x = None
                y = None
                print 'Warning ValueError for %s' % p.name
            #if x > 0. and y > 0.:# and float(p.P0) < 0.01:
            if x > 0. and y is not None:
                x_.append(x)
                y_.append(y)
                psr_.append(p)

        ot, he, he2, axp = None, None, None, None
        mp.rcdefaults()
        mp.rc('font', size=9)
        mp.rc('legend', fontsize=7)
        #mp.rc('font', size=12)
        #mp.rc('legend', fontsize=10)

        pl.figure(figsize=(3.14961, 3.14961)) #8x8cm
        #pl.figure(figsize=(5.90551, 5.90551)) #15x15cm
        pl.subplots_adjust(left=0.17, bottom=0.12, right=0.96, top=0.96)
        pl.minorticks_on()
        #pl.semilogy()
        #pl.semilogx()
        #pl.loglog()
        for i in xrange(len(x_)):
            if psr_[i].binary !='*':
                ot, = pl.plot(x_[i], y_[i], '^', mfc='blue', mec='blue', ms=1.5, zorder=50)
            elif psr_[i].type.startswith('HE'):
                he, = pl.plot(x_[i], y_[i], 's', mfc='magenta', mec='magenta', ms=1.5, zorder=40)
            elif psr_[i].type.find('AXP') != -1:
                axp, = pl.plot(x_[i], y_[i], 's', mfc='green', mec='green', ms=1.5, zorder=30)
            elif psr_[i].type.startswith('NRAD'):
                he2, = pl.plot(x_[i], y_[i], 'D', mfc='yellow', mec='yellow', ms=1.5, zorder=20)
            else:
                pl.plot(x_[i], y_[i], 'o', mfc='red', mec='red', ms=1.0, zorder=1)
            #pl.text(x_[i], y_[i], '%s'%psr_[i].name, fontsize=8)

        leg_, lab_= [], []
        if ot is not None:
            leg_.append(ot)
            lab_.append('Binary')
        if he is not None:
            leg_.append(he)
            lab_.append('with pulsed HE radiation')
        if he2 is not None:
            leg_.append(he2)
            lab_.append('HE (no radio)')
        if axp is not None:
            leg_.append(axp)
            lab_.append('AXP')

        pl.legend(leg_, lab_, loc='upper right')
        pl.xlabel(x_lab)
        pl.ylabel(y_lab)
        ax = pl.axis()
        #pl.axis([5e10, 5e13, ax[2], ax[3]])
        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')
        d = datetime.now()
        if copy_ is True:
            try:
                copyfile(full_path+'pdf', MEDIA_ROOT+'database/plots/custom/%d-%d-%dT%d:%d.pdf' % (d.year, d.month, d.day, d.hour, d.minute))
                copyfile(full_path+'svg', MEDIA_ROOT+'database/plots/custom/%d-%d-%dT%d:%d.svg' % (d.year, d.month, d.day, d.hour, d.minute))
            except IOError:
                print 'Warning: customs copy error'
    return [[full_path + 'svg', file_name + 'svg']]

def get_custom(p):
        co_bb = XrayComponent.objects.filter(psr_id=p).filter(xrayfit__ordinal__gt=0).filter(spec_type='BB').order_by('r')
        co_pl = XrayComponent.objects.filter(psr_id=p).filter(xrayfit__ordinal__gt=0).filter(spec_type='PL')
        try:
            calc = p.calculations.get(num=0)
        except ObjectDoesNotExist:
            calc = None
            print 'Warning no calculations for %s' % p.name
        try:
            ad = p.additionals.get(num=0)
        except ObjectDoesNotExist:
            ad = None
            print 'Warning no additionals for %s' % p.name

        return co_bb, co_pl, calc, ad

def xi_sd_radio(pulsars, recreate=False):
    file_name = 'database/plots/radio/xi_sd.'
    full_path = MEDIA_ROOT + file_name

    if recreate is True:
        x_ = []
        y_ = []
        psr_ = []
        xb_ = []
        yb_ = []
        psrb_ = []

        # axis labels (for plot)
        x_lab = r'$ \log (\dot{E}) \, [{\rm erg / s}] $' # $ \tau [{\rm yr}] $   $ L_{\rm SD} $
        y_lab = r'$\log (\xi) $' # $ b $'

        # get data
        for p in pulsars:
            co_bb, co_pl, calc, ad = get_custom(p)
            try:
                x = log10(float(p.edot))
                # L_{XXX MHz}
                #y = log10(p.s1400 / 1e3  * (p.dist * 3.08567758e21) ** 2. * 1e-23 / p.edot)
                # L_radio
                y =  log10(7.4e27 * p.dist ** 2. * p.s1400 / p.edot)
                print y#, log10(y)
            except (ValueError, ZeroDivisionError, IndexError, TypeError, UnboundLocalError, AttributeError):
                x = None
                y = None
                print 'Warning ValueError for %s' % p.name
            if x > 0. and y is not None:
                x_.append(x)
                y_.append(y)
                psr_.append(p)
                if p.binary != '*':
                    xb_.append(x)
                    yb_.append(y)
                    psrb_.append(p)

        fun = lambda v , x: v[0] * x + v[1]
        x2_, y2_, v2 = least_sq(x_, y_, fun, [1, 1.])
        x3_, y3_, v3 = least_sq(xb_, yb_, fun, [1, 1.])

        ot, he, he2, axp = None, None, None, None
        mp.rcdefaults()
        mp.rc('font', size=9)
        mp.rc('legend', fontsize=6)

        pl.figure(figsize=(3.14961, 3.14961)) #8x8cm
        #pl.figure(figsize=(5.90551, 5.90551)) #15x15cm
        pl.subplots_adjust(left=0.17, bottom=0.12, right=0.96, top=0.96)
        pl.minorticks_on()
        for i in xrange(len(x_)):
            if psr_[i].binary !='*':
                ot, = pl.plot(x_[i], y_[i], '^', mfc='blue', mec='blue', ms=1.5, zorder=50)
            elif psr_[i].type.startswith('HE'):
                he, = pl.plot(x_[i], y_[i], 's', mfc='magenta', mec='magenta', ms=1.5, zorder=40)
            elif psr_[i].type.find('AXP') != -1:
                axp, = pl.plot(x_[i], y_[i], 's', mfc='yellow', mec='yellow', ms=1.5, zorder=30)
            else:
                no, = pl.plot(x_[i], y_[i], 'o', mfc='red', mec='red', ms=0.7, zorder=1)
            #pl.text(x_[i], y_[i], '%s'%psr_[i].name, fontsize=8)
        li, = pl.plot(x2_, y2_, ls='--', c='black', lw=1.50, zorder=9999)
        li.set_dashes([3, 3])
        li2, = pl.plot(x3_, y3_, ls='--', c='green', lw=1.50, zorder=9999)
        li2.set_dashes([1.5, 1.5])
        l0 = pl.legend([li, li2], [r'$\xi \propto \dot{E}^{%.2f}$ (all pulsars)'%v2[0], r'$\xi \propto \dot{E}^{%.2f}$ (Binary)'%v3[0]], loc='lower left')
        leg_, lab_= [], []
        if ot is not None:
            leg_.append(ot)
            lab_.append('Binary')
        if he is not None:
            leg_.append(he)
            lab_.append('with pulsed HE radiation')
        if axp is not None:
            leg_.append(axp)
            lab_.append('AXP')
        leg_.append(no)
        lab_.append('Other')
        l2 = pl.legend(leg_, lab_, loc='upper right')
        pl.gca().add_artist(l0)
        pl.xlabel(x_lab)
        pl.ylabel(y_lab)
        ax = pl.axis()
        #pl.axis([28.01, 39.99, -11.01, 0.99])
        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')
        print len(x_)
        try:
            copyfile(full_path+'eps', '/home/aszary/work/0_radio_efficiency/images/xi_sd.eps')
        except IOError:
            print 'Warning: xi_sd.eps copy error'
    return [ [full_path + 'svg', file_name + 'svg']]


def xi_age_radio(pulsars, recreate=False):
    file_name = 'database/plots/radio/xi_age.'
    full_path = MEDIA_ROOT + file_name

    if recreate is True:
        x_ = []
        y_ = []
        psr_ = []

        # axis labels (for plot)
        x_lab = r'$ \log (\tau) \, [{\rm yr}] $'
        y_lab = r'$\log (\xi) $' # $ b $'

        # get data
        for p in pulsars:
            try:
                x = log10(float(p.age))
                # L_{XXX MHz}
                #y = log10(p.s1400 / 1e3  * (p.dist * 3.08567758e21) ** 2. * 1e-23 / p.edot)
                # L_radio
                y =  log10(7.4e27 * p.dist ** 2. * p.s1400 / p.edot)
                print y#, log10(y)
            except (ValueError, ZeroDivisionError, IndexError, TypeError, UnboundLocalError, AttributeError):
                x = None
                y = None
                print 'Warning ValueError for %s' % p.name
            if x > 0. and y is not None:
                x_.append(x)
                y_.append(y)
                psr_.append(p)

        fun = lambda v , x: v[0] * x + v[1]
        x2_, y2_, v2 = least_sq(x_, y_, fun, [1, 1.])

        ot, he, he2, axp = None, None, None, None
        mp.rcdefaults()
        mp.rc('font', size=9)
        mp.rc('legend', fontsize=6)

        pl.figure(figsize=(3.14961, 3.14961)) #8x8cm
        #pl.figure(figsize=(5.90551, 5.90551)) #15x15cm
        pl.subplots_adjust(left=0.17, bottom=0.12, right=0.96, top=0.96)
        pl.minorticks_on()
        for i in xrange(len(x_)):
            if psr_[i].type.startswith('HE'):
                he, = pl.plot(x_[i], y_[i], 's', mfc='magenta', mec='magenta', ms=1.5, zorder=40)
            elif psr_[i].type.find('AXP') != -1:
                axp, = pl.plot(x_[i], y_[i], 's', mfc='yellow', mec='yellow', ms=1.5, zorder=30)
            else:
                no, = pl.plot(x_[i], y_[i], 'o', mfc='red', mec='red', ms=0.7, zorder=1)
            #pl.text(x_[i], y_[i], '%s'%psr_[i].name, fontsize=8)
        li, = pl.plot(x2_, y2_, ls='--', c='black', lw=1.50, zorder=9999)
        li.set_dashes([3, 3])
        l0 = pl.legend([li], [r'$\xi \propto \dot{\tau}^{%.2f}$'%v2[0]], loc='lower left')
        leg_, lab_= [], []
        if he is not None:
            leg_.append(he)
            lab_.append('with pulsed HE radiation')
        if axp is not None:
            leg_.append(axp)
            lab_.append('AXP')
        leg_.append(no)
        lab_.append('Other')
        l2 = pl.legend(leg_, lab_, loc='upper right')
        pl.gca().add_artist(l0)
        pl.xlabel(x_lab)
        pl.ylabel(y_lab)
        ax = pl.axis()
        #pl.axis([28.01, 39.99, -11.01, 0.99])
        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')
        print len(x_)
        try:
            copyfile(full_path+'eps', '/home/aszary/work/0_radio_efficiency/images/xi_age.eps')
        except IOError:
            print 'Warning: xi_age.eps copy error'
    return [ [full_path + 'svg', file_name + 'svg']]


def l_sd_radio(pulsars, recreate=False):
    file_name = 'database/plots/radio/l1400_sd.'
    full_path = MEDIA_ROOT + file_name

    if recreate is True:

        x_ = []
        y_ = []
        psr_ = []
        xb_ = []
        yb_ = []
        psrb_ = []

        # axis labels (for plot)
        x_lab = r'$ \log (\dot{E}) \, [{\rm erg / s}] $' # $ \tau [{\rm yr}] $   $ L_{\rm SD} $
        y_lab = r'$\log (L_{1400})  \, [{\rm erg / s}]  $' # $ b $'

        # get data
        for p in pulsars:
            co_bb, co_pl, calc, ad = get_custom(p)
            try:
                x = log10(float(p.edot))
                # L_{XXX MHz}
                y = log10(p.s1400 / 1e3  * (p.dist * 3.08567758e21) ** 2. * 1e-23 )
                # L_radio
                #y =  log10(7.4e27 * p.dist ** 2. * p.s1400)
            except (ValueError, ZeroDivisionError, IndexError, TypeError,
                    UnboundLocalError, AttributeError):
                x = None
                y = None
                print 'Warning ValueError for %s' % p.name
            if x > 0. and y is not None:
                x_.append(x)
                y_.append(y)
                psr_.append(p)
                if p.binary != '*':
                    xb_.append(x)
                    yb_.append(y)
                    psrb_.append(p)

        fun = lambda v , x: v[0] * x + v[1]
        x2_, y2_, v2 = least_sq(x_, y_, fun, [1, 1.])
        x3_, y3_, v3 = least_sq(xb_, yb_, fun, [1, 1.])

        ot, he, he2, axp = None, None, None, None
        mp.rcdefaults()
        mp.rc('font', size=9)
        mp.rc('legend', fontsize=5)

        pl.figure(figsize=(3.14961, 3.14961)) #8x8cm
        #pl.figure(figsize=(5.90551, 5.90551)) #15x15cm
        pl.subplots_adjust(left=0.17, bottom=0.12, right=0.96, top=0.96)
        pl.minorticks_on()
        for i in xrange(len(x_)):
            if psr_[i].binary !='*':
                ot, = pl.plot(x_[i], y_[i], '^', mfc='blue', mec='blue', ms=1.5, zorder=50)
            elif psr_[i].type.startswith('HE'):
                he, = pl.plot(x_[i], y_[i], 's', mfc='magenta', mec='magenta', ms=1.5, zorder=40)
            elif psr_[i].type.find('AXP') != -1:
                axp, = pl.plot(x_[i], y_[i], 's', mfc='yellow', mec='yellow', ms=1.5, zorder=30)
            else:
                no, = pl.plot(x_[i], y_[i], 'o', mfc='red', mec='red', ms=0.7, zorder=1)
            #pl.text(x_[i], y_[i], '%s'%psr_[i].name, fontsize=8)
        li, = pl.plot(x2_, y2_, ls='--', c='black', lw=1.50, zorder=9999)
        li.set_dashes([3, 3])
        li2, = pl.plot(x3_, y3_, ls='--', c='green', lw=1.50, zorder=9999)
        li2.set_dashes([1.5, 1.5])
        l0 = pl.legend([li, li2],
            [r'$L_{1400} \propto \dot{E}^{%.2f}$ (all pulsars)'%v2[0],
             r'$L_{1400} \propto \dot{E}^{%.2f}$ (Binary)'%v3[0]], loc='lower left')
        leg_, lab_= [], []
        if ot is not None:
            leg_.append(ot)
            lab_.append('Binary')
        if he is not None:
            leg_.append(he)
            lab_.append('with pulsed HE radiation')
        if axp is not None:
            leg_.append(axp)
            lab_.append('AXP')
        leg_.append(no)
        lab_.append('Other')
        l2 = pl.legend(leg_, lab_, loc='lower right')
        pl.gca().add_artist(l0)
        pl.xlabel(x_lab)
        pl.ylabel(y_lab)
        ax = pl.axis()
        #pl.axis([28.01, 39.99, -11.01, 0.99])
        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')

    return [ [full_path + 'svg', file_name + 'svg']]


def ll_sd_radio(pulsars, recreate=False):

    file_name = 'database/plots/radio/ll_sd.'
    full_path = MEDIA_ROOT + file_name

    if recreate is True:
        x_ = []
        y_ = []
        x_sec_ = []
        y_sec_ = []
        psr_ = []
        xb_ = []
        yb_ = []
        xb_sec_ = []
        yb_sec_ = []
        psr_sec_ = []
        psrb_ = []

        # axis labels (for plot)
        x_lab = r'$ \log (\dot{E}) \, [{\rm erg / s}] $' # $ \tau [{\rm yr}] $   $ L_{\rm SD} $
        y_lab = r'$\log (L_{\rm freq})  \, [{\rm erg / s}]  $' # $ b $'

        # get data
        for p in pulsars:
            try:
                x = log10(float(p.edot))
                y = log10(p.s400 / 1e3  * (p.dist * 3.08567758e21) ** 2. * 1e-23 )
            except (ValueError, ZeroDivisionError, IndexError, TypeError, UnboundLocalError, AttributeError):
                x = None
                y = None
                print 'Warning ValueError for %s' % p.name
            if x > 0. and y is not None:
                x_.append(x)
                y_.append(y)
                psr_.append(p)
                if p.binary != '*':
                    xb_.append(x)
                    yb_.append(y)
                    psrb_.append(p)
            try:
                x2 = log10(float(p.edot))
                y2 = log10(p.s2000 / 1e3  * (p.dist * 3.08567758e21) ** 2. * 1e-23 )
            except (ValueError, ZeroDivisionError, IndexError, TypeError, UnboundLocalError, AttributeError):
                x2 = None
                y2 = None
                print 'Warning ValueError for %s' % p.name
            if x2 > 0. and y2 is not None:
                x_sec_.append(x2)
                y_sec_.append(y2)
                psr_sec_.append(p)
                if p.binary != '*':
                    xb_sec_.append(x2)
                    yb_sec_.append(y2)

        fun = lambda v , x: v[0] * x + v[1]
        x2_, y2_, v2 = least_sq(x_, y_, fun, [1, 1.])
        x3_, y3_, v3 = least_sq(xb_, yb_, fun, [1, 1.])
        x4_, y4_, v4 = least_sq(x_sec_, y_sec_, fun, [1, 1.])
        x5_, y5_, v5 = least_sq(xb_sec_, yb_sec_, fun, [1, 1.])

        ot, he, he2, axp = None, None, None, None
        mp.rcdefaults()
        mp.rc('font', size=9)
        mp.rc('legend', fontsize=5)

        pl.figure(figsize=(3.14961, 3.14961)) #8x8cm
        #pl.figure(figsize=(5.90551, 5.90551)) #15x15cm
        pl.subplots_adjust(left=0.17, bottom=0.12, right=0.96, top=0.96)
        pl.minorticks_on()
        for i in xrange(len(x_)):
            if psr_[i].binary !='*':
                bi400, = pl.plot(x_[i], y_[i], '^', mfc='red', mec='red', ms=2.0, zorder=2)
            else:
                n400, = pl.plot(x_[i], y_[i], 'o', mfc='red', mec='red', ms=1.0, zorder=1)
        for i in xrange(len(x_sec_)):
            if psr_sec_[i].binary !='*':
                bi2000, = pl.plot(x_sec_[i], y_sec_[i], '^', mfc='blue', mec='blue', ms=2.0, zorder=4)
            else:
                n2000, = pl.plot(x_sec_[i], y_sec_[i], 'o', mfc='blue', mec='blue', ms=2.0, zorder=3)

            #pl.text(x_[i], y_[i], '%s'%psr_[i].name, fontsize=8)
        li, = pl.plot(x2_, y2_, ls='--', c='black', lw=1.0, zorder=9999)
        li.set_dashes([2.5, 2.5])
        li2, = pl.plot(x3_, y3_, ls='--', c='black', lw=1.0, zorder=9999)
        li2.set_dashes([1., 1.])
        li3, = pl.plot(x4_, y4_, ls='--', c='green', lw=1.0, zorder=9999)
        li3.set_dashes([2.5, 2.5])
        li4, = pl.plot(x5_, y5_, ls='--', c='green', lw=1.0, zorder=9999)
        li4.set_dashes([1., 1.])
        l0 = pl.legend([li, li2, li3, li4], [r'$L_{400} \propto \dot{E}^{%.2f}$ (all pulsars)'%v2[0], r'$L_{400} \propto \dot{E}^{%.2f}$ (Binary)'%v3[0], r'$L_{2000} \propto \dot{E}^{%.2f}$ (all pulsars)'%v4[0], r'$L_{2000} \propto \dot{E}^{%.2f}$ (Binary)'%v5[0]], loc='lower left')
        #pl.legend(loc='lower right')
        l1 = pl.legend([n400, bi400, n2000, bi2000], ['$L_{400}$', '$L_{400}$ (Binary)', '$L_{2000}$', '$L_{2000}$ (Binary)'], loc='lower right')
        pl.gca().add_artist(l0)
        pl.xlabel(x_lab)
        pl.ylabel(y_lab)
        ax = pl.axis()
        #pl.axis([28.01, 39.99, -11.01, 0.99])
        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')
    return [[full_path + 'svg', file_name + 'svg']]


def flux_sd_radio(pulsars, recreate=False):

    file_name = 'database/plots/radio/flux_sd.'
    full_path = MEDIA_ROOT + file_name

    if recreate is True:
        x_ = []
        y_ = []
        eff_ = []
        psr_ = []

        sd_low_ = []
        eff_low_ = []

        # axis labels (for plot)
        x_lab = r'$ \log (\dot{E}) \, [{\rm erg \, s^{-1}}] $' # $ \tau [{\rm yr}] $   $ L_{\rm SD} $
        y_lab = r'$\log (S_{1400})  \, [{\rm erg \, s^{-1} \, cm^{-2} \, Hz^{-1}}]  $' # $ b $'

        # get data
        for p in pulsars:
            co_bb, co_pl, calc, ad = get_custom(p)
            try:
                x = log10(float(p.edot))
                # L_{XXX MHz}
                y = log10(p.s1400 / 1e3 * 1e-23)
                # L_radio
                eff =  log10(7.4e27 * p.dist ** 2. * p.s1400 / p.edot)
            except (ValueError, ZeroDivisionError, IndexError, TypeError, UnboundLocalError, AttributeError):
                x = None
                y = None
                print 'Warning ValueError for %s' % p.name
            if x > 0. and y is not None:
                x_.append(x)
                y_.append(y)
                eff_.append(eff)
                psr_.append(p)
                if x <= 31:
                    sd_low_.append(x)
                    eff_low_.append(eff)


        ot, he, he2, axp = None, None, None, None
        mp.rcdefaults()
        mp.rc('font', size=9)
        mp.rc('legend', fontsize=5)

        fig =   pl.figure(figsize=(3.14961, 3.14961)) #8x8cm
        #pl.figure(figsize=(5.90551, 5.90551)) #15x15cm
        pl.subplots_adjust(left=0.17, bottom=0.12, right=0.96, top=0.8)
        pl.minorticks_on()
        sc = pl.scatter(x_, y_, c=eff_, marker='o', s=7, edgecolor="none")
        pl.xlabel(x_lab)
        pl.ylabel(y_lab)
        ax = pl.axis()
        pl.axis([28.01, 38.99, -28.7, -23.3])
        cbaxes = fig.add_axes([0.2, 0.9, 0.75, 0.05])
        cb = pl.colorbar(sc, cax=cbaxes, ticks=[-9, -7, -5, -3, -1], orientation='horizontal')
        cb.ax.set_xlabel(r'$\xi$', labelpad=-35)
        cb.ax.set_xticklabels([r'$10^{-9}$', r'$10^{-7}$', r'$10^{-5}$', r'$10^{-3}$', r'$10^{-1}$'])

        print len(eff_low_), min(eff_low_)

        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')
    return [ [full_path + 'svg', file_name + 'svg']]


def malov_radio(pulsars, recreate=False):
    file_name = 'database/plots/radio/l_sd_malov.'
    full_path = MEDIA_ROOT + file_name

    if recreate is True:
        x_ = []
        y_ = []
        psr_ = []

        # axis labels (for plot)
        x_lab = r'$ \log (\dot{E}) \, [{\rm erg \, s^{-1}}] $' # $ \tau [{\rm yr}] $   $ L_{\rm SD} $
        y_lab = r'$\log (L_{\rm Malov} / \dot{E}) $' # $ b $'

        # get data
        for p in pulsars:
            try:
                x = log10(float(p.edot))
                # L_{XXX MHz}
                y = log10(p.lum_malov / p.edot)
                # L_radio
            except (ValueError, ZeroDivisionError, IndexError, TypeError,
                    UnboundLocalError, AttributeError):
                x = None
                y = None
                print 'Warning ValueError for %s' % p.name
            if x > 0. and y is not None:
                x_.append(x)
                y_.append(y)
                psr_.append(p)

        fun = lambda v , x: v[0] * x + v[1]
        x2_, y2_, v2 = least_sq(x_, y_, fun, [1, 1.])


        ot, he, he2, axp = None, None, None, None
        mp.rcdefaults()
        mp.rc('font', size=9)
        mp.rc('legend', fontsize=5)

        pl.figure(figsize=(3.14961, 3.14961)) #8x8cm
        #pl.figure(figsize=(5.90551, 5.90551)) #15x15cm
        pl.subplots_adjust(left=0.17, bottom=0.12, right=0.96, top=0.96)
        pl.minorticks_on()
        for i in xrange(len(x_)):
            if psr_[i].binary !='*':
                ot, = pl.plot(x_[i], y_[i], '^', mfc='blue', mec='blue', ms=1.5, zorder=50)
            elif psr_[i].type.startswith('HE'):
                he, = pl.plot(x_[i], y_[i], 's', mfc='magenta', mec='magenta', ms=1.5, zorder=40)
            elif psr_[i].type.find('AXP') != -1:
                axp, = pl.plot(x_[i], y_[i], 's', mfc='yellow', mec='yellow', ms=1.5, zorder=30)
            else:
                no, = pl.plot(x_[i], y_[i], 'o', mfc='red', mec='red', ms=0.7, zorder=1)
            #pl.text(x_[i], y_[i], '%s'%psr_[i].name, fontsize=8)
        li, = pl.plot(x2_, y2_, ls='--', c='black', lw=1.50, zorder=9999)
        li.set_dashes([3, 3])
        l0 = pl.legend([li],
            [r'$\xi_{\rm Malov} \propto \dot{E}^{%.2f}$'%v2[0]], loc='lower left')
        leg_, lab_= [], []
        if ot is not None:
            leg_.append(ot)
            lab_.append('Binary')
        if he is not None:
            leg_.append(he)
            lab_.append('with pulsed HE radiation')
        if axp is not None:
            leg_.append(axp)
            lab_.append('AXP')
        leg_.append(no)
        lab_.append('Other')
        l2 = pl.legend(leg_, lab_, loc='upper right')
        pl.gca().add_artist(l0)
        pl.xlabel(x_lab)
        pl.ylabel(y_lab)
        ax = pl.axis()
        #pl.axis([28.01, 39.99, -11.01, 0.99])
        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')
        #copyfile(full_path+'eps', '/home/aszary/work/0_radio_efficiency/f72.eps')

    return [ [full_path + 'svg', file_name + 'svg']]

def plot_data(x_, y_, psrs, name, xlab=r"$\tau \,  [ {\rm yr} ]$",
         ylab=r"$L_{1400} / L_{\rm SD}$", recreate=False, loc_='upper right'):

    file_name = 'database/plots/%s.'%name
    full_path = MEDIA_ROOT + file_name

    if recreate:
        ot, he, he2, axp = None, None, None, None
        mp.rcdefaults()
        mp.rc('font', size=7)
        mp.rc('legend', fontsize=5)

        pl.figure(figsize=(3.14961, 1.9464567)) #8x4.944cm (golden ratio)
        pl.subplots_adjust(left=0.16, bottom=0.18, right=0.96, top=0.95)
        pl.loglog()
        for i in xrange(len(x_)):
            if psrs[i].binary !='*':
                ot, = pl.plot(x_[i], y_[i], '^', mfc='blue', mec='blue', ms=1.5, zorder=50)
            elif psrs[i].type.startswith('HE'):
                he, = pl.plot(x_[i], y_[i], 's', mfc='magenta', mec='magenta', ms=1.5, zorder=40)
            elif psrs[i].type.find('AXP') != -1:
                axp, = pl.plot(x_[i], y_[i], 's', mfc='green', mec='green', ms=1.5, zorder=30)
            elif psrs[i].type.startswith('NRAD'):
                he2, = pl.plot(x_[i], y_[i], 'D', mfc='yellow', mec='yellow', ms=1.5, zorder=20)
            else:
                pl.plot(x_[i], y_[i], 'o', mfc='red', mec='red', ms=0.6, zorder=1)
            #pl.text(x_[i], y_[i], '%s'%psrs[i].name, fontsize=3)
        leg_, lab_= [], []
        if ot is not None:
            leg_.append(ot)
            lab_.append('Binary')
        if he is not None:
            leg_.append(he)
            lab_.append('with pulsed HE radiation')
        if he2 is not None:
            leg_.append(he2)
            lab_.append('HE (no radio)')
        if axp is not None:
            leg_.append(axp)
            lab_.append('AXP')
        pl.legend(leg_, lab_, loc=loc_)
        pl.xlabel(xlab)
        pl.ylabel(ylab)
        ax = pl.axis()
        #pl.axis([5e10, 5e13, ax[2], ax[3]])

        pl.savefig(full_path + 'eps')
        pl.savefig(full_path + 'pdf')
        pl.savefig(full_path + 'svg')
    return [ full_path + 'svg', file_name + 'svg']
