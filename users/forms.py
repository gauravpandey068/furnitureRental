from typing import Text
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username',
                  'email', 'password1', 'password2')


class UserInformationForm(forms.Form):
    phone = forms.CharField(max_length=10, required=True, label='Phone Number')
    delivery_address = forms.CharField(
        max_length=100, required=True, label='Delivery Address')