from django.urls import path, include
from.import views
from ous.models import Author
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.log),
    path('logout/', views.exit),
    path('registration/', views.registration),
    path('registrationpage/', views.reg_view),
    path('add_obzor/', views.add_obzor),
    path('aobzor/', views.aobzor),
    path('add_article/', views.add_article),
    path('addarticle/', views.addarticle),
    path('info/', views.info),
    path('profile/', views.profile),
    path('del_article/', views.del_article),





]
