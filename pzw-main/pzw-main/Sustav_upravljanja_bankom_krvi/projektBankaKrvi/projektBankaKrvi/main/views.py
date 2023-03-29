from contextlib import _RedirectStream, redirect_stderr
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from requests import request
from main.models import *

from django.contrib.auth.decorators import login_required
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404

## Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            
            login(request, user)
            
            return redirect('/')
    else:
        form = UserCreationForm()
    
    context = {'form': form}

    return render(request, 'registration/register.html', context) 

def logout(request):
    logout(request)
    return render('login')

##def register_request(request):
##	if request.method == "POST":
##		form = NewUserForm(request.POST)
##		if form.is_valid():
##			user = form.save()
##			login(request, user)
##			messages.success(request, "Registration successful." )
##			return redirect("S")
##		messages.error(request, "Unsuccessful registration. Invalid information.")
##	form = NewUserForm()
##	return render (request=request, template_name="registration/register.html", context={"register_form":form})

##def register(request):
 ##   if request.method == 'POST':
 ##       form = UserCreationForm(request.POST)

 ##       if form.is_valid():
 ##           form.save()
 ##           username = form.cleaned_data['username']
 #           password = form.cleaned_data['password1']
#
  #          user = authenticate(username=username, password=password)
  #          login(request, user)
  #          return redirect_stderr('')

  #  else:
  #      form = UserCreationForm()

   # context = {'form': form}

   # return render(request, 'registration/register.html', context)


def hello_world(request):
    return HttpResponse('Dodajte u adresu <i>/izbornik</i> za izbornik...! <strong>#inf0gang</strong>')
    # primjetiti korištenje HTML-a

class Mosquito(ListView):
    template_name = 'mosquito.html'

    def get_queryset(self):
        return 0

class DonacijeList(ListView):
    template_name = 'donacije_list.html'

    def get_queryset(self):
        return Donacija.objects.all()

class KarticeList(ListView):
    template_name = 'donacijske_kartice_list.html'

    def get_queryset(self):
        return DonacijskaKartica.objects.all()

class DonatoriList(ListView):
    template_name = 'donator_list.html'

    def get_queryset(self):
        return Donator.objects.all()

class KrvnaGrupaList(ListView):
    template_name = 'krvnagrupa_list.html'

    def get_queryset(self):
        return KrvnaGrupa.objects.all()

class PrimateljList(ListView):
    template_name = 'primatelj_list.html'

    def get_queryset(self):
        return Primatelj.objects.all()

class PrimanjeList(ListView):
    template_name = 'primanja_list.html'

    def get_queryset(self):
        return Primatelj.objects.all()

class SpremnikKrviList(ListView):
    template_name = 'spremnik_list.html'

    def get_queryset(self):
        return SpremnikKrvi.objects.all()

