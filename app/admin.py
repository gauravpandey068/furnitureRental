from django.contrib import admin
from app.models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'available')
    list_filter = ('available', 'created_at', 'updated_at')
    search_fields = ['name']


admin.site.register(Product, ProductAdmin)
