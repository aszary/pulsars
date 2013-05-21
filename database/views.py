# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.core.exceptions import ObjectDoesNotExist

from models import Pulsar, XrayArticle, XrayFit, XrayComponent, Geometry, \
    Subpulse, Additional, Calculation
from atnf import get_page, parse_page
import latex


def index(request):
    """ show x-ray pulsars by default
    """
    return x_ray(request)


def psrs(request, id=None):
    """ show all pulsars
    """
    if id != None:
        psr = Pulsar.objects.get(id=id)
        ads = psr.additionals.all()
        cas = psr.calculations.all()
        sus = psr.subpulses.all()
        ges = psr.geometries.all()
        template = loader.get_template('database/component.xhtml')
        c = Context({'psr':psr, 'cas':cas, 'ads':ads, 'sus':sus, 'ges':ges}, )
        return HttpResponse(template.render(c))
    else:
        psrs = Pulsar.objects.all().order_by('Name')
        template = loader.get_template('database/all.xhtml')
        c = Context({'psrs':psrs,})
        return HttpResponse(template.render(c))


def x_ray(request):
    """ show pulsars with X-ray data
    """
    psrs = Pulsar.objects.filter(xray_articles__num__gte=0).distinct()
    template = loader.get_template('database/x-rays.xhtml')
    c = Context({'psrs':psrs})
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
    # for citealiases
    #all_psrs = Pulsar.objects.all()
    #print_latex.citealiases(all_psrs)
    # data for table
    psrs = Pulsar.objects.exclude(calculations__b__isnull=True).\
        exclude(P0__lt=0.01).\
        order_by('-calculations__b').distinct()
    res = latex.table_bb(psrs)
    return HttpResponse(res, mimetype="text/plain")

def table_psrs(request):
    psrs = Pulsar.objects.filter(xray_articles__fits__ordinal__gt=0).filter(P0__gt=0.01).\
        order_by('RaJD').distinct()
    res = latex.table_psrs(psrs)
    return HttpResponse(res, mimetype="text/plain")

def table_pl(request):
    # sort does not work (multiple lum values for different components)
    #psrs = Pulsar.objects.filter(xray_articles__fits__ordinal__gt=0).\
    #    filter(xray_articles__fits__components__spec_type='PL'). \
    #    distinct().order_by('xray_articles__fits__components__lum')
    comps = XrayComponent.objects.filter(spec_type='PL').\
        filter(xrayfit__ordinal__gt=0).filter(psr_id__P0__gt=0.01).distinct().\
        order_by('-lum')
    # data for table
    psrs = []
    for co in comps:
        print co, co.psr_id
        psrs.append(co.psr_id)
    res = latex.table_pl(psrs)
    return HttpResponse(res, mimetype="text/plain")

