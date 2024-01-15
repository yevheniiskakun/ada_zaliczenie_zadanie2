from django.shortcuts import render

from .models import Product


def index(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'pages/index.html', context)

def add_product(request):
    if request.method == 'POST':
        print(request.POST.get('new_product'))
        '''
        form = MyForm(request.POST)

        print(form['my_field'].value())
        print(form.data['my_field'])

        if form.is_valid():
            print(form.cleaned_data['my_field'])
            print(form.instance.my_field)
            form.save()
        '''
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'pages/index.html', context)

def delete_product(request, id):
    Product.objects.filter(id=id).delete()
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'pages/index.html', context)


def mark_product(request, id):
    modified_product = Product.objects.get(id=id)
    if modified_product.buyed == False:
        modified_product.buyed = True  # change field
    else:
        modified_product.buyed = False  # change field
    modified_product.save()  # this will update only
    products = Product.objects.all()
    context = {"products": products}
    return render(request, 'pages/index.html', context)
