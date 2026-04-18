from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='products'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('cart/', views.cart_view, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/success/<int:pk>/', views.order_success, name='order_success'),

    # Cart API
    path('api/cart/add/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('api/cart/remove/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('api/cart/update/<int:pk>/', views.update_cart, name='update_cart'),
]
