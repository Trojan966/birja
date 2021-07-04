from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.index),
    path('en/',views.indexen),
    path('client/',views.client),
    path('admin/',views.admin)
]
