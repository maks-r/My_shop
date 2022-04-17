from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from adminapp.utils import superuser_required
from django.utils.decorators import method_decorator
from django.http.response import HttpResponseRedirect
from django.urls import reverse, reverse_lazy


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product/edit.html'
    fields = '__all__'

    @method_decorator(superuser_required())
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {
            'category': self.get_category()
        }
    
    def get_success_url(self):
        return reverse('admin:products', kwargs=self.kwargs)

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_category
        return context



@superuser_required()
def products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category=category).order_by('id')

    return render(request, 'adminapp/product/products.html', context={
        'title': 'Продукты',
        'category': category,
        'objects': products
    })


@superuser_required()
def product_read(request):
    pass


@superuser_required()
def product_update(request):
    pass


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'adminapp/product/delete.html'
    success_url = reverse_lazy('admin:products')

    def delete(self, request, *arg, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Удаление продукта"
        return context