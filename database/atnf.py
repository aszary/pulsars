__author__ = 'aszary'

from urllib import urlopen
from django.core.exceptions import ObjectDoesNotExist
from pulsars.settings import MEDIA_ROOT

from models import Pulsar


def get_page_old():
    """ old query
    """
    url = ('http://www.atnf.csiro.au/research/pulsar/psrcat/proc_form.php?Name'
           '=Name&JName=JName&RaJ=RaJ&DecJ=DecJ&PMRA=PMRA&PMDec=PMDec&PX=PX&Po'
           'sEpoch=PosEpoch&ELong=ELong&ELat=ELat&PMELong=PMELong&PMELat=PMELa'
           't&GL=GL&GB=GB&RaJD=RaJD&DecJD=DecJD&P0=P0&P1=P1&F0=F0&F1=F1&F2=F2&'
           'F3=F3&PEpoch=PEpoch&DM=DM&DM1=DM1&RM=RM&W50=W50&W10=W10&Tau_sc=Ta'
           'u_sc&S400=S400&S1400=S1400&SPINDX=SPINDX&Binary=Binary&T0=T0&PB=PB'
           '&A1=A1&OM=OM&Ecc=Ecc&Tasc=Tasc&Eps1=Eps1&Eps2=Eps2&Minmass=Minmass'
           '&Medmass=Medmass&Dist=Dist&Dist_DM=Dist_DM&DMsinb=DMsinb&ZZ=ZZ&XX='
           'XX&YY=YY&Assoc=Assoc&Survey=Survey&OSurvey=OSurvey&Date=Date&Type='
           'Type&NGlt=NGlt&R_lum=R_lum&R_lum14=R_lum14&Age=Age&Bsurf=Bsurf&Edo'
           't=Edot&Edotd2=Edotd2&PMtot=PMtot&VTrans=VTrans&P1_i=P1_i&Age_i=Age'
           '_i&Bsurf_i=Bsurf_i&B_LC=B_LC&startUserDefined=true&c1_val=&c2_val='
           '&c3_val=&c4_val=&sort_attr=jname&sort_order=asc&condition=&pulsar_'
           'names=&ephemeris=short&coords_unit=raj%2Fdecj&radius=&coords_1=&co'
           'ords_2=&style=Long+with+errors&no_value=0.0&fsize=3&x_axis=p0&x_sc'
           'ale=linear&y_axis=p1&y_scale=linear&state=query&table_bottom.x=47&'
           'table_bottom.y=34')
    page = urlopen(url)
    s = page.read()
    page.close()
    f = open(MEDIA_ROOT+'database/atnf.html', 'w')
    f.write(s)
    f.close()


def get_page():
    """ new query: 2013-05-14
    """
    url = ('http://www.atnf.csiro.au/people/pulsar/psrcat/proc_form.php?table_'
           'top.x=59&table_top.y=34&Name=Name&JName=JName&RaJ=RaJ&DecJ=DecJ&PM'
           'RA=PMRA&PMDec=PMDec&PX=PX&PosEpoch=PosEpoch&ELong=ELong&ELat=ELat&'
           'PMELong=PMELong&PMELat=PMELat&GL=GL&GB=GB&RaJD=RaJD&DecJD=DecJD&P0'
           '=P0&P1=P1&F0=F0&F1=F1&F2=F2&F3=F3&PEpoch=PEpoch&DM=DM&DM1=DM1&RM=R'
           'M&W50=W50&W10=W10&Units=Units&Tau_sc=Tau_sc&S400=S400&S1400=S1400&'
           'S2000=S2000&Binary=Binary&T0=T0&PB=PB&A1=A1&OM=OM&Ecc=Ecc&Tasc=Tas'
           'c&Eps1=Eps1&Eps2=Eps2&Minmass=Minmass&Medmass=Medmass&Bincomp=Binc'
           'omp&Dist=Dist&Dist_DM=Dist_DM&DMsinb=DMsinb&ZZ=ZZ&XX=XX&YY=YY&Asso'
           'c=Assoc&Survey=Survey&OSurvey=OSurvey&Date=Date&Type=Type&NGlt=NGl'
           't&R_lum=R_lum&R_lum14=R_lum14&Age=Age&Bsurf=Bsurf&Edot=Edot&Edotd2'
           '=Edotd2&PMtot=PMtot&VTrans=VTrans&P1_i=P1_i&Age_i=Age_i&Bsurf_i=Bs'
           'urf_i&B_LC=B_LC&startUserDefined=true&c1_val=&c2_val=&c3_val=&c4_v'
           'al=&sort_attr=jname&sort_order=asc&condition=&pulsar_names=&epheme'
           'ris=short&coords_unit=raj%2Fdecj&radius=&coords_1=&coords_2=&style'
           '=Long+with+errors&no_value=*&fsize=3&x_axis=&x_scale=lin'
           'ear&y_axis=&y_scale=linear&state=query')
    page = urlopen(url)
    s = page.read()
    page.close()
    f = open(MEDIA_ROOT+'database/atnf.html', 'w')
    f.write(s)
    f.close()


