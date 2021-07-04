from django.contrib import admin
from django.urls import path, include
from . import views
from .views import main_view

urlpatterns = [
    path('',views.index),
    path('en/',views.indexen),
    path('client/',views.client),
    path('admin/',views.admin),
    path('ref', main_view, name='main-view'),
    path('ref/<str:ref_code>', main_view, name='main-view'),
]
