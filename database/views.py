# Create your views here.
from django.http import HttpResponse


def index(request):
    output = 'Hello Database!!'
    return HttpResponse(output)
