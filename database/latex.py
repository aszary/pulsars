from math import log10
from pulsars.settings import MEDIA_ROOT

def table_bb_nondipolar(pulsars, fits, calcs, comps, artics_all, artics_sam):

    start_table =r"""
\begin{table*}
    \caption[Observed spectral properties of X-ray detected rotation-powered
    pulsars with blackbody spectrum component]{Observed spectral properties of
    X-ray detected rotation-powered
    pulsars with blackbody spectrum component. The individual columns are
    as follows: (1) Pulsar name, (2) Spectral components required to fit the
    observed
    spectra, PL: power law, BB: blackbody, (3) Radius of the spot obtained
    from the blackbody fit $R_{\rm bb}$, (4) Surface temperature $T_s$,
    (5) Surface magnetic field strength $B_s$,
    (6) $b = A_{\rm dp} / A_{\rm bb} = B_s / B_d$, $A_{\rm dp}$ - conventional
    polar
    cap area, $A_{\rm bb}$ - actual polar cap area, (7) Bolometric luminosity
    of blackbody component $L_{\rm BB}$, (8) Bolometric efficiency
    $\xi_{_{\rm BB}}$,
    (9) Maximum nonthermal luminosity $L_{\rm NT}^{^{\rm max}}$,
    (10) Maximum nonthermal X-ray efficiency $\xi_{_{\rm NT}}^{^{\rm max}}$,
    (11) Best estimate of pulsar age or spin down age,
    (12) References, (13) Number of the pulsar.
    Nonthermal luminosity and efficiency were calculated in the $0.1 -10 \,
    {\rm keV}$ band.
    The maximum value was calculated with the assumption that the X-ray
    nonthermal radiation is isotropic.
    Pulsars are sorted by $b$ parameter (6).
        \label{tab:x-ray_thermal}
    }
    \begin{center}
    \begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|}
        \multicolumn{12}{c}{} \\
        \hline
        & & & & & & & & & & & \\
        Name   &   Spectrum   &   $R_{\rm bb}$   &   $T_s$   &   $B_s$   &
            $b$   &   $\log L_{\rm BB}$   &   $\log \xi_{_{\rm BB}}$   &
            $\log L_{\rm X}$   &   $\log \xi_{_{\rm NT}}^{^{\rm max}}$   &
            Ref.   &   No.   \\
        &   &   &   {\scriptsize $\left ( 10^{6}{\rm K} \right )$}   &
            {\scriptsize $\left (10^{14}{\rm G} \right )$}   &   &
            {\scriptsize $\left ( {\rm erg \, s^{-1}} \right )$}   &    &
            {\scriptsize $\left ( {\rm erg \, s^{-1}} \right )$}   &    &  & \\
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

    # sorted by b in calc
    for ca in calcs:
        # pulsar
        p = pulsars.get(id = ca.psr_id_id)
        psr_name = p.Name.replace('-', '--')
        if ca.b > 1.:
            psr_name = '{\color{red}' + psr_name + '}'
        print p.Name
        #  surface magnetic field strength
        try:
            b14_s = '$%.2f^{+%.2f}_{-%.2f}$'%(ca.b_14, ca.b_14_plus,
                                              ca.b_14_minus)
        except TypeError:
            b14_s = '--'
        # citation field
        arts = artics_all.filter(psr_id=p.id)
        cite = get_cite(arts)
        # articles with ordinal and BB
        arts = artics_sam.filter(psr_id=p.id)
        for art in arts:
            # all fits with ordinal
            fitss =  fits.filter(article_id=art.id)
            for fit in fitss:
                # nonthermal and thermal data
                log_nth, log_xinth = get_lum(comps, fit, ca,
                                                    spec_type='PL')
                log_th, log_xith = get_lum(comps, fit, ca,
                                                    spec_type='BB')
                rads, temps = get_components_data(comps, fit)
                for i in xrange(len(rads)):
                    # create record here
                    record = r"""
    %s   &   {\scriptsize %s}    &    %s   &    %s   &  %s   &   %s   &    %s   &   %s   &   %s   &   %s   &  %s  &  %d  \\"""\
                        %(psr_name, fit.spectrum, rads[i], temps[i],
                          b14_s, float_str(ca.b, digit=3), log_th, log_xith,
                          log_nth, log_xinth, cite, fit.ordinal)
                    record = replace_e(record)

                    body = body + record
        if num % 10 == 0:
            record = r'''
    & & & & & & & & & & & \\
            ''' + record
        num += 1

    res =  start_table + body + end_table

    f = open(MEDIA_ROOT + 'database/table_bb_nondipolar.tex', 'w')
    for line in res:
        f.write(line)
    f.close()
    return res


def get_cite(articles):
    res = ''
    for art in articles:
        res += ' '+art.cite
    res = res.replace('cite', 'citetalias')
    return res

def get_lum(components, fit, calc, spec_type=None):
    comps = components.filter(fit_id=fit.id, spec_type=spec_type)
    log_l = '--'
    log_xi = '--'
    try:
        log_l= '$%.2f$'%log10(comps[0].lum)
        log_xi = '$%.2f$'%log10(comps[0].lum / calc.l_sd)
    except IndexError:
        print 'Warning no %s component' % spec_type
    except TypeError:
        print 'Warning no luminosity  data for %s component' % spec_type
    return log_l, log_xi

def get_components_data(components, fit):

    comps = components.filter(fit_id=fit.id, spec_type="BB").order_by('r')
    rads = []
    temps = []

    for co in  comps:
        rads.append(format_radius(co))
        temps.append(format_temperature(co))
    return rads, temps

def format_radius(co):
    if co.r is not None:
        # radius in meters or in km
        if co.r / 1e2 > 1000.:
            r_st = r"$%.2f" % (co.r / 1e5)
            try:
                rp_st = r"^{+%.2f}" % (co.r_plus / 1e5)
            except TypeError:
                rp_st = r'^{}'
            try:
                rm_st = r"_{-%.2f}\,{\rm km}$" % (co.r_minus / 1e5)
            except TypeError:
                rm_st = r'_{}\,{\rm km}$'
        else:
            r_st = r"$%.2f" % (co.r / 1e2)
            try:
                rp_st = r"^{+%.2f}" % (co.r_plus / 1e2)
            except TypeError:
                rp_st = r'^{}'
            try:
                rm_st = r"_{-%.2f}\,{\rm m}$" % (co.r_minus / 1e2)
            except TypeError:
                rm_st = r'_{}\,{\rm m}$'
        radius_str = r_st + rp_st + rm_st
    else:
        radius_str = '--'
    return radius_str

def format_temperature(co):
    t6_s= r"$%.2f" % (co.t / 1e6)
    try:
        t6_plus = r"^{+%.2f}" % (co.t_plus / 1e6)
    except TypeError:
        print 'Warning no T_6 (+ err.)'
        t6_plus = r'^{}'
    try:
        t6_minus = r"_{-%.2f}$" % (co.t_minus / 1e6)
    except TypeError:
        print 'Warning no T_6 (- err.)'
        t6_minus = r'_{}$'
    return t6_s + t6_plus + t6_minus


def table_bb_nondipolar_old(pulsars, fits, calcs, comps, artics):

    start_float =r"""
