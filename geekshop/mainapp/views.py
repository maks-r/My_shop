import json
from django.shortcuts import render


MENU_LINKS = [
    {'url': 'main', 'name': 'домой'},
    {'url': 'products', 'name': 'продукты'},
    {'url': 'contact', 'name': 'контакты'}
]


def index(request):
    return render(request, 'mainapp/index.html', context={
        'title': 'Главная',
        'menu_links': MENU_LINKS
    })


def products(request):
    # with open('./products.json', 'r') as file:
    #     products = json.load(file)
    products = [
    {
        "name": "Стул повышенного качества",
        "description": "Не оторваться",
        "image": "img/product-11.jpg"
    },
    {
        "name": "Стул повышенного качества 2",
        "description": "Супер стул",
        "image": "img/product-21.jpg"
    },
    {
        "name": "Стул повышенного качества 3",
        "description": "Классно",
        "image": "product-31.jpg"
    }
]
    return render(request, 'mainapp/products.html', context={
        'title': 'Продукты',
        'products': products,
        'menu_links': MENU_LINKS
    })


def contact(request):
    return render(request, 'mainapp/contact.html', context={
        'title': 'Контакты',
        'menu_links': MENU_LINKS
    })