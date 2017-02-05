from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from product.models import Product, Category


def products(request):
    prod = Product.objects.all()

    context = {
        'products': prod
    }
    return render(request,'product/products.html',context)

def home(request):
    prod = Product.objects.all()
    categ = Category.objects.all()
    context = {
        'products' : prod,
        'categories':categ
    }
    return render(request, 'product/home.html', context)

def categories(request):
    categ = Category.objects.all()
    context = {

        'categories': categ
    }
    return render(request, 'product/categories.html',context)


def show_product(request):
    product = get_object_or_404(Product)
    context = {
        'slug': product.slug
    }
    return render(request,'product/product.html', product.slug)
