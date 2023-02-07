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
from django.urls import path
from Proyectofinal.views import Index, Nosotros, Vende
from aplicacion1.views import creacion_producto, lista_productos, update_product, ProductDeleteView
from ventas.views import creacion_orden
from users.views import login_user, register, update_user, update_profile
from django.contrib.auth.views import LogoutView
from Proyectofinal.settings import MEDIA_ROOT, MEDIA_URL
from django.conf.urls.static import static



urlpatterns = [
    path('', Index, name='index'),
    path('admin/', admin.site.urls),
    path("nosotros/",Nosotros ),
    path("creacionproducto/", creacion_producto),
    path("Lista-Productos/", lista_productos),
    path("Vende tu producto/", Vende ),
    path("compra/", creacion_orden ),
    path("Login/", login_user, name="login"),
    path("Logout/", LogoutView.as_view(template_name="users/logout.html" )),
    path("Singup/", register),
    path("Update/", update_user),
    path("Update_Profile/", update_profile),
    path("Update_Product/<int:pk>/", update_product),
    path("Delete_Product/<int:pk>/", ProductDeleteView.as_view(), name="delete_product"),
    

    
] + static(MEDIA_URL, document_root = MEDIA_ROOT)

