from django.shortcuts import render
from .models import *

def ofrt_dia_list(request):
    
    return render(request, 'diurno_home.html')

def dia_list(request):
    ofertas = OfrtDia.objects.all()
    return render(request, 'ofrt_dia_list.html', {'ofertas': ofertas})

def desa_list(request):
    ofertas = OfrtDesa.objects.all()
    return render(request, 'ofrt_dia_list.html', {'ofertas': ofertas})
