"""Proyectofinal URL Configuration

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
from django.urls import path, include

from Proyectofinal.views import Index, Nosotros, Vende
from aplicacion1.views import creacion_producto, lista_productos
from compras.views import creacion_orden


urlpatterns = [
    path('', Index, name='index'),
    path('admin/', admin.site.urls),
    path("nosotros/",Nosotros ),
    path("creacionproducto/", creacion_producto),
    path("Lista-Productos/", lista_productos),
    path("Ordenes/", creacion_orden),
    path("Vende tu producto/", Vende )
    
]
