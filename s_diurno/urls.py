from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'ofert_dia_list'

urlpatterns = [
 path('ofertasD/',views.ofrt_dia_list,name='ofertasD'),
 path('desayuno/',views.desa_list,name='desayuno'),
 path('dia/',views.dia_list,name='dia'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)