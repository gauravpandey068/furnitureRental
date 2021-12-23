from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from users.forms import UserForm, UserInformationForm
from users.models import UserInformation


def register(request):

    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:

        form = UserForm()

    return render(request, 'register.html', {"form": form})


@login_required(login_url='login')
def profile(request):

    username = request.user.username
    email = request.user.email
    first_name = request.user.first_name
    last_name = request.user.last_name

    if UserInformation.objects.filter(user=request.user).exists():
        phone = request.user.userinformation.phone
        address = request.user.userinformation.delivery_address
    else:
        phone = ''
        address = ''

    name = first_name + ' ' + last_name

    data = {}
    data['username'] = username
    data['email'] = email
    data['name'] = name
    data['phone'] = phone
    data['address'] = address

    return render(request, 'profile.html', data)


@login_required(login_url='login')
def editProfile(request):

    if request.method == "POST":
        pass
    else:
        form = UserInformationForm()

    return render(request, 'edit_profile.html',  {"form": form})
