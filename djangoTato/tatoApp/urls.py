from django.contrib import admin
from django.urls import path
from tatoApp import views
urlpatterns = [
    path('', views.home, name="home"),
    path('contacto/', views.contacto, name="contacto"),
    path('ask/', views.ask, name="ask"),
    path('deleteChat/', views.deleteChat, name="deleteChat"),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
]
