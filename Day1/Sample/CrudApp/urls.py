from django.urls import path
from CrudApp.views import addstudent, read, delete, update, createstu, readstu, updatestu, deletestu

urlpatterns = [
    path('addstudent/', addstudent, name='addstudent'),
    path('read/', read, name='read'),
    path('update/<int:id>', update, name='update'),
    path('delete/<int:id>', delete, name='delete'),
    path('createstu/', createstu, name='createstu'),
    path('readstu/', readstu, name='readstu'),
    path('updatestu/<int:id>', updatestu, name='updatestu'),
    path('deletestu/<int:id>', deletestu, name='deletestu'),
]
