from django.shortcuts import render

#from pages.models import PromotionPhoto, GeneralInfo, GalleryPhoto, FooterSliderImage


def index(request):
    context = {}
    return render(request, 'pages/index.html', context)

def add_product(request):
    context = {}
    return render(request, 'pages/index.html', context)

def delete_product(request):
    context = {}
    return render(request, 'pages/index.html', context)


def mark_product(request):
    context = {}
    return render(request, 'pages/index.html', context)
