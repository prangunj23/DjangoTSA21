from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('main', views.main, name='main'),
    path('login', views.loginuser, name='login'),
    path('register', views.register, name = 'register'),
    path('logout', views.logoutuser, name='logout')
]