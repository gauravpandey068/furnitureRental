from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from app.forms import ProductForm, ProductInfoForm
from app.models import Product


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'db_base.html')


@login_required(login_url='/login/')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # request.FILES is for image
        if form.is_valid():
            pk = form.save()
            product_id = pk.id
            return HttpResponseRedirect(f'{product_id}/add-product-info')

    else:
        form = ProductForm()

    return render(request, 'add_product.html', {"form": form})


@login_required(login_url='/login/')
def add_product_info(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = ProductInfoForm(initial={'product': product.id})
    return render(request, 'add_product_info.html', {"form": form, "product": product}, )
