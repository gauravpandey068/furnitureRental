from django.shortcuts import render
from app.models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def products_detail(request, product_id):
    product = Product.objects.get(id=product_id)

    return render(request, 'products_detail.html', {'product': product})
