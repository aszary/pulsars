__author__ = 'aszary'
import os
from decimal import Decimal

from urllib import urlopen
from django.core.exceptions import ObjectDoesNotExist

from models import Pulsar


MEDIA_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'media')


def get_page_old():
    """ old query
    """
    url = 'http://www.atnf.csiro.au/research/pulsar/psrcat/proc_form.php?Name=Name&JName=JName&RaJ=RaJ&DecJ=DecJ&PMRA=PMRA&PMDec=PMDec&PX=PX&PosEpoch=PosEpoch&ELong=ELong&ELat=ELat&PMELong=PMELong&PMELat=PMELat&GL=GL&GB=GB&RaJD=RaJD&DecJD=DecJD&P0=P0&P1=P1&F0=F0&F1=F1&F2=F2&F3=F3&PEpoch=PEpoch&DM=DM&DM1=DM1&RM=RM&W50=W50&W10=W10&Tau_sc=Tau_sc&S400=S400&S1400=S1400&SPINDX=SPINDX&Binary=Binary&T0=T0&PB=PB&A1=A1&OM=OM&Ecc=Ecc&Tasc=Tasc&Eps1=Eps1&Eps2=Eps2&Minmass=Minmass&Medmass=Medmass&Dist=Dist&Dist_DM=Dist_DM&DMsinb=DMsinb&ZZ=ZZ&XX=XX&YY=YY&Assoc=Assoc&Survey=Survey&OSurvey=OSurvey&Date=Date&Type=Type&NGlt=NGlt&R_lum=R_lum&R_lum14=R_lum14&Age=Age&Bsurf=Bsurf&Edot=Edot&Edotd2=Edotd2&PMtot=PMtot&VTrans=VTrans&P1_i=P1_i&Age_i=Age_i&Bsurf_i=Bsurf_i&B_LC=B_LC&startUserDefined=true&c1_val=&c2_val=&c3_val=&c4_val=&sort_attr=jname&sort_order=asc&condition=&pulsar_names=&ephemeris=short&coords_unit=raj%2Fdecj&radius=&coords_1=&coords_2=&style=Long+with+errors&no_value=0.0&fsize=3&x_axis=p0&x_scale=linear&y_axis=p1&y_scale=linear&state=query&table_bottom.x=47&table_bottom.y=34'
    page = urlopen(url)
    s = page.read()
    page.close()
    f = open(os.path.join(MEDIA_PATH, 'database/atnf.html'), 'w')
    f.write(s)
    f.close()


def get_page():
    """ new query: 2013-05-14
    """
    url = 'http://www.atnf.csiro.au/people/pulsar/psrcat/proc_form.php?table_top.x=59&table_top.y=34&Name=Name&JName=JName&RaJ=RaJ&DecJ=DecJ&PMRA=PMRA&PMDec=PMDec&PX=PX&PosEpoch=PosEpoch&ELong=ELong&ELat=ELat&PMELong=PMELong&PMELat=PMELat&GL=GL&GB=GB&RaJD=RaJD&DecJD=DecJD&P0=P0&P1=P1&F0=F0&F1=F1&F2=F2&F3=F3&PEpoch=PEpoch&DM=DM&DM1=DM1&RM=RM&W50=W50&W10=W10&Units=Units&Tau_sc=Tau_sc&S400=S400&S1400=S1400&S2000=S2000&Binary=Binary&T0=T0&PB=PB&A1=A1&OM=OM&Ecc=Ecc&Tasc=Tasc&Eps1=Eps1&Eps2=Eps2&Minmass=Minmass&Medmass=Medmass&Bincomp=Bincomp&Dist=Dist&Dist_DM=Dist_DM&DMsinb=DMsinb&ZZ=ZZ&XX=XX&YY=YY&Assoc=Assoc&Survey=Survey&OSurvey=OSurvey&Date=Date&Type=Type&NGlt=NGlt&R_lum=R_lum&R_lum14=R_lum14&Age=Age&Bsurf=Bsurf&Edot=Edot&Edotd2=Edotd2&PMtot=PMtot&VTrans=VTrans&P1_i=P1_i&Age_i=Age_i&Bsurf_i=Bsurf_i&B_LC=B_LC&startUserDefined=true&c1_val=&c2_val=&c3_val=&c4_val=&sort_attr=jname&sort_order=asc&condition=&pulsar_names=&ephemeris=short&coords_unit=raj%2Fdecj&radius=&coords_1=&coords_2=&style=Long+with+errors&no_value=*&fsize=3&x_axis=&x_scale=linear&y_axis=&y_scale=linear&state=query'
    page = urlopen(url)
    s = page.read()
    page.close()
    f = open(os.path.join(MEDIA_PATH, 'database/atnf.html'), 'w')
    f.write(s)
    f.close()


def parse_page():
    # read page
    f = open(os.path.join(MEDIA_PATH, 'database/atnf.html'), 'r')
    lines = f.readlines()
    f.close()

    # find lines with numbers at the beginning
    line_ind = []
    nums = []
    for i in xrange(len(lines)):
        try:
            # ATNF index
            nums.append(int(lines[i][:5]))
            line_ind.append(i)
        except ValueError:
            pass
    # parse records
    for ii, i in enumerate(line_ind):
        res = lines[i].split()
        try:
            p = Pulsar.objects.get(name=res[1])
            print 'ATNF Id = %d  Name = %s  (updating existing record...)' % (nums[ii], res[1])
        except ObjectDoesNotExist:
            p = Pulsar(name=res[1])
            print 'ATNF Id = %d  Name = %s  (creating new record...)' % (nums[ii], res[1])
        # set pulsar parameters
        record_from_list(p, res)
        p.save()


