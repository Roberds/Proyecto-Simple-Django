"""sprojectdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from core import views as core_views
from portfolio import views as portfolio_views

from django.conf import settings 

#Enlazamos nuestras views con una dirección
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', core_views.index, name='index'),
    path('about-me', core_views.about, name='about-me'),
    path('portfolio', portfolio_views.portfolio, name='portfolio'),
    path('contact', core_views.contact, name='contact'),
]


#Django no puede subir ficheros media en modo DEBUG, solo en servidor de produccion
#como algo temportal con el modo debug

#cargar el módulo de ficheros estáticos genérico y hacer que Django sirva ficheros como algo excepcional

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, 
        document_root=settings.MEDIA_ROOT)
