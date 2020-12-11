"""Sample URL Configuration

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
from django.urls import path, include
from SampleApp import views
from SampleApp_2 import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home),
    path('about/', views.about),
    path('msg/<str:name>/', views.mesg),
    path('data/<str:name>/<int:num>/', views.data),
    path('table/<int:n>/', views.table),
    path('details/<str:name>/<int:n>/', views.details),
    path('dcss/', views.samplecss),
    path('login/', views.login),
    path('register/', views.register),
    path('djs/', views.samplejs),
    path('jstask/', views.jstask),
    path('', v.home),
    path('bstp/', v.bootstrap),
    path('bst/', v.bst),
    path('log-in/', v.login),
    path('reg/', v.reg),
    path('crud/', include('CrudApp.urls')),
]
