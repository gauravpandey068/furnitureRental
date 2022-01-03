from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.forms import ProductForm
from app.models import Product


@login_required(login_url='/login/')
@staff_member_required()
def dashboard(request):
    product = Product.objects.all()
    return render(request, 'db_index.html', {"product": product})


@login_required(login_url='/login/')
@staff_member_required()
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # request.FILES is for image
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    else:
        form = ProductForm()

    return render(request, 'add_product.html', {"form": form})
