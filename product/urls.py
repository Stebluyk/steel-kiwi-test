"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin


from product.views import products, home, categories, show_product, show_category

urlpatterns = [
    url(r'^$',home,name='home' ),
    url(r'^products/',products,name='products' ),
    url(r'^categories/',categories,name='categories' ),
    url(r'^product/(?P<product_slug>[\w-]+)/$', show_product, name='product_detail'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', show_category, name='category_detail')#,
    #url(r'^category/(?P<category_slug>[\w-]+)/(?P<product_slug>[\w-]+)/$', show_category, show_product, name='product_detail')
]
