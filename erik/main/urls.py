from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('theme', views.theme, name='theme'),
    path('translation', views.translation, name='translation'),
]
