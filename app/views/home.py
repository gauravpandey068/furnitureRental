from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render, redirect

from app.decorators import user_information_required
from app.forms import RentForm
from app.forms.comment import CommentForm
from app.models import Product, Rent, Comment


def home(request):
    products = Product.objects.all().order_by('?')
    new_products = Product.objects.all().order_by('created_at')[:5]
    context = {
        'products': products,
        'new_products': new_products
    }
    return render(request, 'index.html', context)


def products_detail(request, product_id):

    product = Product.objects.get(id=product_id)
    all_products = Product.objects.all().order_by('?')[:5]
    comments = Comment.objects.filter(product=product_id)

    if request.method == 'POST':
        form = CommentForm(request.POST, initial={'product': product, 'user': request.user.pk})
        if request.user:
            if form.is_valid():
                form.save()
                return redirect('product_detail', product_id)
        else:
            redirect('login')
    else:
        form = CommentForm(initial={'product': product, 'user': request.user.pk})

    context = {
        'product': product,
        'all_products': all_products,
        'form': form,
        'comments': comments
    }
    return render(request, 'products_detail.html', context)


@login_required(login_url='login')
@user_information_required
def rent(request, product_id):
    request_product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = RentForm(request.POST, initial={'product': request_product, 'user': request.user.pk})
        if form.is_valid():
            rents = form.save(commit=False)
            rents.rental_day = int((rents.end_date - rents.start_date).days)
            rents.total_price = rents.rental_day * request_product.price * rents.quantity
            rents.save()
            return redirect('index')
        else:
            messages.error(request, form.errors)

    else:
        product = request_product.pk
        user = request.user.pk

        form = RentForm(initial={'product': product, 'user': user})

    return render(request, 'rent_form.html', {'form': form})


@login_required(login_url='login')
def my_rent_products(request):
    rents = Rent.objects.filter(user=request.user).order_by('created_at')
    return render(request, 'my_rent_products.html', {'rents': rents})


@login_required(login_url='login')
def cancel_rent(request, rent_id):
    rents = Rent.objects.get(id=rent_id)
    rents.delete()
    return redirect('my_rent_products')


@login_required(login_url='login')
def return_request(request, rent_id):
    rents = Rent.objects.get(id=rent_id)
    rents.status = 'returned'
    rents.save()
    return redirect('my_rent_products')


def search(request):
    query = request.GET.get('query')
    if not query:
        return redirect('index')
    else:
        products = Product.objects.annotate(search=SearchVector('name', 'brand')).filter(search=query)
    context = {
        'products': products,
        'query': query
    }
    return render(request, 'search.html', context)


@login_required(login_url='login')
def delete_comment(request, comment_id):
    user = request.user
    comment = Comment.objects.get(id=comment_id, user=user)
    comment.delete()
    return redirect('product_detail', comment.product.id)
