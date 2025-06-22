from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home
from catalog.views import contacts
from catalog.views import products_list
from catalog.views import product_detail


app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('products_list/', products_list, name='products_list'),
    path('product_detail/<int:pk>', product_detail, name='product_detail')
]
