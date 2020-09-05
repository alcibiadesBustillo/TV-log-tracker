from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('show/<str:pk>/', views.show, name='show'),
    path('new_show/', views.createShow, name='create_show'),
    path('new_spent/<str:pk>/', views.createSpent, name='create_spent'),

]
