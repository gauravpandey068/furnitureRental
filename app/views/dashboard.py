from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from app.forms import ProductForm
from app.models import Product, Rent


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


@login_required(login_url='/login/')
@staff_member_required()
def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.delete()
    return redirect('dashboard')


@login_required(login_url='/login/')
@staff_member_required()
def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)  # request.FILES is for image
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']
            price = form.cleaned_data['price']
            image = form.cleaned_data['image']  # bug
            brand = form.cleaned_data['brand']
            available = form.cleaned_data['available']

            Product.objects.filter(id=product_id).update(name=name, description=description, price=price, image=image,
                                                         brand=brand, available=available)
            return redirect('dashboard')

    else:
        form = ProductForm(instance=product)

    return render(request, 'add_product.html', {"form": form})


@login_required(login_url='login')
@staff_member_required()
def pending_rent_requests(request):
    rent_request = Rent.objects.filter(status='pending')

    context = {
        'rent_request': rent_request
    }
    return render(request, 'pending_rent_requests.html', context)


@login_required(login_url='login')
@staff_member_required()
def accept_rent_request(request, rent_id):
    rent = Rent.objects.get(id=rent_id)
    rent.status = 'rented'
    rent.save()
    return redirect('pending_rent_requests')


@login_required(login_url='login')
@staff_member_required()
def reject_rent_request(request, rent_id):
    rent = Rent.objects.get(id=rent_id)
    rent.status = 'rejected'
    rent.save()
    return redirect('pending_rent_requests')
