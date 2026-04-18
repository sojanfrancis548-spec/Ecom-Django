from django.contrib import admin
from .models import Category, Product, CartItem, Order, OrderItem

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'is_featured', 'category']
    list_filter = ['category', 'is_featured']
    list_editable = ['price', 'stock', 'is_featured']
    search_fields = ['name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'email', 'total', 'status', 'created_at']
    list_filter = ['status']
    list_editable = ['status']

admin.site.register(CartItem)
admin.site.register(OrderItem)
