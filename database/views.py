# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.core.exceptions import ObjectDoesNotExist

from models import Pulsar, XrayArticle, XrayFit, XrayComponent, Geometry, \
    Subpulses, Additional, Calculations
from atnf import get_page, parse_page
from latex import table_bb_nondipolar


def index(request):
    """ show x-ray pulsars by default
    """
    return x_ray(request)


def psrs(request, id=None):
    """ show all pulsars
    """
    if id != None:
        psr = Pulsar.objects.get(id=id)
        articles = XrayArticle.objects.filter(psr_id=psr)
        try:
            geometry = Geometry.objects.get(psr_id=psr)
        except ObjectDoesNotExist:
            geometry = None
        try:
            subpulses = Subpulses.objects.get(psr_id=psr)
        except ObjectDoesNotExist:
            subpulses = None
        try:
            additional = Additional.objects.get(psr_id=psr)
        except ObjectDoesNotExist:
            additional = None
        try:
            calculations = Calculations.objects.get(psr_id=psr)
        except ObjectDoesNotExist:
            calculations = None
        fits = []
        components = []
        for article in articles:
            fits += list(XrayFit.objects.filter(article_id=article))
        for fit in fits:
            components += list(XrayComponent.objects.filter(fit_id=fit))
        #template = loader.get_template('database/pulsar.xhtml')
        #template = loader.get_template('database/atnf.xhtml')
        #template = loader.get_template('database/article.xhtml')
        #template = loader.get_template('database/fits.xhtml')
        template = loader.get_template('database/components.xhtml')
        c = Context({'psr':psr, 'articles':articles, 'fits':fits,
                     'components':components, 'g':geometry,
                     's':subpulses, 'a':additional, 'c':calculations }, )
        return HttpResponse(template.render(c))
    else:
        psrs = Pulsar.objects.all().order_by('Name')
        template = loader.get_template('database/all.xhtml')
        c = Context({'psrs':psrs,})
        return HttpResponse(template.render(c))


def x_ray(request):
    """ show pulsars with X-ray data
    """
    fits = XrayFit.objects.filter(ordinal__gt=0).order_by('ordinal')
    psrs = []
    for fit in fits:
        psrs.append(fit.article_id.psr_id)
    # assuming one calc for one pulsar
    calcs = []
    for psr in psrs:
        calcs.append(Calculations.objects.get(psr_id=psr))
    psrs_calcs = zip(psrs, calcs)
    template = loader.get_template('database/x-rays.xhtml')
    c = Context({'psrs_calcs':psrs_calcs})
    return HttpResponse(template.render(c))


def get_atnf(request):
    if False:
        get_page()
        return HttpResponse('ATNF data downloaded successfully..')
    else:
        return HttpResponse('ATNF download disabled! (check views.py)')


def sync_atnf(request):
    parse_page()
    return HttpResponse('ATNF data sync successfully..')

def table_bb(request):
    #comps = XrayComponent.objects.filter(spec_type='BB')
    # fits with BB and ordinal id__in=comps.values_list('fit_id', flat=True)
    # all fits
    fits_all = XrayFit.objects.filter(ordinal__gt=0)
    # all components for ordinal fits
    comps = XrayComponent.objects.filter(fit_id__in=fits_all)
    # fits with ordinal and BB
    fits = XrayFit.objects.filter(id__in=comps.values_list('fit_id', flat=True))
    # articles with BB and ordinal
    artics_sample = XrayArticle.objects.filter(id__in=fits.values_list(
        'article_id', flat=True))
    # psrs with BB and oridinal
    psrs = Pulsar.objects.filter(id__in=
        artics_sample.values_list('psr_id',flat=True))
    # all articles
    artics = XrayArticle.objects.filter(psr_id__in=psrs.values_list('id',
                                                                   flat=True))
    calcs = Calculations.objects.filter(psr_id__in=artics_sample.values_list(
        'psr_id', flat=True)).order_by('-b')


    '''
    psrs = []
    comps = []
    artics = []
    for fit in fits:
        psrs.append(fit.article_id.psr_id)
        print fit.article_id.psr_id
        artics.append(fit.article_id)
        comps.append(XrayComponent.objects.filter(fit_id=fit))
    # assuming one calc for one pulsar
    calcs = []
    for psr in psrs:
        calcs.append(Calculations.objects.get(psr_id=psr))
    print len(fits), len(psrs), len(calcs), len(comps), len(artics)
    '''
    res = table_bb_nondipolar(psrs, fits_all, calcs, comps, artics,
                              artics_sample)
    return HttpResponse(res, mimetype="text/plain")

