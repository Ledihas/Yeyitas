from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'evento' 

urlpatterns = [
    path('eventos/',eventos_list,name='eventos'),
    path('reservas/',show_reservas, name='reservas'),
    path('delete_r/',delete_res,name='delete_r'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)