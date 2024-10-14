from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

app_name = 'taberna' 

urlpatterns = [
    path('ofertasTa/',tabern_home,name='ofertasTa'),
    path('bebidas/',bebidas_list,name='bebidas'),
    path('specials/',specials_list,name='specials'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)