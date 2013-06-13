import os
from math import log10, pi
from shutil import copyfile

from models import XrayComponent, XrayFit
from calcs.functions import radio_lum
from plot import dist_hist
from pulsars.settings import MEDIA_ROOT

def table_bb(pulsars):

    start_table =r"""
\begin{table*}
    \caption[Observed spectral properties of X-ray detected rotation-powered pulsars with blackbody spectrum component]{Observed spectral properties of X-ray detected rotation-powered pulsars with blackbody spectrum component. The individual columns are as follows: (1) Pulsar name, (2) Spectral components required to fit the observed spectra, PL: power law, BB: blackbody, (3) Radius of the spot obtained from the blackbody fit $R_{\rm bb}$, (4) Surface temperature $T_s$, (5) Surface magnetic field strength $B_s$, (6) $b = A_{\rm dp} / A_{\rm bb} = B_s / B_d$, $A_{\rm dp}$ - conventional polar cap area, $A_{\rm bb}$ - actual polar cap area, (7) Bolometric luminosity of blackbody component $L_{\rm BB}$, (8) Bolometric efficiency $\xi_{_{\rm BB}}$, (9) Maximum nonthermal luminosity $L_{\rm NT}^{^{\rm max}}$, (10) Maximum nonthermal X-ray efficiency $\xi_{_{\rm NT}}^{^{\rm max}}$, (11) Best estimate of pulsar age or spin down age, (12) References, (13) Number of the pulsar. Nonthermal luminosity and efficiency were calculated in the $0.1 -10 \, {\rm keV}$ band. The maximum value was calculated with the assumption that the X-ray nonthermal radiation is isotropic. Pulsars are sorted by $b$ parameter (6). \label{tab:x-ray_thermal} }
    \begin{center}
    \begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|}
        \multicolumn{12}{c}{} \\
        \hline
        & & & & & & & & & & & \\
        Name   &   Spectrum   &   $R_{\rm bb}$   &   $T_s$   &   $B_s$   &  $b$   &   $\log L_{\rm BB}$   &   $\log \xi_{_{\rm BB}}$   &  $\log L_{\rm X}$   &   $\log \xi_{_{\rm NT}}^{^{\rm max}}$   &   Ref.   &   No.   \\
        &   &   &   {\scriptsize $\left ( 10^{6}{\rm K} \right )$}   & {\scriptsize $\left (10^{14}{\rm G} \right )$}   &   &  {\scriptsize $\left ( {\rm erg \, s^{-1}} \right )$}   &    &  {\scriptsize $\left ( {\rm erg \, s^{-1}} \right )$}   &    &  & \\
        \hline
        \hline
"""

    end_table = r"""
        & & & & & & & & & & & \\
        \hline
        \hline
  \end{tabular}
  \end{center}
\end{table*}
"""

    body = ' '
    num, i = 0, 0

    for p in pulsars:
        psr_name = p.name.replace('-', '--')
        ca = p.calculations.get(num=0)
        if ca.b > 1.:
            psr_name = '{\color{red}' + psr_name + '}'
        print p.name
        #  surface magnetic field strength
        try:
            if ca.b > 1.:
                b14_s = '$%s^{+%s}_{-%s}$'%(float_str(ca.b_14, digit=3), float_str(ca.b_14_plus, digit=3), float_str(ca.b_14_minus, digit=3))
            else:
                b14_s = '--'
        except TypeError:
            b14_s = '--'
        # citation field (all articles)
        articles = p.xray_articles.all()
        cite = get_cite(articles)
        # fits
        fits = XrayFit.objects.filter(ordinal__gt=0, xrayarticle__in=articles)
        bb_comps = XrayComponent.objects.filter(spec_type='BB', xrayfit__in=fits).order_by('r')
        pl_comps = XrayComponent.objects.filter(spec_type='PL', xrayfit__in=fits)
        #articles_ord = p.xray_articles.filter(fits__ordinal__gt=0).distinct()
        #articles_ord.filter.
        try:
            log_lnth, log_xinth, log_xinth2 = get_lum(pl_comps[0], ca)
        except IndexError:
            print 'Warning no PL component'
            log_lnth, log_xinth = '--', '--'

        # space every X records
        if num % 5 == 0:
            body += '& & & & & & & & & & & \\\\\n'
        num += 1
        # add record
        for i, bb_co in enumerate(bb_comps):
            rad = format_radius(bb_co)
            temp = format_temperature(bb_co)
            log_lth, log_xith, tmp = get_lum(bb_co, ca)
            # find fit
            fit = fits.get(components=bb_co)
            if i == 0:
                # create record here
                record = ('%s   &   {\scriptsize %s}    &    %s   &    %s   &  %s   &   $%s$   &    %s   &   %s   &   %s   &   %s   &  %s  &  %d  \\\\\n'%(psr_name, fit.spectrum, rad, temp, b14_s, float_str(ca.b, digit=4), log_lth, log_xith, log_lnth, log_xinth, cite, fits[0].ordinal))
                record = replace_e(record)
            else:
                record = ('------   &   {\scriptsize %s}   &    %s   &    %s   &   &   &   %s   &   %s   &    &   &   &  \\\\\n' % (fit.spectrum, rad, temp, log_lth, log_xith))
                record = replace_e(record)
                pass
            body = body + record

    res =  start_table + body + end_table

    f = open(os.path.join(MEDIA_ROOT, 'database/latex/table_bb.tex'), 'w')
    for line in res:
        f.write(line)
    f.close()
    try:
        copyfile(os.path.join(MEDIA_ROOT,'database/latex/table_bb.tex'), '/home/aszary/work/1_x-ray/includes/table_bb.tex')
    except IOError:
        print 'Warning: table_bb.tex copy error'
    return res


