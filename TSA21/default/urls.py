from django.urls import path

from . import views

urlpatterns = [
    path('default', views.index, name='index'),
]