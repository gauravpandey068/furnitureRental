from django import forms

from app.models import Product, ProductInfo


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price',
            'image',
        ]


class ProductInfoForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), widget=forms.HiddenInput())
    stock = forms.IntegerField()
    available = forms.BooleanField(initial=True)

    class Meta:
        model = ProductInfo
        fields = [
            'product',
            'stock',
            'available',
        ]
