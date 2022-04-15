from django.shortcuts import get_object_or_404, render
from .models import Product, ProductCategory


MENU_LINKS = [
    {"url": "main", "active": ["main"], "name": "домой"},
    {"url": "products:all", "active": ["products:all", "products.category"], "name": "продукты"},
    {"url": "contact", "active": ["contact"], "name": "контакты"},
]


def index(request):
    products = Product.objects.all()[:4]
    return render(
        request,
        "mainapp/index.html",
        context={
            "title": "Главная", 
            "menu_links": MENU_LINKS, 
            "products": products
        },
    )


def products(request):
    categories = ProductCategory.objects.all()
    products = Product.objects.all()[:4]
    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            "products": products,
            "menu_links": MENU_LINKS,
            "categories": categories,
        },
    )


def category(request, pk):
    categories = ProductCategory.objects.all()
    category = get_object_or_404(ProductCategory, id=pk)
    products = Product.objects.filter(category=category)
    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты",
            "products": products,
            "menu_links": MENU_LINKS,
            "categories": categories,
        },
    )


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={
            "title": "Контакты",
            "menu_links": MENU_LINKS,
        },
    )