def table_psrs(pulsars):

    start_float =r"""
\begin{table*}
    \caption[Parameters of rotation powered normal pulsars with detected X-ray radiation]{Parameters of rotation powered normal pulsars with detected X-ray radiation. The individual columns are as follows: (1) Pulsar name, (2) Barycentric period $P$ of the pulsar, (3) Time derivative of barycentric period $\dot{P}$, (4) Canonical value of the dipolar magnetic field $B_{d}$ at poles, (5) Spin down energy loss rate $L_{\rm SD}$ (spin-down luminosity), (6) Dispersion measure $DM$, (7) Best estimate of pulsar
        distance $D$ (used in all calculations), (8) Best estimate of pulsar age or spin down age $\tau=P/\left(2\dot{P}\right)$, (9) Pulsar number (used in figures). Parameters of radio pulsar have been taken from the ATNF catalog.\label{tab:pulsars}}
    \begin{center}
    \begin{tabular}{|l|c|c|c|c|c|c|c|c|}
        \multicolumn{9}{c}{} \\
        \hline
        & & & & & & & & \\
        Name    &   $P$   &   $\dot{P}$   &   $B_d$   &  $\log L_{\rm SD}$  &   $DM$   &   $D$   &   $\tau$  &   No.  \\
         &   {\scriptsize $\left ( {\rm s} \right )$}   &   {\scriptsize $\left ( 10^{-15} \right )$}   &   {\scriptsize $\left ( 10^{12}{\rm G} \right )$}   &   {\scriptsize $\left ( {\rm erg \, s^{-1}} \right )$}   &   {\scriptsize $\left ( {\rm cm^{-3}\,pc} \right )$}   &   {\scriptsize $\left ({\rm kpc} \right )$}   &   &  \\
        & & & & & & & & \\
        \hline
        \hline
            """

    end_float = r"""
      & & & & & & & & \\
      \hline
      \hline
  \end{tabular}
  \end{center}
\end{table*}
"""
    i = 0
    body = ' '
    for p in pulsars:
        calc = p.calculations.get(num=0)
        ad = p.additionals.get(num=0)
        age = get_age(ad)
        fits = XrayFit.objects.filter(psr_id=p, ordinal__isnull=False)
        fit = fits[0]

        # new record
        psr_name = p.name.replace('-', '--')
        if calc.b > 1.:
            psr_name = '{\color{red}' + psr_name + '}'
        record = r"""
        %s  &   $%.3f$  &  %s  &  %s  &   $%.2f$  &  %s  &  %s  &  %s &  %d  \\""" % (psr_name, p.p0, float_str(p.p1*1e15), float_str(calc.bsurf2/1e12), log10(p.edot), float_str(p.dm, digit=3), float_str(p.dist, digit=3), age, fit.ordinal)
        record = replace_e(record)
        if i % 10 == 0:
            record = r'''
        & & & & & & & & \\
            ''' + record
        body = body + record
        i += 1
    res = start_float + body + end_float

    f = open(os.path.join(MEDIA_ROOT, 'database/latex/table_psrs.tex'), 'w')
    for line in res:
        f.write(line)
    f.close()
    try:
        copyfile(os.path.join(MEDIA_ROOT, 'database/latex/table_psrs.tex'), '/home/aszary/work/1_x-ray/includes/table_psrs.tex')
    except IOError:
        print 'Warning: table_psrs.tex copy error'
    return res


