from django.contrib import admin
from django.urls import path,include
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('login/', views.login, name = 'login'),
    path('register/', views.register, name= 'register'),
    path('logout/', views.user_logout, name='logout'),
]
