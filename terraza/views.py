from django.shortcuts import render
from .models import *

def ofert_list(request):
    
    return render(request, 'terra_home.html')
    

def helados_list(request):
    ofertas=Helados.objects.all()
    return render(request, 'ofrt_terra_list.html', {'ofertas': ofertas})


def bebidas_list(request):
    ofertas=Bebidas.objects.all()
    return render(request, 'ofrt_terra_list.html', {'ofertas': ofertas})


def platos_list(request):
    ofertas=Platos.objects.all()
    return render(request, 'ofrt_terra_list.html', {'ofertas': ofertas})
