from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.views.decorators.http import require_POST
from .models import Product, Category, CartItem, Order, OrderItem
import json


def get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def get_cart_count(request):
    sk = get_session_key(request)
    return CartItem.objects.filter(session_key=sk).count()


def home(request):
    featured = Product.objects.filter(is_featured=True, stock__gt=0)[:4]
    all_products = Product.objects.filter(stock__gt=0)[:12]
    categories = Category.objects.all()
    return render(request, 'store/home.html', {
        'featured': featured,
        'products': all_products,
        'categories': categories,
        'cart_count': get_cart_count(request),
    })


def product_list(request):
    products = Product.objects.filter(stock__gt=0)
    category_slug = request.GET.get('category')
    search = request.GET.get('q', '')
    categories = Category.objects.all()
    active_category = None

    if category_slug:
        active_category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=active_category)

    if search:
        products = products.filter(name__icontains=search)

    return render(request, 'store/products.html', {
        'products': products,
        'categories': categories,
        'active_category': active_category,
        'search': search,
        'cart_count': get_cart_count(request),
    })


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    related = Product.objects.filter(category=product.category).exclude(pk=pk)[:4]
    return render(request, 'store/product_detail.html', {
        'product': product,
        'related': related,
        'cart_count': get_cart_count(request),
    })


def cart_view(request):
    sk = get_session_key(request)
    items = CartItem.objects.filter(session_key=sk).select_related('product')
    total = sum(item.subtotal for item in items)
    return render(request, 'store/cart.html', {
        'items': items,
        'total': total,
        'cart_count': items.count(),
    })


def checkout(request):
    sk = get_session_key(request)
    items = CartItem.objects.filter(session_key=sk).select_related('product')
    if not items.exists():
        return redirect('cart')
    total = sum(item.subtotal for item in items)

    if request.method == 'POST':
        order = Order.objects.create(
            session_key=sk,
            full_name=request.POST.get('full_name'),
            email=request.POST.get('email'),
            address=request.POST.get('address'),
            total=total,
        )
        for item in items:
            OrderItem.objects.create(
                order=order,
                product=item.product,
                product_name=item.product.name,
                price=item.product.price,
                quantity=item.quantity,
            )
        items.delete()
        return redirect('order_success', pk=order.id)

    return render(request, 'store/checkout.html', {
        'items': items,
        'total': total,
        'cart_count': items.count(),
    })


def order_success(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'store/order_success.html', {'order': order, 'cart_count': 0})


@require_POST
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    sk = get_session_key(request)
    item, created = CartItem.objects.get_or_create(session_key=sk, product=product)
    if not created:
        item.quantity += 1
        item.save()
    count = CartItem.objects.filter(session_key=sk).count()
    return JsonResponse({'success': True, 'cart_count': count, 'message': f'{product.name} added to cart!'})


@require_POST
def remove_from_cart(request, pk):
    sk = get_session_key(request)
    CartItem.objects.filter(session_key=sk, product_id=pk).delete()
    items = CartItem.objects.filter(session_key=sk).select_related('product')
    total = sum(item.subtotal for item in items)
    return JsonResponse({'success': True, 'cart_count': items.count(), 'total': float(total)})


@require_POST
def update_cart(request, pk):
    sk = get_session_key(request)
    data = json.loads(request.body)
    qty = int(data.get('quantity', 1))
    if qty < 1:
        CartItem.objects.filter(session_key=sk, product_id=pk).delete()
    else:
        CartItem.objects.filter(session_key=sk, product_id=pk).update(quantity=qty)
    items = CartItem.objects.filter(session_key=sk).select_related('product')
    total = sum(item.subtotal for item in items)
    return JsonResponse({'success': True, 'cart_count': items.count(), 'total': float(total)})