def table_pl(pulsars):
    start_table =r"""
\begin{table*}
    \caption[Observed spectral properties of rotation-powered pulsars with X-ray spectrum showing the nonthermal component]{Observed spectral properties of rotation-powered pulsars with X-ray spectrum showing the nonthermal (power-law) component. The individual columns are as follows: (1) Pulsar name, (2) Additional information, (3) Spectral components required to fit the observed spectra, PL: power law, BB: blackbody, (4) Pulse phase average photon index, (5) Maximum nonthermal luminosity $L_{\rm NT}$, (6) Maximum nonthermal X-ray efficiency $\xi_{_{\rm NT}}^{^{\rm max}}$, (7) Minimum nonthermal X-ray efficiency $\xi_{_{\rm NT}}^{^{\rm min}}$, (8) Total thermal luminosity $L_{\rm BB}$, (9) Thermal efficiency $\xi_{_{\rm BB}}$, (10) References, (11) Number of the pulsar. Both nonthermal luminosity and efficiencies were calculated in the $0.1 -10 \, {\rm keV}$ band. The maximum value was calculated with the assumption that the X-ray radiation is isotropic while the minimum value was calculated assuming strong angular anisotropy of the radiation ($\xi_{_{\rm NT}}^{^{\rm min}} \approx 1/4\pi \cdot \xi_{_{\rm NT}}^{^{\rm max}} $). Pulsars are sorted by nonthermal X-ray luminosity (5). \label{tab:x-ray_nonthermal}}
    \begin{center}
    \begin{tabular}{|l|c|c|c|c|c|c|c|c||}
        %\multicolumn{9}{c}{} \\
        \hline
        & & & & & & & & \\
        Name    &   Comment   &   Spectrum   &   Photon-Index   &   $\log L_{\rm NT}$   &  $\log \xi_{_{\rm NT}}^{^{\rm max}}$  &   $\log \xi_{_{\rm NT}}^{^{\rm min}}$  &  Ref.   &   No.  \\
        & & & &   {\scriptsize $\left ( {\rm erg \, s^{-1}} \right )$}   &   &   &   {\scriptsize $\left ( {\rm erg \, s^{-1}} \right )$}   & \\
        \hline
        \hline
"""

    end_table = r"""
      & & & & & & & &\\
      \hline
      \hline
  \end{tabular}
  \end{center}
\end{table*}
"""
    num = 0
    body = ' '
    for p in pulsars:
        psr_name = p.name.replace('-', '--')
        ca = p.calculations.get(num=0)
        if ca.b > 1.:
            psr_name = '{\color{red}' + psr_name + '}'
        print p.name
        # citation field (all articles)
        articles = p.xray_articles.all()
        cite = get_cite(articles)
        # fits
        fits = XrayFit.objects.filter(ordinal__gt=0, xrayarticle__in=articles)
        bb_comps = XrayComponent.objects.filter(spec_type='BB',
                                                xrayfit__in=fits).order_by('r')
        pl_comps = XrayComponent.objects.filter(psr_id=p, spec_type='PL',
                                                  xrayfit__ordinal__gt=0)
        print pl_comps
        # space every X records
        if num % 500 == 0:
            body += '& & & & & & & & \\\\\n'
        num += 1
        # add record
        for i, pl_co in enumerate(pl_comps):
            fit = fits.get(components=pl_co)
            # get pls
            try:
                pl_str = '$%.2f^{+%.2f}_{-%.2f}$' % (pl_co.pl,
                    pl_co.pl_plus, pl_co.pl_minus)
            except TypeError:
                pl_str = '--'
            # new record
            #print (psr_name, p.comment, fit.spectrum, pl_co.pl,
            #    pl_co.pl_plus, pl_co.pl_minus, pl_co.lum,
            #    pl_co.lum, pl_co.lum,
            #    cite, fit.ordinal)
            l1, xi1, xi2 = get_lum(pl_co, ca)
            record = "%s   &   %s   &   %s   &   %s   &   %s   &  %s   &   %s   &   %s   &   %d  \\\\ \n" % (psr_name, p.comment, fit.spectrum,  pl_str, l1, xi1, xi2, cite, fit.ordinal)
            record = replace_e(record)
            body = body + record
    res = start_table + body + end_table

    f = open(os.path.join(MEDIA_ROOT, 'database/latex/table_pl.tex'), 'w')
    for line in res:
        f.write(line)
    f.close()
    try:
        copyfile(os.path.join(MEDIA_ROOT, 'database/latex/table_pl.tex'), '/home/aszary/work/1_x-ray/includes/table_pl.tex')
    except IOError:
        print 'Warning: table_pl.tex copy error'
    return res

