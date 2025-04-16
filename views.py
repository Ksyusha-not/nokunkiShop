from django.shortcuts import render
from .models import Product


def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def login_view(request):
    return render(request, 'myshop/log-in.html')

def register_view(request):
    return render(request, 'register.html')
