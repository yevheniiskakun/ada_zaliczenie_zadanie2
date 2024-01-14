from django.shortcuts import render

#from pages.models import PromotionPhoto, GeneralInfo, GalleryPhoto, FooterSliderImage


def index(request):

    context = {}
    return render(request, 'pages/index.html', context)

