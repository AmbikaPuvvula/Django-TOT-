from django.urls import path
from FormsApp import views

urlpatterns = [
    path('demo/', views.demo, name='demo'),
    path('dhtml/', views.dhtml, name='dhtml'),
    path('read/', views.read, name='read'),
    path('userdata/', views.userdata, name='userdata'),
    # path('registerform/', views.registerform, name='registerform'),
    # path('fetch/', views.fetch, name='fetch'),
    path('', views.home, name='home'),
    path('reg/', views.reg, name='reg'),
    path('details/', views.details, name='details'),
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),
]
