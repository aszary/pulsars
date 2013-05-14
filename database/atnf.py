__author__ = 'aszary'

from pulsars.settings import PROJECT_PATH, MEDIA_ROOT
from urllib import urlopen


def get_page():
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
    print PROJECT_PATH
