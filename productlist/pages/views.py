from django.shortcuts import render

from .models import Product


def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'pages/index.html', context)

def add_product(request):
    context = {}
    return render(request, 'pages/index.html', context)

def delete_product(request, id):
    Product.objects.filter(id=id).delete()
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'pages/index.html', context)


def mark_product(request):
    context = {}
    return render(request, 'pages/index.html', context)
