from django.contrib import admin
from django.urls import path
from tatoApp import views
urlpatterns = [
    path('', views.home, name="home"),
    path('contacto/', views.contacto, name="contacto")
]
