from django.shortcuts import render
from .models import menubar, Product


def index(request):
    Menus = menubar.objects.all()
    Products = Product.objects.all()
    return render(request, 'Products/index.html', {'menus': Menus, 'products': Products})


