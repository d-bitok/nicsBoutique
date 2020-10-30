from django.shortcuts import render
from .models import *

def homeMarket(request):
    return render(request, 'NicsBoutiqueApp/base.html', {})

def store(request):
    products = Product.objects.all()
    context = {'Products':products}
    return render(request, 'NicsBoutiqueApp/store.html', context)

def cart(request):
    return render(request, 'NicsBoutiqueApp/cart.html', {})

def checkout(request):
    return render(request, 'NicsBoutiqueApp/checkout.html', {})