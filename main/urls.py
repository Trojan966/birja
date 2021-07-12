
from django.urls import path
from . import views
from .views import main_view

urlpatterns = [
    path('',views.index),
    path('ru/',views.indexen),
    path('fr/',views.indexfra),
    path('pl/',views.indexpol),
    path('tr/',views.indextr),
    path('client/',views.client),
    path('admin/',views.admin),
    path('ref', main_view, name='main-view'),
    path('ref/<str:ref_code>', main_view, name='main-view'),
    path('admin/balance', views.balance),
    path('nft/', views.nft, name='NFT'),
    path('app',views.app,name='app')

]
