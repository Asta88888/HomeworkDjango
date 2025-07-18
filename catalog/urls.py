from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.apps import CatalogConfig
from catalog.views import ProductListView, ProductDetailView, ProductCreateView, ProductUpdateView, ProductDeleteView, ProductUnpublishView, CategoryListView, CategoryDetailView
from catalog.views import contacts


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),
    path('catalog/contacts/', contacts, name='contacts'),
    path('catalog/<int:pk>', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('catalog/create', ProductCreateView.as_view(), name='product_create'),
    path('catalog/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('catalog/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/unpublish/', ProductUnpublishView.as_view(), name='product_unpublish'),
    path('catalog/category_list', CategoryListView.as_view(), name='category_list'),
    path("catalog/category/<int:pk>/", CategoryDetailView.as_view(), name="category_detail"),

]
