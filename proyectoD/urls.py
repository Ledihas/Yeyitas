"""
URL configuration for proyectoD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from hola import views
import s_diurno
from django.conf import settings
from django.conf.urls.static import static
import accounts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home),
    path('s_diurno/', include('s_diurno.urls',namespace='s_diurno')),
    path('s_diurno/', include('s_diurno.urls',namespace='desayuno')),
    path('s_diurno/', include('s_diurno.urls',namespace='dia')),
    path('ofertas/',include('hola.urls',namespace='ofertas')),
    path('a_nombre/',include('hola.urls',namespace='a_nombre')),
    path('terraza/',include('terraza.urls')),
    path('taberna/',include('taberna.urls',namespace='ofertasTa')),
    path('taberna/',include('taberna.urls',namespace='bebidas')),
    path('taberna/',include('taberna.urls',namespace='specials')),
    path('evento/',include('evento.urls')),
    path('evento/',include('evento.urls',namespace='reserva')),
    path('nosotros/', views.nosotros),
    path('contacto/', views.contacto),
    path('jefeLog/',views.vista_login),
    path('adminSite/',views.login_supUser),
    path('evento/',include('evento.urls',namespace='reservas')),
    path('logout/',views.logout),
    path('accounts/', include('accounts.urls', namespace= 'accounts')),
   # path('evento/', include('evento.urls')),  # Asumiendo que existe una app 'evento'
    #path('', include('hola.urls')),  # O la app que maneje la home
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)