def custom(pulsars):
    res = ''
    psr_radio_ = []
    radio_eff_ = []
    for i, p in enumerate(pulsars):
        try:
            radio = radio_lum(p)
        except ZeroDivisionError:
            radio = 0.
        xray = 0.
        comp = XrayComponent.objects.filter(psr_id=p).filter(xrayfit__ordinal__gt=0)
        for c in comp:
            try:
                xray += c.lum
            except TypeError:
                pass

        if radio > 0. and xray > 0.:
            if radio > xray:
                res += r'%s   %s    %s<br />' % (p.name, p.raj_err, p.decj_err)
            try:
                #print radio/p.edot, xray/p.edot
                radio_eff_.append(radio/p.edot)
                res += r'%s  &nbsp;&nbsp;&nbsp;&nbsp; xi_radio = %.1e  &nbsp;&nbsp;&nbsp;  xi_xray = %.1e<br />' % (p.name, radio/p.edot, xray/p.edot)
            except:
                pass
        if radio > 0.:
            psr_radio_.append(p)

    max_radio = max(radio_eff_)
    print max_radio

    radio_high_eff_ = []
    dist_ = []
    eff_ = []
    lum_ = []

    for p in psr_radio_:
        radio = radio_lum(p)
        try:
            eff = radio / p.edot
            if eff > max_radio and p.dist<5.:
                radio_high_eff_.append(p)
                dist_.append(p.dist)
                eff_.append(eff)
                lum_.append(radio)
        except:
            pass

    dist_hist(dist_, eff_, lum_)


    '''
    num = 0
    for i,p in enumerate(pulsars):
        #res += '%s \n' % p.name
        res += '%s,%s\n' % (p.raj, p.decj)
        if i%500 == 0 and i > 0:
            num += 1
    f = open(os.path.join(MEDIA_ROOT, 'database/latex/chandra.csv'), 'w')
    for line in res:
        f.write(line)
    f.close()
    '''
    return res

def print_citealiases(psrs):
    # defcitealias
    citalias = []
    for psr in psrs:
        # citation field (all articles)
        articles = psr.xray_articles.all()
        res = get_citealias(articles)
        citalias += res
    citalias = remove_duplicates(citalias)
    citalias.sort()
    for ci in citalias: print ci

def get_age(ad):
    #age in kyrs or Myrs
    if ad.best_age / 1e3 > 1000:
        age = ad.best_age / 1e6
        age_str = float_str(age, digit=3)+' Myr'
    else:
        age = ad.best_age / 1e3
        age_str = float_str(age, digit=3)+' kyr'
    return age_str


