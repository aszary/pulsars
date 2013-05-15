from django.db import models


# Create your models here.
class Pulsar(models.Model):
    """ using same notation (for attributes) as in ATNF database
    """

    def __unicode__(self):
        result = "%s   ID : %d   P0 : %s" % (self.Name, self.id, self.P0)
        return result

    # data from ATNF
    Name = models.CharField(max_length=200, default='None', verbose_name=
                            'Pulsar name.  The B name if exists, otherwise'
                            'the J name')
    JName = models.CharField(max_length=200, default='None', verbose_name=
                             'Pulsar name based on J2000 coordinates')
    RaJ = models.CharField(default='None', max_length=200, verbose_name='Right'
                           'ascension (J2000) (hh:mm:ss.s)')
    RaJ_err = models.FloatField(default=0., verbose_name='Right ascension '
                                                         'Error')
    DecJ = models.CharField(max_length=200, default='None', verbose_name=
                            'Declination (J2000) (+dd:mm:ss)')
    DecJ_err = models.FloatField(default=0., verbose_name='Declination Error')
    PMRA = models.FloatField(default=0., verbose_name='Proper motion in right '
                                                      'ascension (mas/yr)')
    PMRA_err = models.FloatField(default=0., verbose_name='Proper motion in '
                                 'right ascension Error')
    PMDec = models.FloatField(default=0., verbose_name='Proper motion in '
                                                       'declination (mas/yr)')
    PMDec_err = models.FloatField(default=0., verbose_name='Proper motion in '
                                                           'declination Error')
    PX = models.FloatField(default=0., verbose_name='Annual parallax (mas)')
    PX_err = models.FloatField(default=0., verbose_name='Annual parallax '
                                                        'Error')
    PosEpoch = models.FloatField(default=0., verbose_name='Epoch at which the '
                                 'position is measured (MJD) ')
    ELong = models.FloatField(default=0., verbose_name='Ecliptic longitude '
                                                       '(degrees)')
    ELong_err = models.FloatField(default=0., verbose_name='Ecliptic longitude'
                                                           ' Error')
    ELat = models.FloatField(default=0., verbose_name='Ecliptic latitude '
                                                      '(degrees)')
    ELat_err = models.FloatField(default=0., verbose_name='Ecliptic latitude '
                                                          'Error')
    PMElong = models.FloatField(default=0., verbose_name='Proper motion in '
                                'ecliptic longitude (mas/yr)')
    PMElong_err = models.FloatField(default=0., verbose_name='Proper motion in'
                                    ' ecliptic longitude Error')
    PMElat = models.FloatField(default=0., verbose_name='Proper motion in '
                               'ecliptic latitude (mas/yr)')
    PMElat_err = models.FloatField(default=0., verbose_name='Proper motion in '
                                   'ecliptic latitude Error')
    GL = models.FloatField(default=0., verbose_name='Galactic longitude '
                                                    '(degrees)')
    GB = models.FloatField(default=0., verbose_name='Galactic latitude '
                                                    '(degrees)')
    RaJD = models.FloatField(default=0., verbose_name='Right ascension (J2000)'
                                                      ' (degrees)')
    DecJD = models.FloatField(default=0., verbose_name='Declination (J2000) '
                                                       '(degrees)')

    P0 = models.DecimalField(default='-0.0', max_digits=22, decimal_places=20,
                             verbose_name='Barycentric period of the pulsar'
                                          ' (s)')
    P0_err = models.FloatField(default=0., verbose_name='Barycentric period of'
                                                        ' the pulsar Error')
    P1 = models.FloatField(default=0., verbose_name='Time derivative of '
                           'barcycentric period (dimensionless)')
    P1_err = models.FloatField(default=0., verbose_name='Time derivative of '
                               'barcycentric period Error')
    F0 = models.FloatField(default=0., verbose_name='Barycentric rotation '
                                                    'frequency (Hz)')
    F0_err = models.FloatField(default=0., verbose_name='Barycentric rotation '
                                                        'frequency Error')
    F1 = models.FloatField(default=0., verbose_name='Time derivative of '
                           'barycentric rotation frequency (s-2)')
    F1_err = models.FloatField(default=0., verbose_name='Time derivative of '
                               'barycentric rotation frequency Error')
    F2 = models.FloatField(default=0., verbose_name='Second time derivative of'
                           ' barycentric rotation frequency (s-3)')
    F2_err = models.FloatField(default=0., verbose_name='Second time '
                               'derivative of barycentric rotation frequency'
                               ' Error')
    F3 = models.FloatField(default=0., verbose_name='Third time derivative of '
                           'barycentric rotation frequency (s-4)')
    F3_err = models.FloatField(default=0., verbose_name='Third time derivative'
                               ' of barycentric rotation frequency Error')
    PEpoch = models.FloatField(default=0., verbose_name='Epoch of period or '
                                                        'frequency (MJD)')
    DM = models.FloatField(default=0., verbose_name='Dispersion measure '
                                                    '(cm-3 pc)')
    DM_err = models.FloatField(default=0., verbose_name='Dispersion measure '
                                                        'Error')
    DM1 = models.FloatField(default=0., verbose_name='First time derivative of'
                            ' dispersion measure (cm-3 pc yr-1)')
    DM1_err = models.FloatField(default=0., verbose_name='First time '
                                'derivative of dispersion measure Error')
    RM = models.FloatField(default=0., verbose_name='Rotation measure '
                                                    '(rad m-2)')
    RM_err = models.FloatField(default=0., verbose_name='Rotation measure '
                                                        'Error')
    W50 = models.FloatField(default=0., verbose_name='Width of pulse at 50% of'
                            ' peak (ms).  Note, pulse widths are a function of'
                            ' both observing frequency and observational time'
                            ' resolution,so quoted widths are indicative only.'
                            ' Refer to the original reference for details.')
    W50_err = models.FloatField(default=0., verbose_name='Width of pulse at '
                                '50% of peak (ms).  Note, pulse widths are a '
                                'function of both observing frequency and '
                                'observational time resolution,so quoted '
                                'widths are indicative only. Refer to the '
                                'original reference for details. Error')
    W10 = models.FloatField(default=0., verbose_name='Width of pulse at 10% '
                            '(ms). Note the comments above for W50.')
    W10_err = models.FloatField(default=0., verbose_name='Width of pulse at '
                                '10% (ms). Note the comments above for W50.'
                                ' Error')
    Units = models.CharField(max_length=200, default="None", verbose_name=
                             'no idea what it is..')
    Tau_sc = models.FloatField(default=0., verbose_name='Temporal broadening '
                               'of pulses at 1 GHz due to interestellar '
                               'scattering (s)')
    Tau_sc_err = models.FloatField(default=0., verbose_name='Temporal '
                                   'broadening of pulses at 1 GHz due to '
                                   'interestellar scattering Error')
    S400 = models.FloatField(default=0., verbose_name='Mean flux density at '
                                                      '400 MHz (mJy)')
    S400_err = models.FloatField(default=0., verbose_name='Mean flux density '
                                                          'at 400 MHz Error')
    S1400 = models.FloatField(default=0., verbose_name='Mean flux density at '
                                                       '1400 MHz (mJy)')
    S1400_err = models.FloatField(default=0., verbose_name='Mean flux density '
                                                           'at 1400 MHz Error')
    S2000 = models.FloatField(default=0., verbose_name='Mean flux density at '
                                                       '2000 MHz (mJy)')
    S2000_err = models.FloatField(default=0., verbose_name='Mean flux density '
                                                           'at 2000 MHz Error')
    # what is it? replaced by S2000 in parser?
    spindx = models.FloatField(default=0., verbose_name='Measured spectral '
                                                        'index')
    spindx_err = models.FloatField(default=0., verbose_name='Measured spectral'
                                                            ' index Error')
    Binary = models.CharField(max_length=200, default="None", verbose_name=
                              'Binary model (normally one of several '
                              'recognised by the pulsar timing program TEMPO')
    T0 = models.FloatField(default=0., verbose_name='Epoch of periastron '
                                                    '(MJD)')
    T0_err = models.FloatField(default=0., verbose_name='Epoch of periastron '
                                                        'Error')
    PB = models.FloatField(default=0., verbose_name='Binary period of pulsar '
                                                    '(days)')
    PB_err = models.FloatField(default=0., verbose_name='Binary period of '
                                                        'pulsar Error')
    A1 = models.FloatField(default=0., verbose_name='Projected semi-major axis'
                                                    ' of orbit (lt s)')
    A1_err = models.FloatField(default=0., verbose_name='Projected semi-major'
                                                        ' axis of orbit Error')
    OM = models.FloatField(default=0., verbose_name='Longitude of periastron'
                                                    ' (degrees)')
    OM_err = models.FloatField(default=0., verbose_name='Longitude of'
                                                        ' periastron Error')
    ECC = models.FloatField(default=0., verbose_name='Eccentricity')
    ECC_err = models.FloatField(default=0., verbose_name='Eccentricity Error')
    TASC = models.FloatField(default=0., verbose_name='Epoch of ascending node'
                                                      '(MJD)')
    TASC_err = models.FloatField(default=0., verbose_name='Epoch of ascending'
                                                          ' node Error')
    Eps1 = models.FloatField(default=0., verbose_name='Ecc x sin(OM) - ELL1'
                                                      ' binary model')
    Eps1_err = models.FloatField(default=0., verbose_name='Ecc x sin(OM) -'
                                 ' ELL1 binary model Error')
    Eps2 = models.FloatField(default=0., verbose_name='Ecc x cos(OM) - ELL1 '
                                                      'binary model')
    Eps2_err = models.FloatField(default=0., verbose_name='Ecc x cos(OM) - '
                                 'ELL1 binary model Error')
    MinMass = models.FloatField(default=0., verbose_name='Minimum companion '
                                'mass assuming i=90 degrees and neutron star '
                                'mass is 1.35 Mo')
    MedMass = models.FloatField(default=0., verbose_name='Median companion '
                                'mass assuming i=60 degrees')
    MedMass = models.FloatField(default=0., verbose_name='Median companion '
                                'mass assuming i=60 degrees')
    BinComp = models.CharField(max_length=200, default='None', verbose_name=
                               'Companion type')

    Dist = models.FloatField(default=0., verbose_name='Best estimate of the '
                             'pulsar distance (kpc)')
    Dist_DM = models.FloatField(default=0., verbose_name='Distance based on '
                                'the Taylor & Cordes (1993) electron density'
                                ' model. In LONG or PUBLICATION QUALITY modes,'
                                ' lower limits from the distance model are '
                                'preceded by a + sign.')
    DMsinb = models.FloatField(default=0., verbose_name='DM x sin(b) '
                                                        '(cm-3 pc)')
    ZZ = models.FloatField(default=0., verbose_name='Distance from the '
                           'Galactic plane, based on Dist')
    XX = models.FloatField(default=0., verbose_name='X-Distance in X-Y-Z '
                           'Galactic coordinate system (kpc)')
    YY = models.FloatField(default=0., verbose_name='Y-Distance in X-Y-Z '
                           'Galactic coordinate system (kpc)')

    Assoc = models.CharField(max_length=255, default="0", verbose_name='Names'
                             ' of other objects, for example, supernova '
                             'remnants or globular clusters, associated with '
                             'the pulsar')
    Survey = models.CharField(max_length=200, default="0", verbose_name='Surve'
                              'ys that detected the pulsar (discovery survey '
                              'first).')
    OSurvey = models.CharField(max_length=200, default="0", verbose_name='Surv'
                               'eys that detected the pulsar encoded as bits '
                               'in integer')
    Date = models.IntegerField(default=0, verbose_name='Date of discovery'
                                                       ' publication.')
    Type = models.CharField(max_length=200, default="0", verbose_name='Type '
                            'codes for the pulsar. Click here for available '
                            'types.')
    NGlt = models.IntegerField(default=0, verbose_name='Number of glitches '
                               'observed for the pulsar')

    R_Lum = models.FloatField(default=0., verbose_name='Radio luminosity at '
                                                       '400 MHz (mJy kpc2)')
    R_Lum14 = models.FloatField(default=0., verbose_name='Radio luminosity at '
                                                         '1400 MHz (mJy kpc2)')
    Age = models.FloatField(default=0., verbose_name='Spin down age (yr) []')
    BSurf = models.FloatField(default=0., verbose_name='Surface magnetic flux'
                                                       ' density (Gauss) []')
    Edot = models.FloatField(default=0., verbose_name='Spin down energy loss '
                                                      'rate (ergs/s)')
    Edotd2 = models.FloatField(default=0., verbose_name='Energy flux at the '
                                                        'Sun (ergs/kpc2/s)')
    PMTot = models.FloatField(default=0., verbose_name='Total proper motion '
                                                       '(mas/yr)')
    VTrans = models.FloatField(default=0., verbose_name='Transverse velocity'
                               ' - based on DIST (km/s)')
    P1_i = models.FloatField(default=0., verbose_name='Period derivative '
                             'corrected for proper motion effect')
    Age_i = models.FloatField(default=0., verbose_name='Spin down age from '
                                                       'P1_i (yr)')
    BSurf_i = models.FloatField(default=0., verbose_name='Surface magnetic '
                                'dipole from P1_i (gauss)')
    Edot_i = models.FloatField(default=0., verbose_name='Spin down energy loss'
                               ' rate from P1_i (ergs/s)')
    B_LC = models.FloatField(default=0., verbose_name='Magnetic field at light'
                                                      ' cylinder')

    # additional information
    simbad_link = models.TextField(default="http://simbad.u-strasbg.fr",
                                   verbose_name='Simbad database link')
    comment = models.TextField(default="", verbose_name='Short comment  e.g. '
                               'popular pulsar name: Crab')


