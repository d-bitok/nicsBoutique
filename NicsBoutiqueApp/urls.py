from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeMarket, name='Market'),
    path('store/', views.store, name='Store'),
    path('cart/', views.cart, name='Cart'),
    path('checkout/', views.checkout, name='Checkout'),
]