from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/add-product/', views.add_product, name='add_product'),
    path('dashboard/product/delete/<int:product_id>/', views.delete_product, name='delete_product'),
    path('dashboard/product/edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('home/<int:product_id>/', views.products_detail, name='product_detail'),
    path('home/rent/<int:product_id>/', views.rent, name='rent'),
    path('home/rent/my-rent-products/', views.my_rent_products, name='my_rent_products'),
    path('home/rent/my-rent-products/cancel-product/<int:rent_id>/', views.cancel_rent, name='cancel_rent'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
