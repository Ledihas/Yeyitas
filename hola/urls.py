from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'ofertas' 

urlpatterns = [
    path('hi/',hola_mundo),
    path('Home/',Home),
    path('ofertas/',ofertas,name='ofertas'),
    path('a_nombre/',a_nombre,name='a_nombre'),
    path('exito/',exito,name='exito'),
  
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)