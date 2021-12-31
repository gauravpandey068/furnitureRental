from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.forms import ProductForm, ProductInfoForm


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'db_base.html')


@login_required(login_url='/login/')
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # request.FILES is for image
        if form.is_valid():
            form.save()
            return redirect('add_product_info', )

    else:
        form = ProductForm()

    return render(request, 'add_product.html', {"form": form})


@login_required(login_url='/login/')
def add_product_info(request):
    if request.method == 'POST':
        form = ProductInfoForm(request.POST)
        if form.is_valid():
            print(form)
            return redirect('dashboard')

    else:
        form = ProductInfoForm()
    return render(request, 'add_product_info.html', {"form": form})
