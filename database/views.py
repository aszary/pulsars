# Create your views here.
from django.http import HttpResponse
from django.template import Context, loader

from models import Pulsar, XrayArticle
from atnf import get_page, parse_page


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
        print articles
        #template = loader.get_template('database/pulsar.xhtml')
        #template = loader.get_template('database/atnf.xhtml')
        template = loader.get_template('database/article.xhtml')
        c = Context({'psr':psr, 'articles':articles}, )
        return HttpResponse(template.render(c))
    else:
        psrs = Pulsar.objects.all()
        template = loader.get_template('database/all.xhtml')
        c = Context({'psrs':psrs,})
        return HttpResponse(template.render(c))


def x_ray(request):
    """ show pulsars with X-ray data
    """
    output = 'X-ray pulsars'
    articles = XrayArticle.objects.filter(num=0)
    psrs = []
    for article in articles:
        psrs.append(article.psr_id)
    print psrs
    template = loader.get_template('database/x-rays.xhtml')
    c = Context({'psrs':psrs,})
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
