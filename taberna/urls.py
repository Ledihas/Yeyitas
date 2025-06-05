# taberna/urls.py
from django.urls import path
from .views import tabern_home, bebidas_list, specials_list
# Eliminar static de aquí
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'taberna' # ¡Correcto!

urlpatterns = [
    path('ofertasTa/', tabern_home, name='ofertasTa'), # -> taberna:ofertasTa
    path('bebidas/', bebidas_list, name='bebidas'), # -> taberna:bebidas
    path('specials/', specials_list, name='specials'), # -> taberna:specials
]
# if settings.DEBUG: # Eliminar esto de aquí
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)