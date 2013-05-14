__author__ = 'aszary'

from django.http import HttpResponse
from django.template import Context, loader


def home(request):
    template = loader.get_template('pulsars/hello.xhtml')
    c = Context()
    return HttpResponse(template.render(c))
