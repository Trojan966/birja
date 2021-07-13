
from django.urls import path
from . import views
from .views import main_view, RegisterView, VerifView

urlpatterns = [
    path('',views.index),
    path('en/',views.indexen),
    path('client/',views.client),
    path('admin/',views.admin),
    path('ref', main_view, name='main-view'),
    path('ref/<str:ref_code>', main_view, name='main-view'),
    path('admin/balance', views.balance),
    path('nft/', views.nft, name='NFT'),
    path('reg', RegisterView.as_view(), name='Регистрация'),
    path('verif', VerifView.as_view(), name='Верификация')
]