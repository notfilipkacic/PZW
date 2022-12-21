from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from main.models import *

## Create your views here.
def hello_world(request):
    return HttpResponse('Hello world! <strong>#inf0gang</strong>')
    # primjetiti korištenje HTML-a

class Mosquito(ListView):
    template_name = 'mosquito.html'

    def get_queryset(self):
        return 0

class DonacijeList(ListView):
    template_name = 'donacije_list.html'

    def get_queryset(self):
        return 0

class KarticeList(ListView):
    template_name = 'donacijske_kartice_list.html'

    def get_queryset(self):
        return 0

class DonatoriList(ListView):
    template_name = 'donator_list.html'

    def get_queryset(self):
        return 0

class KrvnaGrupaList(ListView):
    template_name = 'krvnagrupa_list.html'

    def get_queryset(self):
        return 0

class PrimateljList(ListView):
    template_name = 'primatelj_list.html'

    def get_queryset(self):
        return 0

class SpremnikKrviList(ListView):
    template_name = 'spremnik_list.html'

    def get_queryset(self):
        return 0