"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    # Usuarios
    path('usuarios/', views.listar_usuarios),
    path('usuarios/<str:id>/', views.usuario_por_id),

    # Fichas
    path('fichas/', views.listar_fichas),
    path('fichas/<str:id>/', views.ficha_por_id),

    # Atenciones
    path('atenciones/', views.listar_atenciones),
    path('atenciones/<str:id>/', views.atencion_por_id),
]
