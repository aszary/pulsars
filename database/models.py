from django.db import models

class GammaRayFermi(models.Model):
    def __unicode__(self):
        result = "GammaRayFermi ID : %d NUM : %d" % (self.id, self.num)
        return result
    psr_id = models.ForeignKey('Pulsar', null=True, blank=True, default=None)
    num = models.IntegerField(null=True, blank=True, verbose_name='number of component')
    lum = models.FloatField(null=True, blank=True, verbose_name='the total gamma-ray luminosity in the 0.1 - 100 GeV energy band (assuming f=1, isotropic)  [erg s^-1]')
    lum_plus = models.FloatField(null=True, blank=True, verbose_name='statistical uncertainty in the spectral fit (plus) [erg s^-1]')
    lum_minus = models.FloatField(null=True, blank=True, verbose_name='statistical uncertainty in the spectral fit (minus) [erg s^-1]')
    lum_plus_dist = models.FloatField(null=True, blank=True, verbose_name='uncertainty due to the distance errors (plus) [erg s^-1]')
    lum_minus_dist = models.FloatField(null=True, blank=True, verbose_name='uncertainty due to the distance errors (plus) [erg s^-1]')


class XrayComponent(models.Model):
    def __unicode__(self):
        result = "XrayComponent ID : %d (%s) NUM : %d" % (self.id, self.spec_type, self.num)
        return result
    psr_id = models.ForeignKey('Pulsar', null=True, blank=True, default=None)
    spec_types = (('BB', 'blackbody'), ('PL', 'power-law'), ('AT', 'atmospheric'), ('OT', 'other'))
    num = models.IntegerField(null=True, blank=True, verbose_name='number of component')
    spec_type = models.CharField(choices=spec_types, max_length=200)
    lum = models.FloatField(null=True, blank=True, verbose_name='luminosity [erg s^-1]')
    lum_plus = models.FloatField(null=True, blank=True, verbose_name='luminosity error + [erg s^-1]')
    lum_minus = models.FloatField(null=True, blank=True, verbose_name='luminosity error - [erg s^-1]')
    flux = models.FloatField(null=True, blank=True, verbose_name='flux [erg s^-1 cm^-2]')
    flux_plus = models.FloatField(null=True, blank=True, verbose_name='flux error + [erg s^-1 cm^-2]')
    flux_minus = models.FloatField(null=True, blank=True, verbose_name='flux error -[erg s^-1 cm^-2]')
    t = models.FloatField(null=True, blank=True, verbose_name='temperature [K]')
    t_plus = models.FloatField(null=True, blank=True, verbose_name='temperature err +[K]')
    t_minus = models.FloatField(null=True, blank=True, verbose_name='temperature err - [K]')
    r = models.FloatField(null=True, blank=True, verbose_name='radius from BB fit [cm]')
    r_plus = models.FloatField(null=True, blank=True,verbose_name='radius err + [cm]')
    r_minus = models.FloatField(null=True, blank=True, verbose_name='radius err - [cm]')
    pl = models.FloatField(null=True, blank=True,                           verbose_name='photon index')
    pl_plus = models.FloatField(null=True, blank=True, verbose_name='photon index err +')
    pl_minus = models.FloatField(null=True, blank=True, verbose_name='photon index err -')
    b_atm = models.FloatField(null=True, blank=True, verbose_name='Field strength -atmospheric model')


class XrayFit(models.Model):
    def __unicode__(self):
        result = "XrayFit ID : %d (%s) NUM : %d" % (self.id, self.spectrum, self.num)
        return result
    psr_id = models.ForeignKey('Pulsar', default=None, null=True, blank=True)
    components = models.ManyToManyField(XrayComponent)
    ordinal = models.IntegerField(null=True, blank=True, verbose_name='Ordinal number in X-ray catalogue, sorted by name')
    num = models.IntegerField(null=True, blank=True, verbose_name='0 the highest (included in most graphs/tables)')
    spectrum = models.CharField(default=None, null=True, blank=True, max_length=200, verbose_name='type spectrum fit e.g. BB + PL')


class XrayArticle(models.Model):
    def __unicode__(self):
        result = "XrayArticle (%s)" % self.cite
        return result
    fits = models.ManyToManyField(XrayFit)
    num = models.IntegerField(null=True, blank=True, verbose_name='0 the highest (included in most graphs/tables)')
    article = models.TextField(default=None, null=True, blank=True, verbose_name='article link')
    cite = models.TextField(default="\cite{}", verbose_name='latex citation')
    info = models.TextField(default=None, null=True, blank=True, verbose_name='Additional information')
    dist = models.FloatField(null=True, blank=True, verbose_name='distance used to calculate luminosities [in kpc]')