class XrayArticle(models.Model):
    psr_id = models.ForeignKey(Pulsar, null=True, default=None)
    num = models.IntegerField(default=0, verbose_name='0 the highest'
                                     ' (included in most graphs/tables)')
    article = models.TextField(default='', verbose_name='article link')
    cite = models.TextField(default="\cite{}", verbose_name='latex citation')
    info = models.TextField(default="", verbose_name='Additional information')
    dist = models.FloatField(default=0., verbose_name='distance used to '
                             'calculate luminosities [in kpc]')


class XrayFit(models.Model):
    article_id = models.ForeignKey(XrayArticle, null=True, default=None)
    ordinal = models.IntegerField(default=-1, verbose_name='Ordinal number'
                                  ' in X-ray catalogue, sorted by name')
    num = models.IntegerField(default=0, verbose_name='0 the highest'
                                     ' (included in most graphs/tables)')
    spectrum = models.CharField(default='', max_length=200, verbose_name='type'
                                ' spectrum fit e.g. BB + PL')


class XrayComponent(models.Model):
    spec_types = (('BB', 'blackbody'), ('PL', 'power-law'),
                 ('AT', 'atmospheric'), ('OT', 'other'))
    fit_id = models.ForeignKey(XrayFit, null=True, default=None)
    num = models.IntegerField(default=0, verbose_name='number of component')
    spec_type = models.CharField(choices=spec_types, max_length=200)
    lum = models.FloatField(default=0., verbose_name='luminosity [erg s^-1]')
    lum_plus = models.FloatField(default=0., verbose_name='luminosity error +'
                                                          ' [erg s^-1]')
    lum_minus = models.FloatField(default=0., verbose_name='luminosity error -'
                                                           ' [erg s^-1]')
    flux = models.FloatField(default=0., verbose_name='flux [erg s^-1 cm^-2]')
    flux_plus = models.FloatField(default=0., verbose_name='flux error +'
                                                          ' [erg s^-1 cm^-2]')
    flux_minus = models.FloatField(default=0., verbose_name='flux error -'
                                   ' [erg s^-1 cm^-2]')
    t = models.FloatField(default=0., verbose_name='temperature [K]')
    t_plus = models.FloatField(default=0., verbose_name='temperature err +[K]')
    t_minus = models.FloatField(default=0., verbose_name='temperature err - '
                                                         '[K]')
    r = models.FloatField(default=0., verbose_name='radius from BB fit [cm]')
    r_plus = models.FloatField(default=0., verbose_name='radius err + [cm]')
    r_minus = models.FloatField(default=0., verbose_name='radius err - [cm]')
    pl = models.FloatField(default=0., verbose_name='photon index')
    pl_plus = models.FloatField(default=0., verbose_name='photon index err +')
    pl_minus = models.FloatField(default=0., verbose_name='photon index err -')
    b_atm = models.FloatField(default=0., verbose_name='??')


