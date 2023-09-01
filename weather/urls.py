from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('about/', views.about, name='about'),
    path('information/', views.information, name='information'),
    path('documentation/', views.doc, name='doc'),
]