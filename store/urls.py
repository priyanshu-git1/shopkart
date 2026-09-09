from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.products, name='products'),
    path('add-to-cart/<str:product_name>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart, name='cart'),
    path('clear-cart/', views.clear_cart, name='clear_cart'),
    path('remove-item/<str:product_name>/', views.remove_item, name='remove_item'),
    path('increase/<str:product_name>/', views.increase_qty, name='increase_qty'),
    path('decrease/<str:product_name>/', views.decrease_qty, name='decrease_qty'),
]