class Geometry(models.Model):
    psr_id = models.ForeignKey(Pulsar, null=True, default=None)
    article = models.TextField(default='', verbose_name='article link')
    cite = models.TextField(default="\cite{}", verbose_name='latex citation')
    info = models.TextField(default="", verbose_name='Additional information')
    alpha = models.FloatField(default=0., verbose_name='inclination angle of '
                                                       'magnetic axis [deg]')
    beta = models.FloatField(default=0., verbose_name='impact parameter [deg]')
    rho = models.FloatField(default=0., verbose_name='opening angle [deg]')


class Subpulses(models.Model):
    psr_id = models.ForeignKey(Pulsar, null=True, default=None)
    article = models.TextField(default='', verbose_name='article link')
    cite = models.TextField(default="\cite{}", verbose_name='latex citation')
    info = models.TextField(default="", verbose_name='Additional information')
    p2 = models.FloatField(default=0., verbose_name='characteristic spaces '
                                                    'between subpulses [deg]')
    p2_plus = models.FloatField(default=0., verbose_name='characteristic '
                                'spaces between subpulses error + [deg]')
    p2_minus = models.FloatField(default=0., verbose_name='characteristic '
                                 'spaces between subpulses error - [deg]')
    p3 = models.FloatField(default=0., verbose_name='period at which a '
                           'pattern of pulses crosses the pulse window [P0]')
    p3_plus = models.FloatField(default=0., verbose_name='period at which a '
                                'pattern of pulses crosses the pulse window'
                                ' error + [P0]')
    p3_minus = models.FloatField(default=0., verbose_name='period at which a '
                                 'pattern of pulses crosses the pulse window '
                                 'error - [P0]')
    p4 = models.FloatField(default=0., verbose_name='Does it exist?')