\begin{table*}
    \caption[Observed spectral properties of X-ray detected rotation-powered
    pulsars with blackbody spectrum component]{Observed spectral properties of
    X-ray detected rotation-powered
    pulsars with blackbody spectrum component. The individual columns are
    as follows: (1) Pulsar name, (2) Spectral components required to fit the
    observed
    spectra, PL: power law, BB: blackbody, (3) Radius of the spot obtained
    from the blackbody fit $R_{\rm bb}$, (4) Surface temperature $T_s$,
    (5) Surface magnetic field strength $B_s$,
    (6) $b = A_{\rm dp} / A_{\rm bb} = B_s / B_d$, $A_{\rm dp}$ - conventional
    polar
    cap area, $A_{\rm bb}$ - actual polar cap area, (7) Bolometric luminosity
    of blackbody component $L_{\rm BB}$, (8) Bolometric efficiency
    $\xi_{_{\rm BB}}$,
    (9) Maximum nonthermal luminosity $L_{\rm NT}^{^{\rm max}}$,
    (10) Maximum nonthermal X-ray efficiency $\xi_{_{\rm NT}}^{^{\rm max}}$,
    (11) Best estimate of pulsar age or spin down age,
    (12) References, (13) Number of the pulsar.
    Nonthermal luminosity and efficiency were calculated in the $0.1 -10 \,
    {\rm keV}$ band.
    The maximum value was calculated with the assumption that the X-ray
    nonthermal radiation is isotropic.
    Pulsars are sorted by $b$ parameter (6).
        \label{tab:x-ray_thermal}
    }
    \begin{center}
    \begin{tabular}{|l|c|c|c|c|c|c|c|c|c|c|c|}
        \multicolumn{12}{c}{} \\
        \hline
        & & & & & & & & & & & \\
        Name   &   Spectrum   &   $R_{\rm bb}$   &   $T_s$   &   $B_s$   &
            $b$   &   $\log L_{\rm BB}$   &   $\log \xi_{_{\rm BB}}$   &
            $\log L_{\rm X}$   &   $\log \xi_{_{\rm NT}}^{^{\rm max}}$   &
            Ref.   &   No.   \\
        &   &   &   {\scriptsize $\left ( 10^{6}{\rm K} \right )$}   &
            {\scriptsize $\left (10^{14}{\rm G} \right )$}   &   &
            {\scriptsize $\left ( {\rm erg \, s^{-1}} \right )$}   &    &
            {\scriptsize $\left ( {\rm erg \, s^{-1}} \right )$}   &    &  & \\
        \hline
        \hline
            """

    end_float = r"""
        & & & & & & & & & & & \\
        \hline
        \hline
  \end{tabular}
  \end{center}
