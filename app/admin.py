from django.contrib import admin
from app.models import Product, ProductInfo


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('price', 'created_at', 'updated_at')
    search_fields = ['name']


class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ('product', 'stock', 'available')
    list_filter = ('stock', 'available')
    search_fields = ['product']


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInfo, ProductInfoAdmin)