def get_citealias(articles):
    res = []
    for art in articles:
        cite = art.cite.replace('cite', 'defcitealias')
        ye = cite.find('{')
        year = cite[ye+3:ye+5]
        na = cite.find('_')
        name = cite[na+1:na+3]
        res.append(cite + '{'+ name + year + '}')
    return res


def get_cite(articles):
    res = ''
    for art in articles:
        res += ' '+art.cite
    res = res.replace('cite', 'citetalias')
    return res

def get_lum(co, calc):
    log_l = '--'
    log_xi = '--'
    log_xi2 = '--'
    try:
        log_l= '$%.2f$'%log10(co.lum)
        log_xi = '$%.2f$'%log10(co.lum / calc.l_sd)
        log_xi2 = '$%.2f$'%log10(co.lum / calc.l_sd / (4. * pi))
    except TypeError:
        print 'Warning no luminosity  data'
    return log_l, log_xi, log_xi2

def format_radius(co):
    if co.r is not None:
        # radius in meters or in km
        if co.r / 1e2 > 1000.:
            r_st = r"$%s" % float_str(co.r / 1e5, digit=3)
            try:
                rp_st = r"^{+%s}" % float_str(co.r_plus / 1e5, digit=3)
            except TypeError:
                rp_st = r'^{}'
            try:
                rm_st = r"_{-%s}\,{\rm km}$" % float_str(co.r_minus / 1e5,
                                                           digit=3)
            except TypeError:
                rm_st = r'_{}\,{\rm km}$'
        else:
            r_st = r"$%s" % float_str(co.r / 1e2, digit=3)
            try:
                rp_st = r"^{+%s}" % float_str(co.r_plus / 1e2, digit=3)
            except TypeError:
                rp_st = r'^{}'
            try:
                rm_st = r"_{-%s}\,{\rm m}$" % float_str(co.r_minus / 1e2,
                                                          digit=3)
            except TypeError:
                rm_st = r'_{}\,{\rm m}$'
        radius_str = r_st + rp_st + rm_st
    else:
        radius_str = '--'
    return radius_str

def format_temperature(co):
    t6_s= r"$%s" % float_str(co.t / 1e6, digit=3)
    try:
        t6_plus = r"^{+%s}" % float_str(co.t_plus / 1e6, digit=3)
    except TypeError:
        print 'Warning no T_6 (+ err.)'
        t6_plus = r'^{}'
    try:
        t6_minus = r"_{-%s}$" % float_str(co.t_minus / 1e6, digit=3)
    except TypeError:
        print 'Warning no T_6 (- err.)'
        t6_minus = r'_{}$'
    return t6_s + t6_plus + t6_minus

def float_str(num, digit=4):
    if num is None:
        return '--'
    num_str = '%.9f'%num
    dot = num_str.find('.')
    if digit < dot:
        return float_str(num, digit=digit+1)
    elif dot <= digit - 1:
        return num_str[:digit+1]
    else:
        return num_str[:digit]

def replace_e(body):
    # to avoid Be-star
    start_body = ''
    # replace e-10 with 10^{-10}
    index = 1
    while index > 0:
        # get power
        index = body.find("e-")
        if index > 0:
            power = body[index+2] + body[index+3]
            try:
                body = body.replace('e-%s'%power, r' \times 10^{-%d}'%int(power),1)
            except:
                start_body = body[0:index+2]
                body = body[index+2:]
    # replace e+10 with 10^{10}
    index = 1
    while index > 0:
        # get power
        index=body.find("e+")
        if index > 0:
            power = body[index+2]+body[index+3]
            try:
                body = body.replace('e+%s'%power, r' \times 10^{%d}'%int(power), 1)
            except:
                start_body = body[:index+2]
                body = body[index+2:]
    body = start_body + body
    return body

def remove_duplicates(seq, idfun=None):
   """
   order preserving from http://www.peterbe.com/plog/uniqifiers-benchmark
   """
   if idfun is None:
       def idfun(x): return x
   seen = {}
   result = []
   for item in seq:
       marker = idfun(item)
       # in old Python versions:
       # if seen.has_key(marker)
       # but in new ones:
       if marker in seen: continue
       seen[marker] = 1
       result.append(item)
   return result
