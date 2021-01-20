from django.urls import path
from RoleApp import views
from django.contrib.auth import views as v
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('updateprofile/', views.updateprofile, name='updateprofile'),
    path('login/', v.LoginView.as_view(template_name='RoleApp/login.html'), name='login'),
    path('logout/', v.LogoutView.as_view(template_name='RoleApp/logout.html'), name='logout'),
]