\end{table*}
          """

    body = ' '
    num, i = 0, 0
    for i, p in enumerate(pulsars):

        # nonthermal luminositiy
        for co in comps[i]:
            if co.spec_type == 'PL':
                try:
                    log_l = '$%.2f$'%log10(co.lum)
                    log_xi = '$%.2f$'%log10(co.lum / calcs[i].l_sd)
                except:
                    log_l = '--'
                    log_xi = '--'

        # b14
        if calcs[i].b > 1.:
            b_14 = '$%.2f^{+%.2f}_{-%.2f}$'%(calcs[i].b_14, calcs[i].b_14_plus,
                                             calcs[i].b_14_minus)
        else:
            b_14 = '--'
        psr_name = p.Name.replace('-', '--')
        if calcs[i].b > 1.:
            psr_name = '{\color{red}' + psr_name + '}'
        print p.Name

        for co in comps[i]:
             if co.spec_type == 'BB':
                t_6 =  co.t /1e6
                try:
                    t6_plus = co.t_plus / 1e6
                except TypeError:
                    t6_plus = 0.1 * t_6
                try:
                    t6_minus = co.t_minus /1e6
                except:
                    t6_minus = 0.1 * t_6
                if co.r is not None:
                    # radius in meters or in km
                    if co.r / 1e2 > 1000.:
                        r_st = r"$%.2f" % (co.r / 1e5)
                        try:
                            rp_st = r"^{+%.2f}" % (co.r_plus / 1e5)
                        except TypeError:
                            rp_st = r'^{}'
                        try:
                            rm_st = r"_{-%.2f}\,{\rm km}$" % (co.r_minus / 1e5)
                        except TypeError:
                            rp_st = r'_{}\,{\rm km}$'
                    else:
                        r_st = r"$%.2f" % (co.r / 1e2)
                        try:
                            rp_st = r"^{+%.2f}" % (co.r_plus / 1e2)
                        except TypeError:
                            rp_st = r'^{}'
                        try:
                            rm_st = r"_{-%.2f}\,{\rm m}$" % (co.r_minus / 1e2)
                        except TypeError:
                            rp_st = r'_{}\,{\rm m}$'
                    radius_str = r_st + rp_st + rm_st
                else:
                    radius_str = '--'



        # new record
        try:
            record = r"""
    %s   &   {\scriptsize %s}    &    %s   &    $%.1f^{+%.2f}_{-%.2f}$    &  %s   &   %s   &    $%.2f$   &   $%.2f$   &   %s   &   %s   &  %s  &  %d  \\"""\
                %(psr_name, fits[i].spectrum, radius_str,
                  t_6, t6_plus, t6_minus, b_14,
                  float_str(calcs[i].b, digit=3), log10(comps[i][0].lum),
                  log10(comps[i][0].lum / calcs[i].l_sd), log_l, log_xi,
                  artics[i].cite.replace('cite', 'citetalias'),
                  fits[i].ordinal)
            record = replace_e(record)
        except:
            pass
        '''
        if p.l_bol2 > 0.:
            add_rec = (r'        ------ &   &  $%.2f^{+%.0f}_{-%.0f} $km&'
                       r'   $%.1f^{+%.2f}_{-%.2f}$   &    &   &  $%.2f$  &'
                       r'  $%.2f$  &    &   &   \\')%(
                p.r2/1e5, p.r2_plus/1e5, p.r2_minus/1e5, p.t2/1e6,
                p.t2_plus/1e6, p.t2_minus/1e6, log10(p.l_bol2),
                  log10(p.l_bol2/p.l_sd))
            record = record + '\n' + add_rec
        '''
        if num%10 ==0:
            record = r'''
    & & & & & & & & & & & \\
            ''' + record
        num += 1
        body = body + record
        i += 1
    res = start_float + body + end_float

    # defcitealias
    citalias = []
    for art in artics:
        splt = art.cite.split(',')
        for cit in splt:
            #short
            ye = cit.find('{')
            na = cit.find('_')
            short = cit[na+1:na+3]+cit[ye+3:ye+5]
            citalias.append(cit.replace('cite','defcitealias') +\
                    '{'+short + '}')
            citalias[-1] = citalias[-1].strip()
    citalias.sort()
    for ci in citalias: print ci

    f = open(MEDIA_ROOT + 'database/table_bb_nondipolar.tex', 'w')
    for line in res:
        f.write(line)
    f.close()
    return res


def float_str(num, digit=4):
    if num is None:
        return '--'
    if digit == 4:
        if num<0.001:
            return '$%.5f$'%num
        elif num<0.01:
            return '$%.3f$'%num
        elif num<0.1:
            return '$%.3f$'%num
        elif num<1.:
            return '$%.3f$'%num
        elif num<10.:
            return '$%.3f$'%num
        elif num<100.:
            return '$%.2f$'%num
        elif num<1000.:
            return '$%.1f$'%num
        else:
            return '$%.0f$'%num
    elif digit == 3:
        if num==0:
            return '--'
        elif num<0.1:
            return '$%.2f$'%num
        elif num<1.:
            return '$%.2f$'%num
        elif num<10.:
            return '$%.2f$'%num
        elif num<100.:
            return '$%.1f$'%num
        elif num<1000.:
            return '$%.0f$'%num


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