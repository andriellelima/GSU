"""gsu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from gsu.base import views as v

app_name = 'base'

urlpatterns = [
    path('',v.home,name='home'),
    path('login/', v.log, name='login'),
    path('logout/', v.sair, name='logout'),
    path('gerenciar/', v.gerenciar, name='gerenciar'),
    path('sugestao/', v.sugestao, name='sugestao'),
    path('sobre/', v.sobre, name='sobre'),
    path('mapa/', v.mapa, name='mapa')

]
