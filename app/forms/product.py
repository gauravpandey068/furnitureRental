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
    class Meta:
        model = ProductInfo
        fields = [
            'product',
            'stock',
            'available',
        ]
