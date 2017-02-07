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


def show_product(request, product_slug):
    print(product_slug)
    product = get_object_or_404(Product, slug=product_slug)
    print(product)
    context = {
        'product': product
    }
    return render(request,'product/product.html', context)


def show_category(request, category_slug):
    product = get_object_or_404(Category, slug=category_slug)
    context = {
        'category': category.slug
    }
    return render(request,'product/category.html', context)