class Geometry(models.Model):
    def __unicode__(self):
        result = "Geometry ID : %d" % (self.id)
        return result
    num = models.IntegerField(null=True, blank=True, verbose_name='Number')
    article = models.TextField(default=None, null=True, blank=True, verbose_name='article link')
    cite = models.TextField(default="\cite{}", verbose_name='latex citation')
    info = models.TextField(default=None, null=True, blank=True, verbose_name='Additional information')
    alpha = models.FloatField(null=True, blank=True, verbose_name='inclination angle of magnetic axis [deg]')
    beta = models.FloatField(null=True, blank=True, verbose_name='impact parameter [deg]')
    rho = models.FloatField(null=True, blank=True, verbose_name='opening angle [deg]')


class Subpulse(models.Model):
    def __unicode__(self):
        result = "Subpulse ID : %d " % (self.id)
        return result
    num = models.IntegerField(null=True, blank=True, verbose_name='Number')
    article = models.TextField(default=None, null=True, blank=True, verbose_name='article link')
    cite = models.TextField(default="\cite{}", verbose_name='latex citation')
    info = models.TextField(default=None, null=True, blank=True, verbose_name='Additional information')
    p2 = models.FloatField(null=True, blank=True, verbose_name='characteristic spaces between subpulses [deg]')
    p2_plus = models.FloatField(null=True, blank=True, verbose_name='characteristic spaces between subpulses error + [deg]')
    p2_minus = models.FloatField(null=True, blank=True, verbose_name='characteristic spaces between subpulses error - [deg]')
    p3 = models.FloatField(null=True, blank=True, verbose_name='period at which a pattern of pulses crosses the pulse window [P0]')
    p3_plus = models.FloatField(null=True, blank=True, verbose_name='period at which a pattern of pulses crosses the pulse window error + [P0]')
    p3_minus = models.FloatField(null=True, blank=True, verbose_name='period at which a pattern of pulses crosses the pulse window error - [P0]')
    p4 = models.FloatField(null=True, blank=True, verbose_name='Does it exist?')


class Additional(models.Model):
    """ all additional pulsar information, dist_dm,
    """
    def __unicode__(self):
        result = "Additional ID : %d " % (self.id)
        return result
    num = models.IntegerField(null=True, blank=True, verbose_name='Number')
    articles = models.TextField(default=None, null=True, blank=True, verbose_name='article links (;)')
    best_age = models.FloatField(null=True, blank=True, verbose_name='Best estimate of age')
    dist_dm_cl = models.FloatField(null=True, blank=True, verbose_name='CL model [kpc]')
    dist_dm_cl_plus = models.FloatField(null=True, blank=True, verbose_name='err + [kpc]')
    dist_dm_cl_minus = models.FloatField(null=True, blank=True, verbose_name='err - [kpc]')
    dist_pi = models.FloatField(null=True, blank=True, verbose_name='parallax distance [kpc]')
    dist_pi_plus = models.FloatField(null=True, blank=True, verbose_name='parallax distance error + [kpc]')
    dist_pi_minus = models.FloatField(null=True, blank=True, verbose_name='parallax distance error - [kpc]')


class Calculation(models.Model):
    """ all my calculations stored in database
    """
    def __unicode__(self):
        result = "Calculation ID : %d " % (self.id)
        return result
    num = models.IntegerField(null=True, blank=True, verbose_name='Number')
    # geometry
    cos_i = models.FloatField(null=True, blank=True, verbose_name='time averaged cosine of the angle between the magnetic axis and the line of sight')
    f = models.FloatField(null=True, blank=True, verbose_name='flux correction factor for x-ray data (similar to cos_theta, but with gravitational bending)')
    # checks
    dotp_15 = models.FloatField(null=True, blank=True, verbose_name='period derivative')
    bsurf2 = models.FloatField(null=True, blank=True, verbose_name='surface magnetic field at the pole')
    b_14dp = models.FloatField(null=True, blank=True, verbose_name='surface magnetic field at the pole [in units of 10^14 G]')
    l_sd = models.FloatField(null=True, blank=True, verbose_name='Spin-down luminosity - same as edot')
    #  X-rays
    a_dp = models.FloatField(null=True, blank=True, verbose_name='area of conventional polar cap [cm^2]')
    r_dp = models.FloatField(null=True, blank=True, verbose_name='radius of conventional polar cap [cm]')
    a = models.FloatField(null=True, blank=True, verbose_name='actual polar cap (from best X-ray obs [cm^2]')
    b = models.FloatField(null=True, blank=True, verbose_name='b = B_s / B_d = A_dp / A')
    b_14 = models.FloatField(null=True, blank=True, verbose_name='surface magnetic field strength [in 10^14 G]')
    b_14_plus = models.FloatField(null=True, blank=True, verbose_name='surface magnetic field strength err + [in 10^14 G]')
    b_14_minus = models.FloatField(null=True, blank=True, verbose_name='surface magnetic field strength err - [in 10^14 G]')


