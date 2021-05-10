from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path ('', views.index,name='index'),
    path('login/', views.user_login,name='login'),
    path('special/', views.special,name='special'),
    path('home/', views.home,name='home'),
    path('pro/', views.pro,name='pro')
    ]