from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required(login_url='/login/')
def dashboard(request):
    return render(request, 'db_base.html')


@login_required(login_url='/login/')
def add_product(request):
    return render(request, 'add_product.html')
