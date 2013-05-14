# Create your views here.
from django.http import HttpResponse
from atnf import get_page


def index(request):
    """ show x-ray pulsars by default
    """
    return x_ray(request)


def all(request):
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
    get_page()
    return HttpResponse('ATNF data downloaded successfully..')