# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader
from django.core.exceptions import ObjectDoesNotExist

from models import Pulsar, XrayArticle, XrayFit, XrayComponent, Geometry, \
    Subpulse, Additional, Calculation
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
    psrs = Pulsar.objects.exclude(calculations__b__isnull=True).distinct()
    res = table_bb_nondipolar(psrs)
    return HttpResponse(res, mimetype="text/plain")

