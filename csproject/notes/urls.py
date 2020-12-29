from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.addUser, name='addUser'),
    path('error/', views.badSessionRequest, name='error'),
    path('add/', views.addNote, name='add'),
]