class Additional(models.Model):
    """ all additional pulsar information, dist_dm,
    """
    psr_id = models.ForeignKey(Pulsar, null=True, default=None)
    articles = models.TextField(default='', verbose_name='article links (;)')
    best_age = models.FloatField(default=0., verbose_name='Best estimate of'
                                                          'age')
    dist_dm_cl = models.FloatField(default=0., verbose_name='CL model [kpc]')
    dist_dm_cl_plus = models.FloatField(default=0., verbose_name='err + [kpc]')
    dist_dm_cl_minus = models.FloatField(default=0., verbose_name='err - '
                                                                  '[kpc]')
    dist_pi = models.FloatField(default=0., verbose_name='parallax distance'
                                                         ' [kpc]')
    dist_pi_plus = models.FloatField(default=0., verbose_name='parallax '
                                     'distance error + [kpc]')
    dist_pi_minus = models.FloatField(default=0., verbose_name='parallax '
                                      'distance error - [kpc]')

class Calculations(models.Model):
    """ all my calculations stored in database
    """
    # geometry
    psr_id = models.ForeignKey(Pulsar, null=True, default=None, blank=True)
    cos_i = models.FloatField(default=0., verbose_name='time averaged cosine '
                              'of the angle between the magnetic axis and the '
                              'line of sight')
    f = models.FloatField(default=0., verbose_name='flux correction factor for'
                          ' x-ray data (similar to cos_theta, but with '
                          'gravitational bending)')
    # checks
    dotP_15 = models.FloatField(default=0., verbose_name='period derivative')
    bsurf2 = models.FloatField(default=0., verbose_name='surface magnetic field'
                               'at the pole')
    b_14dp = models.FloatField(default=0., verbose_name='surface magnetic '
                               'field at the pole [in units of 10^14 G]')
    l_sd = models.FloatField(default=0., verbose_name='Spin-down luminosity -'
                             ' same as edot')
    #  X-rays
    a_dp = models.FloatField(default=0., verbose_name='area of conventional '
                                                      'polar cap [cm^2]')
    r_dp = models.FloatField(default=0., verbose_name='radius of conventional'
                                                      'polar cap [cm]')
    a = models.FloatField(default=0., verbose_name='actual polar cap (from '
                                                   'best X-ray obs [cm^2]')
    b = models.FloatField(default=0., verbose_name='b = B_s / B_d = A_dp / A')
    b_14 = models.FloatField(default=0., verbose_name='surface magnetic field '
                                                      'strength [in 10^14 G]')
    b_14_plus = models.FloatField(default=0., verbose_name='surface magnetic '
                                  'field strength err + [in 10^14 G]')
    b_14_minus = models.FloatField(default=0., verbose_name='surface magnetic '
                                   'field strength err - [in 10^14 G]')



