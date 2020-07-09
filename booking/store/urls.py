from django.urls import path
from . import views

# Urls patterns

urlpatterns = [
    # base.html
    path('', views.store, name='store'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout')
]
