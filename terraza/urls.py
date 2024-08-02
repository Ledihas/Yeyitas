from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'terraza'

urlpatterns = [
 path('ofertasT/',views.ofert_list,name='ofertasT'),
 path('helados/',views.helados_list,name='helados'),
 path('bebidas/',views.bebidas_list,name='bebidas'),
 path('platos/',views.platos_list,name='platos'),
 

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)