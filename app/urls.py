from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/add-product/', views.add_product, name='add_product'),
    path('dashboard/add-product/add-product-info/', views.add_product_info, name='add_product_info'),
]
