from django.shortcuts import render
from .models import *


def tabern_home(request):
    
    return render(request, 'tabern_home.html')



def ofrt_tab_list(request):
    ofertas = OfrtTab.objects.all()
    return render(request, 'ofrt_tab_list.html', {'ofertas': ofertas})


def bebidas_list(request):
    ofertas = Bebidas.objects.all()
    return render(request, 'ofrt_tab_list.html', {'ofertas': ofertas})


def specials_list(request):
    ofertas = Specials.objects.all()
    return render(request, 'ofrt_tab_list.html', {'ofertas': ofertas})