def parse_page():
    # read page
    f = open(MEDIA_ROOT + 'database/atnf.html', 'r')
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
            p = Pulsar.objects.get(Name=res[1])
            print 'ATNF Id = %d  Name = %s  (updating existing record...)' % (
                nums[ii], res[1])
        except ObjectDoesNotExist:
            p = Pulsar(Name=res[1])
            print 'ATNF Id = %d  Name = %s  (creating new record...)' % (
                nums[ii], res[1])
        # set pulsar parameters
        record_from_list(p, res)
        p.save()
        break


def record_from_list(p, res):
    p.Name = res[1]
    p.JName = res[2]
    p.RaJ = res[3]
    p.RaJ_err = to_float(res[4])
    p.DecJ = res[5]
    p.DecJ_err = to_float(res[6])
    p.PMRA = to_float(res[7])
    p.PMRA_err = to_float(res[8])
    p.PMDec = to_float(res[9])
    p.PMDec_err = to_float(res[10])
    p.PX = to_float(res[11])
    p.PX_err = to_float(res[12])
    p.PosEpoch = to_float(res[13])
    p.ELong = to_float(res[14])
    p.ELong_err = to_float(res[15])
    p.ELat = to_float(res[16])
    p.ELat_err = to_float(res[17])
    p.PMElong = to_float(res[18])
    p.PMElong_err = to_float(res[19])
    p.PMElat = to_float(res[20])
    p.PMElat_err = to_float(res[21])
    p.GL = to_float(res[22])
    p.GB = to_float(res[23])
    p.RaJD = to_float(res[24])
    p.DecJD = to_float(res[25])

    p.P0 = res[26]
    p.P0_err = to_float(res[27])
    p.P1 = to_float(res[28])
    p.P1_err = to_float(res[29])
    p.F0 = to_float(res[30])
    p.F0_err = to_float(res[31])
    p.F1 = to_float(res[32])
    p.F1_err = to_float(res[33])
    p.F2 = to_float(res[34])
    p.F2_err = to_float(res[35])
    p.F3 = to_float(res[36])
    p.F3_err = to_float(res[37])
    p.PEpoch = to_float(res[38])
    p.DM = to_float(res[39])
    p.DM_err = to_float(res[40])
    p.DM1 = to_float(res[41])
    p.DM1_err = to_float(res[42])
    p.RM = to_float(res[43])
    p.RM_err = to_float(res[44])
    p.W50 = to_float(res[45])
    p.W50_err = to_float(res[46])
    p.W10 = to_float(res[47])
    p.W10_err = to_float(res[48])
    p.Units = res[49]
    p.Tau_sc = to_float(res[50])
    p.Tau_sc_err = to_float(res[51])
    p.S400 = to_float(res[52])
    p.S400_err = to_float(res[53])
    p.S1400 = to_float(res[54])
    p.S1400_err = to_float(res[55])
    p.S2000 = to_float(res[56])
    p.S2000_err = to_float(res[57])

    p.Binary = res[58]
    p.T0 = to_float(res[59])
    p.T0_err = to_float(res[60])
    p.PB = to_float(res[61])
    p.PB_err = to_float(res[62])
    p.A1 = to_float(res[63])
    p.A1_err = to_float(res[64])
    p.OM = to_float(res[65])
    p.OM_err = to_float(res[66])
    p.ECC = to_float(res[67])
    p.ECC_err = to_float(res[68])
    p.TASC = to_float(res[69])
    p.TASC_err = to_float(res[70])
    p.Eps1 = to_float(res[71])
    p.Eps1_err = to_float(res[72])
    p.Eps2 = to_float(res[73])
    p.Eps2_err = to_float(res[74])
    p.MinMass = to_float(res[75])
    p.MedMass = to_float(res[76])
    p.BinComp = res[77]

    p.Dist = to_float(res[78])
    p.Dist_DM = to_float(res[79])
    p.DMsinb = to_float(res[80])
    p.ZZ = to_float(res[81])
    p.XX = to_float(res[82])
    p.YY = to_float(res[83])

    p.Assoc = res[84]
    p.Survey = res[85]
    p.OSurvey = str(res[86])
    p.Date = to_int(res[87])
    p.Type = res[88]
    p.NGlt = to_int(res[89])

    p.R_Lum = to_float(res[90])
    p.R_Lum14 = to_float(res[91])
    p.Age = to_float(res[92])
    p.BSurf = to_float(res[93])
    p.Edot = to_float(res[94])
    p.Edotd2 = to_float(res[95])
    p.PMTot = to_float(res[96])
    p.VTrans = to_float(res[97])
    p.P1_i = to_float(res[98])
    p.Age_i = to_float(res[99])
    p.BSurf_i = to_float(res[100])
    p.Edot_i = to_float(res[101])
    p.B_LC = to_float(res[102])


def to_float(str_):
    try:
        return float(str_)
    except ValueError:
        return 0.

def to_int(str_):
    try:
        return int(str_)
    except ValueError:
        return 0

