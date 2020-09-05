from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('show/<str:pk>/', views.show, name='show'),
    path('new_show/', views.createShow, name='create_show'),
    path('update_show/<str:pk>/', views.updateShow, name='update_show'),
    path('delete_show/<str:pk>/', views.deleteShow, name='delete_show'),
    path('new_spent/<str:pk>/', views.createSpent, name='create_spent'),
    path('<str:pk1>/update_spent/<str:pk2>/', views.updateSpent, name='update_spent'),
    path('<str:pk1>/delete_spent/<str:pk2>/', views.deleteSpent, name='delete_spent'),

]
