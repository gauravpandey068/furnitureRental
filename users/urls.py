from django.conf.urls import include
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('edit-profile/', views.editProfile, name='edit-profile'),
    path('profile/', views.profile, name='profile'),
]
