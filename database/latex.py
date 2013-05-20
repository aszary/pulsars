from math import log10
from pulsars.settings import MEDIA_ROOT
from models import XrayComponent, XrayFit

def table_bb_nondipolar(pulsars):

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

    for p in pulsars:
        psr_name = p.Name.replace('-', '--')
        ca = p.calculations.get(num=0)
        if ca.b > 1.:
            psr_name = '{\color{red}' + psr_name + '}'
        print p.Name
        #  surface magnetic field strength
        try:
            if ca.b > 1.:
                b14_s = '$%.2f^{+%.2f}_{-%.2f}$'%(ca.b_14, ca.b_14_plus,
                                              ca.b_14_minus)
            else:
                b14_s = '--'
        except TypeError:
            b14_s = '--'
        # citation field (all articles)
        articles = p.xray_articles.all()
        cite = get_cite(articles)
        # fits
        fits = XrayFit.objects.filter(ordinal__gt=0, xrayarticle__in=articles)
        bb_comps = XrayComponent.objects.filter(spec_type='BB',
                                                xrayfit__in=fits).order_by('r')
        pl_comps = XrayComponent.objects.filter(spec_type='PL',
                                                  xrayfit__in=fits)
        #articles_ord = p.xray_articles.filter(fits__ordinal__gt=0).distinct()
        #articles_ord.filter.
        try:
            log_lnth, log_xinth = get_lum(pl_comps[0], ca)
        except IndexError:
            print 'Warning no PL component'
            log_lnth, log_xinth = '--', '--'

        for i, bb_co in enumerate(bb_comps):
            rad = format_radius(bb_co)
            temp = format_temperature(bb_co)
            log_lth, log_xith = get_lum(bb_co, ca)
            if i ==0:
                # create record here
                record = r"""
    %s   &   {\scriptsize %s}    &    %s   &    %s   &  %s   &   %s   &    %s   &   %s   &   %s   &   %s   &  %s  &  %d  \\"""\
                        %(psr_name, fits[0].spectrum, rad, temp,
                          b14_s, float_str(ca.b, digit=3), log_lth, log_xith,
                          log_lnth, log_xinth, cite, fits[0].ordinal)
                record = replace_e(record)
            else:
                record = r"""
    ------   &      &    %s   &    %s   &   &   &    %s   &   %s   &    &   &   &  \\"""\
                        %( rad, temp, log_lth, log_xith)
                record = replace_e(record)
                pass

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

def get_lum(co, calc):
    log_l = '--'
    log_xi = '--'
    try:
        log_l= '$%.2f$'%log10(co.lum)
        log_xi = '$%.2f$'%log10(co.lum / calc.l_sd)
    except TypeError:
        print 'Warning no luminosity  data'
    return log_l, log_xi

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