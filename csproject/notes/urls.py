from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.addUser, name='addUser'),
    path('error/', views.error, name='error'),
    path('note/', views.note, name='note'),
]