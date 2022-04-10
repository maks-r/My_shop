from django.shortcuts import render
from .models import Product, ProductCategory


MENU_LINKS = [
    {"url": "main", "name": "домой"},
    {"url": "mainapp:products", "name": "продукты"},
    {"url": "contact", "name": "контакты"},
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
    categories = ProductCategory.objects.all()[:4]
    return render(
        request,
        "mainapp/products.html",
        context={
            "title": "Продукты", 
            "products": [], 
            "menu_links": MENU_LINKS,
            "categories": categories 
            },
    )


def  category(request, pk):
    return products(request)


def contact(request):
    return render(
        request,
        "mainapp/contact.html",
        context={
            "title": "Контакты",
            "menu_links": MENU_LINKS,
        },
    )