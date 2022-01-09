from django import forms
from django.contrib.auth.models import User

from app.models import Product
from app.models import Rent


class RentForm(forms.ModelForm):

    user = forms.ModelChoiceField(queryset=User.objects.all(), required=True, widget=forms.HiddenInput())
    product = forms.ModelChoiceField(queryset=Product.objects.all(), required=True, widget=forms.HiddenInput())
    status = forms.ChoiceField(choices=Rent.Status.choices, required=True, widget=forms.HiddenInput())
    rental_day = forms.IntegerField(widget=forms.HiddenInput())
    total_price = forms.IntegerField(widget=forms.HiddenInput())
    is_returned = forms.BooleanField(widget=forms.HiddenInput())
    start_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2022, 2023)))
    end_date = forms.DateField(widget=forms.SelectDateWidget(years=range(2022, 2023)))

    class Meta:
        model = Rent
        fields = ['user', 'product', 'quantity', 'start_date', 'end_date',
                  'status', 'rental_day', 'total_price', 'is_returned']

