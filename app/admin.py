from django.contrib import admin
from app.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'brand', 'available')
    list_filter = ('available', 'brand', 'created_at', 'updated_at')
    search_fields = ['name', 'brand']


admin.site.register(Product, ProductAdmin)

