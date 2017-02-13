
from django.conf.urls import url
from django.contrib import admin


from product.views import products, home, categories, show_product, show_category

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^categories/', categories, name='categories'),
    url(r'^product/(?P<product_slug>[\w-]+)/$', show_product, name='product_detail'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', show_category, name='category_detail'),
    url(r'^category/(?P<category_slug>[\w-]+)/(?P<product_slug>[\w-]+)/$', show_product, name='product_detail')

    # url(r'^category/(?P<category_slug>[\w-]+)/(?P<product_slug>[\w-]+)/$', show_product, name='product_detail'),
    # url(r'^category/(?P<category_slug>[\w-]+)/$', show_category, name='category_detail'),
     # url(r'^product/(?P<category_slug>[\w-]+)/(?P<product_slug>[\w-]+)/$', show_category, name='product_detail')

]