class Pulsar(models.Model):

    def __unicode__(self):
        result = "%s   ID : %d   P0 : %s" % (self.name, self.id, self.p0)
        return result

    # data from ATNF
    name = models.CharField(max_length=200, default=None, null=True, blank=True, verbose_name= 'Pulsar name.  The B name if exists, otherwise the J name')
    jname = models.CharField(max_length=200, default=None, null=True, blank=True, verbose_name='Pulsar name based on J2000 coordinates')
    raj = models.CharField(default=None, null=True, blank=True, max_length=200, verbose_name='Right ascension (J2000) (hh:mm:ss.s)')
    raj_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Right ascension Error')
    decj = models.CharField(max_length=200, default=None, null=True, blank=True, verbose_name='Declination (J2000) (+dd:mm:ss)')
    decj_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Declination Error')
    pmra = models.FloatField(default=None, null=True, blank=True, verbose_name='Proper motion in right ascension (mas/yr)')
    pmra_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Proper motion in right ascension Error')
    pmdec = models.FloatField(default=None, null=True, blank=True, verbose_name='Proper motion in declination (mas/yr)')
    pmdec_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Proper motion in declination Error')
    px = models.FloatField(default=None, null=True, blank=True, verbose_name='Annual parallax (mas)')
    px_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Annual parallax Error')
    posepoch = models.FloatField(default=None, null=True, blank=True, verbose_name='Epoch at which the position is measured (MJD) ')
    elong = models.FloatField(default=None, null=True, blank=True, verbose_name='Ecliptic longitude (degrees)')
    elong_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Ecliptic longitude Error')
    elat = models.FloatField(default=None, null=True, blank=True, verbose_name='Ecliptic latitude (degrees)')
    elat_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Ecliptic latitude Error')
    pmelong = models.FloatField(default=None, null=True, blank=True, verbose_name='Proper motion in ecliptic longitude (mas/yr)')
    pmelong_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Proper motion in ecliptic longitude Error')
    pmelat = models.FloatField(default=None, null=True, blank=True, verbose_name='Proper motion in ecliptic latitude (mas/yr)')
    pmelat_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Proper motion in ecliptic latitude Error')
    gl = models.FloatField(default=None, null=True, blank=True, verbose_name='Galactic longitude (degrees)')
    gb = models.FloatField(default=None, null=True, blank=True, verbose_name='Galactic latitude (degrees)')
    rajd = models.FloatField(default=None, null=True, blank=True, verbose_name='Right ascension (J2000) (degrees)')
    decjd = models.FloatField(default=None, null=True, blank=True, verbose_name='Declination (J2000) (degrees)')

    p0 = models.DecimalField(default=None, max_digits=22, decimal_places=20, verbose_name='Barycentric period of the pulsar (s)')
    p0_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Barycentric period of the pulsar Error')
    p1 = models.FloatField(default=None, null=True, blank=True, verbose_name='Time derivative of barcycentric period (dimensionless)')
    p1_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Time derivative of barcycentric period Error')
    f0 = models.FloatField(default=None, null=True, blank=True, verbose_name='Barycentric rotation frequency (Hz)')
    f0_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Barycentric rotation frequency Error')
    f1 = models.FloatField(default=None, null=True, blank=True, verbose_name='Time derivative of barycentric rotation frequency (s-2)')
    f1_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Time derivative of barycentric rotation frequency Error')
    f2 = models.FloatField(default=None, null=True, blank=True, verbose_name='Second time derivative of barycentric rotation frequency (s-3)')
    f2_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Second time derivative of barycentric rotation frequency Error')
    f3 = models.FloatField(default=None, null=True, blank=True, verbose_name='Third time derivative of barycentric rotation frequency (s-4)')
    f3_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Third time derivative of barycentric rotation frequency Error')
    pepoch = models.FloatField(default=None, null=True, blank=True, verbose_name='Epoch of period or frequency (MJD)')
    dm = models.FloatField(default=None, null=True, blank=True, verbose_name='Dispersion measure (cm-3 pc)')
    dm_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Dispersion measure Error')
    dm1 = models.FloatField(default=None, null=True, blank=True, verbose_name='First time derivative of dispersion measure (cm-3 pc yr-1)')
    dm1_err = models.FloatField(default=None, null=True, blank=True, verbose_name='First time derivative of dispersion measure Error')
    rm = models.FloatField(default=None, null=True, blank=True, verbose_name='Rotation measure (rad m-2)')
    rm_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Rotation measure Error')
    w50 = models.FloatField(default=None, null=True, blank=True, verbose_name='Width of pulse at 50% of peak (ms).  Note, pulse widths are a function of both observing frequency and observational time resolution,so quoted widths are indicative only. Refer to the original reference for details.')
    w50_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Width of pulse at 50% of peak (ms).  Note, pulse widths are a function of both observing frequency and observational time resolution,so quoted widths are indicative only. Refer to the original reference for details. Error')
    w10 = models.FloatField(default=None, null=True, blank=True, verbose_name='Width of pulse at 10% (ms). Note the comments above for W50.')
    w10_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Width of pulse at 10% (ms). Note the comments above for W50. Error')
    units = models.CharField(max_length=200, default=None, verbose_name='no idea what it is..')
    tau_sc = models.FloatField(default=None, null=True, blank=True, verbose_name='Temporal broadening of pulses at 1 GHz due to interestellar scattering (s)')
    tau_sc_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Temporal broadening of pulses at 1 GHz due to interestellar scattering Error')
    s400 = models.FloatField(default=None, null=True, blank=True, verbose_name='Mean flux density at 400 MHz (mJy)')
    s400_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Mean flux density at 400 MHz Error')
    s1400 = models.FloatField(default=None, null=True, blank=True, verbose_name='Mean flux density at 1400 MHz (mJy)')
    s1400_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Mean flux density at 1400 MHz Error')
    s2000 = models.FloatField(default=None, null=True, blank=True, verbose_name='Mean flux density at 2000 MHz (mJy)')
    s2000_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Mean flux density at 2000 MHz Error')
    # what is it? replaced by S2000 in parser?
    spindx = models.FloatField(default=None, null=True, blank=True, verbose_name='Measured spectral index')
    spindx_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Measured spectral index Error')
    binary = models.CharField(max_length=200, default=None, null=True, blank=True,verbose_name='Binary model (normally one of several recognised by the pulsar timing program TEMPO')
    t0 = models.FloatField(default=None, null=True, blank=True, verbose_name='Epoch of periastron (MJD)')
    t0_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Epoch of periastron Error')
    pb = models.FloatField(default=None, null=True, blank=True, verbose_name='Binary period of pulsar (days)')
    pb_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Binary period of pulsar Error')
    a1 = models.FloatField(default=None, null=True, blank=True, verbose_name='Projected semi-major axis of orbit (lt s)')
    a1_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Projected semi-major axis of orbit Error')
    om = models.FloatField(default=None, null=True, blank=True, verbose_name='Longitude of periastron (degrees)')
    om_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Longitude of periastron Error')
    ecc = models.FloatField(default=None, null=True, blank=True, verbose_name='Eccentricity')
    ecc_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Eccentricity Error')
    tasc = models.FloatField(default=None, null=True, blank=True, verbose_name='Epoch of ascending node (MJD)')
    tasc_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Epoch of ascending node Error')
    eps1 = models.FloatField(default=None, null=True, blank=True, verbose_name='Ecc x sin(OM) - ELL1 binary model')
    eps1_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Ecc x sin(OM) - ELL1 binary model Error')
    eps2 = models.FloatField(default=None, null=True, blank=True, verbose_name='Ecc x cos(OM) - ELL1 binary model')
    eps2_err = models.FloatField(default=None, null=True, blank=True, verbose_name='Ecc x cos(OM) - ELL1 binary model Error')
    minmass = models.FloatField(default=None, null=True, blank=True, verbose_name='Minimum companion mass assuming i=90 degrees and neutron star mass is 1.35 Mo')
    medmass = models.FloatField(default=None, null=True, blank=True, verbose_name='Median companion mass assuming i=60 degrees')
    medmass = models.FloatField(default=None, null=True, blank=True, verbose_name='Median companion mass assuming i=60 degrees')
    bincomp = models.CharField(max_length=200, default=None, verbose_name='Companion type')

    dist = models.FloatField(default=None, null=True, blank=True, verbose_name='Best estimate of the pulsar distance (kpc)')
    dist_dm = models.FloatField(default=None, null=True, blank=True, verbose_name='Distance based on the Taylor & Cordes (1993) electron density model. In LONG or PUBLICATION QUALITY modes, lower limits from the distance model are preceded by a + sign.')
    dmsinb = models.FloatField(default=None, null=True, blank=True, verbose_name='DM x sin(b) (cm-3 pc)')
    zz = models.FloatField(default=None, null=True, blank=True, verbose_name='Distance from the Galactic plane, based on Dist')
    xx = models.FloatField(default=None, null=True, blank=True, verbose_name='X-Distance in X-Y-Z Galactic coordinate system (kpc)')
    yy = models.FloatField(default=None, null=True, blank=True, verbose_name='Y-Distance in X-Y-Z Galactic coordinate system (kpc)')

    assoc = models.CharField(max_length=255, default=None, null=True, blank=True,verbose_name='Names of other objects, for example, supernova remnants or globular clusters, associated with the pulsar')
    survey = models.CharField(max_length=200, default=None, null=True, blank=True,verbose_name='Surveys that detected the pulsar (discovery survey first).')
    osurvey = models.CharField(max_length=200, default=None, null=True, blank=True,verbose_name='Surveys that detected the pulsar encoded as bits in integer')
    date = models.IntegerField(default=None, null=True, blank=True, verbose_name='Date of discovery publication.')
    type = models.CharField(max_length=200, default=None, null=True, blank=True,verbose_name='Type codes for the pulsar. Click here for available types.')
    nglt = models.IntegerField(default=None, null=True, blank=True, verbose_name='Number of glitches observed for the pulsar')

    r_lum = models.FloatField(default=None, null=True, blank=True, verbose_name='Radio luminosity at 400 MHz (mJy kpc2)')
    r_lum14 = models.FloatField(default=None, null=True, blank=True, verbose_name='Radio luminosity at 1400 MHz (mJy kpc2)')
    age = models.FloatField(default=None, null=True, blank=True, verbose_name='Spin down age (yr) []')
    bsurf = models.FloatField(default=None, null=True, blank=True, verbose_name='Surface magnetic flux density (Gauss) []')
    edot = models.FloatField(default=None, null=True, blank=True, verbose_name='Spin down energy loss rate (ergs/s)')
    edotd2 = models.FloatField(default=None, null=True, blank=True, verbose_name='Energy flux at the Sun (ergs/kpc2/s)')
    pmtot = models.FloatField(default=None, null=True, blank=True, verbose_name='Total proper motion (mas/yr)')
    vtrans = models.FloatField(default=None, null=True, blank=True, verbose_name='Transverse velocity - based on DIST (km/s)')
    p1_i = models.FloatField(default=None, null=True, blank=True, verbose_name='Period derivative corrected for proper motion effect')
    age_i = models.FloatField(default=None, null=True, blank=True, verbose_name='Spin down age from P1_i (yr)')
    bsurf_i = models.FloatField(default=None, null=True, blank=True, verbose_name='Surface magnetic dipole from P1_i (gauss)')
    edot_i = models.FloatField(default=None, null=True, blank=True, verbose_name='Spin down energy loss rate from P1_i (ergs/s)')
    b_lc = models.FloatField(default=None, null=True, blank=True, verbose_name='Magnetic field at light cylinder')

    # additional information
    simbad_link = models.TextField(default="http://simbad.u-strasbg.fr", verbose_name='Simbad database link')
    comment = models.TextField(default=None, null=True, blank=True, verbose_name='Short comment  e.g. popular pulsar name: Crab')
    lum_malov = models.FloatField(default=None, null=True, blank=True, verbose_name='radio luminosity from Malov 2007 in erg/s')

    xray_articles = models.ManyToManyField(XrayArticle)
    geometries = models.ManyToManyField(Geometry)
    subpulses = models.ManyToManyField(Subpulse)
    additionals = models.ManyToManyField(Additional)
    calculations = models.ManyToManyField(Calculation)
    gammarays = models.ManyToManyField(GammaRayFermi)


