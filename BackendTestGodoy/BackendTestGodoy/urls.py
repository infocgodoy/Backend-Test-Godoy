"""BackendTestGodoy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from gestionClientes import views

urlpatterns = [
    path('<int:pk>', views.product_detail, name='detail'),
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('login_respuesta/', views.login_res),
    path('ingresar_pedido/', views.login_res),
    path('nuevo_menu/', views.menus_v),
    path('modificar_menu/', views.modificar_menus_v),
    path('nuevos_platos/', views.platos_v),
    path('ver_pedidos/', views.ver_pedidos_v),
    path('enviar_menu/', views.enviar_menu_v),
    path('solo_menu/9b1deb3d-3b7d-4bsd-9zdd-2b0d7b3dcb6d', views.solo_menu_v), 
    
]
