__author__ = 'aszary'

from django.http import HttpResponse


def home(request):
    output = 'Hello Pulsars!!'
    return HttpResponse(output)
