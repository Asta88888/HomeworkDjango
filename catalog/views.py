from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from catalog.forms import ProductForm
from catalog.models import Product, Category
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalog.services import get_products_from_cache, get_products_by_category


class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return get_products_from_cache()


class ProductDetailView(DetailView):
    model = Product


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.create_product'


    def form_valid(self, form):
        product = form.save(commit=False)
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.change_product'

    def form_valid(self, form):
        product = form.instance
        if product.owner != self.request.user:
            return HttpResponseForbidden("Нет прав на редактирование.")
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

    def delete(self, request, *args, **kwargs):
        product = self.get_object()
        if not (product.owner == request.user or request.user.has_perm('catalog.delete_product')):
            return HttpResponseForbidden("Нет прав на удаление.")
        return super().delete(request, *args, **kwargs)


def contacts(request):
    return render(request, 'catalog/contacts.html')


class ProductUnpublishView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.publication_flag = False
        product.save()
        return redirect('catalog:product_detail', pk=pk)


class CategoryListView(ListView):
    model = Category


class CategoryDetailView(DetailView):
    model = Category

    def get_queryset(self):
        pk = self.objects.id
        return get_products_by_category(pk)