def record_from_list(p, res):
    p.name = res[1]
    p.jname = res[2]
    p.raj = res[3]
    p.raj_err = to_float(res[4])
    p.decj = res[5]
    p.decj_err = to_float(res[6])
    p.pmra = to_float(res[7])
    p.pmra_err = to_float(res[8])
    p.pmdec = to_float(res[9])
    p.pmdec_err = to_float(res[10])
    p.px = to_float(res[11])
    p.px_err = to_float(res[12])
    p.posepoch = to_float(res[13])
    p.elong = to_float(res[14])
    p.elong_err = to_float(res[15])
    p.elat = to_float(res[16])
    p.elat_err = to_float(res[17])
    p.pmelong = to_float(res[18])
    p.pmelong_err = to_float(res[19])
    p.pmelat = to_float(res[20])
    p.pmelat_err = to_float(res[21])
    p.gl = to_float(res[22])
    p.gb = to_float(res[23])
    p.rajd = to_float(res[24])
    p.decjd = to_float(res[25])

    try:
        p.p0 = Decimal(res[26])
    except:
        p.p0 = Decimal('0')
    p.p0_err = to_float(res[27])
    p.p1 = to_float(res[28])
    p.p1_err = to_float(res[29])
    p.f0 = to_float(res[30])
    p.f0_err = to_float(res[31])
    p.f1 = to_float(res[32])
    p.f1_err = to_float(res[33])
    p.f2 = to_float(res[34])
    p.f2_err = to_float(res[35])
    p.f3 = to_float(res[36])
    p.f3_err = to_float(res[37])
    p.pepoch = to_float(res[38])
    p.dm = to_float(res[39])
    p.dm_err = to_float(res[40])
    p.dm1 = to_float(res[41])
    p.dm1_err = to_float(res[42])
    p.rm = to_float(res[43])
    p.rm_err = to_float(res[44])
    p.w50 = to_float(res[45])
    p.w50_err = to_float(res[46])
    p.w10 = to_float(res[47])
    p.w10_err = to_float(res[48])
    p.units = res[49]
    p.tau_sc = to_float(res[50])
    p.tau_sc_err = to_float(res[51])
    p.s400 = to_float(res[52])
    p.s400_err = to_float(res[53])
    p.s1400 = to_float(res[54])
    p.s1400_err = to_float(res[55])
    p.s2000 = to_float(res[56])
    p.s2000_err = to_float(res[57])

    p.binary = res[58]
    p.t0 = to_float(res[59])
    p.t0_err = to_float(res[60])
    p.pb = to_float(res[61])
    p.pb_err = to_float(res[62])
    p.a1 = to_float(res[63])
    p.a1_err = to_float(res[64])
    p.om = to_float(res[65])
    p.om_err = to_float(res[66])
    p.ecc = to_float(res[67])
    p.ecc_err = to_float(res[68])
    p.tasc = to_float(res[69])
    p.tasc_err = to_float(res[70])
    p.eps1 = to_float(res[71])
    p.eps1_err = to_float(res[72])
    p.eps2 = to_float(res[73])
    p.eps2_err = to_float(res[74])
    p.minmass = to_float(res[75])
    p.medmass = to_float(res[76])
    p.bincomp = res[77]

    p.dist = to_float(res[78])
    p.dist_dm = to_float(res[79])
    p.dmsinb = to_float(res[80])
    p.zz = to_float(res[81])
    p.xx = to_float(res[82])
    p.yy = to_float(res[83])

    p.assoc = res[84]
    p.survey = res[85]
    p.osurvey = str(res[86])
    p.date = to_int(res[87])
    p.type = res[88]
    p.nglt = to_int(res[89])

    p.r_lum = to_float(res[90])
    p.r_lum14 = to_float(res[91])
    p.age = to_float(res[92])
    p.bsurf = to_float(res[93])
    p.edot = to_float(res[94])
    p.edotd2 = to_float(res[95])
    p.pmtot = to_float(res[96])
    p.vtrans = to_float(res[97])
    p.p1_i = to_float(res[98])
    p.age_i = to_float(res[99])
    p.bsurf_i = to_float(res[100])
    p.edot_i = to_float(res[101])
    p.b_lc = to_float(res[102])

    p.simbad_link = "http://simbad.u-strasbg.fr/simbad/sim-id?Ident=PSR+" + p.name.replace("+", "%2B").replace("_", "+") + "&NbIdent=1&Radius=2&Radius.unit=arcmin&submit=submit+id"


def to_float(str_):
    if str_.startswith('nan'):
        return 0.
    try:
        return float(str_)
    except ValueError:
        return 0.


def to_int(str_):
    try:
        return int(str_)
    except ValueError:
        return 0


def parse_malov():
    f = open(os.path.join(MEDIA_PATH, 'database/malov_2007.tsv'), 'r')
    lines = f.readlines()
    for line in lines:
        if not line.startswith('#'):
            res = line.split(';')
            name = res[3].strip()
            lum_pow = float(res[4])
            try:
                pulsar = Pulsar.objects.get(name=name)
            except ObjectDoesNotExist:
                pulsar = Pulsar.objects.get(jname=name)
            pulsar.lum_malov = 10 ** lum_pow
            print pulsar
            pulsar.save()
    f.close()
