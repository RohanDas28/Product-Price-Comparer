from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('results',views.results, name="results"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('services',views.services, name="services"),
    
]