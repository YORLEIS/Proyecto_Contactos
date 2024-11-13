"""
URL configuration for Contactos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic.base import RedirectView
from Aplicaciones.Gestion.views import formularioContacto, contactar, contacto_exitoso

urlpatterns = [
    path('', formularioContacto),
    path('admin/', admin.site.urls),
    path('formularioContacto/', formularioContacto),
    path('contactar/', contactar),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
    path('contacto_exitoso/', contacto_exitoso, name='contacto_exitoso'),  # Note that 'contacto_exitoso' is imported from 'views' in your 'urls.py'
]
