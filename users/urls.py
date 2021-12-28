from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('billing-address', views.billingAddress, name='billing-address'),
    path('edit-billing-address', views.edit_billing_address, name='edit-billing-address'),
]
