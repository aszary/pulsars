# Create your views here.
from django.http import HttpResponse
from atnf import get_page, parse_page


def index(request):
    """ show x-ray pulsars by default
    """
    return x_ray(request)


def all_(request):
    """ show all pulsars
    """
    output = 'All pulsars'
    return HttpResponse(output)


def x_ray(request):
    """ show pulsars with X-ray data
    """
    output = 'X-ray pulsars'
    return HttpResponse(output)


def get_atnf(request):
    if False:
        get_page()
        return HttpResponse('ATNF data downloaded successfully..')
    else:
        return HttpResponse('ATNF download disabled! (check views.py)')


def sync_atnf(request):
    parse_page()
    return HttpResponse('ATNF data sync successfully..')
