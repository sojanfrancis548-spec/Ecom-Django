"""
Run: python seed.py
Adds sample categories and products to the database.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ecom_project.settings')
django.setup()

from store.models import Category, Product

# Categories
cats = {
    'electronics': Category.objects.get_or_create(name='Electronics', slug='electronics')[0],
    'fashion': Category.objects.get_or_create(name='Fashion', slug='fashion')[0],
    'home': Category.objects.get_or_create(name='Home & Living', slug='home-living')[0],
    'books': Category.objects.get_or_create(name='Books', slug='books')[0],
}

products = [
    dict(name='Wireless Noise-Cancelling Headphones', category=cats['electronics'],
         description='Premium sound quality with 30-hour battery life. Active noise cancellation for an immersive listening experience.',
         price=2499, original_price=3999,
         image_url='https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=600&q=80',
         stock=15, is_featured=True),

    dict(name='Mechanical Keyboard RGB', category=cats['electronics'],
         description='Tactile typing experience with customizable RGB backlighting. Compatible with Windows and Mac.',
         price=3299, original_price=4500,
         image_url='https://images.unsplash.com/photo-1587829741301-dc798b83add3?w=600&q=80',
         stock=8, is_featured=True),

    dict(name='Smart Watch Pro', category=cats['electronics'],
         description='Track your fitness, receive notifications and monitor your health 24/7. Water resistant up to 50m.',
         price=5999, original_price=7999,
         image_url='https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=600&q=80',
         stock=12, is_featured=True),

    dict(name='Wireless Charging Pad', category=cats['electronics'],
         description='Fast 15W wireless charging for all Qi-compatible devices. Slim design fits any desk.',
         price=899, original_price=1299,
         image_url='https://images.unsplash.com/photo-1609091839311-d5365f9ff1c5?w=600&q=80',
         stock=20),

    dict(name='Premium Cotton T-Shirt', category=cats['fashion'],
         description='100% organic cotton. Breathable fabric perfect for everyday wear. Available in multiple colors.',
         price=599, original_price=999,
         image_url='https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=600&q=80',
         stock=50, is_featured=True),

    dict(name='Classic Denim Jacket', category=cats['fashion'],
         description='Timeless denim jacket with a modern fit. A wardrobe essential for every season.',
         price=1899, original_price=2499,
         image_url='https://images.unsplash.com/photo-1576871337632-b9aef4c17ab9?w=600&q=80',
         stock=18),

    dict(name='Leather Wallet', category=cats['fashion'],
         description='Genuine full-grain leather. Slim profile with 6 card slots and a cash pocket.',
         price=799, original_price=1200,
         image_url='https://images.unsplash.com/photo-1627123424574-724758594e93?w=600&q=80',
         stock=30),

    dict(name='Minimalist Table Lamp', category=cats['home'],
         description='Warm white LED lamp with touch dimmer. Perfect for your bedside or work desk.',
         price=1299, original_price=1799,
         image_url='https://images.unsplash.com/photo-1507473885765-e6ed057f782c?w=600&q=80',
         stock=10),

    dict(name='Ceramic Coffee Mug Set', category=cats['home'],
         description='Set of 4 handcrafted ceramic mugs. Microwave and dishwasher safe. Holds 350ml.',
         price=699, original_price=999,
         image_url='https://images.unsplash.com/photo-1514228742587-6b1558fcca3d?w=600&q=80',
         stock=25),

    dict(name='The Psychology of Money', category=cats['books'],
         description='Morgan Housel explores timeless lessons about wealth, greed, and happiness. A must-read for everyone.',
         price=349, original_price=499,
         image_url='https://images.unsplash.com/photo-1592496431122-2349e0fbc666?w=600&q=80',
         stock=40),

    dict(name='Atomic Habits', category=cats['books'],
         description='James Clear shares proven strategies for building good habits and breaking bad ones.',
         price=329, original_price=450,
         image_url='https://images.unsplash.com/photo-1544716278-ca5e3f4abd8c?w=600&q=80',
         stock=35),

    dict(name='Portable Bluetooth Speaker', category=cats['electronics'],
         description='360° surround sound with 20-hour battery. IPX7 waterproof for outdoor adventures.',
         price=1799, original_price=2499,
         image_url='https://images.unsplash.com/photo-1608043152269-423dbba4e7e1?w=600&q=80',
         stock=14),
]

created = 0
for p in products:
    obj, made = Product.objects.get_or_create(name=p['name'], defaults=p)
    if made:
        created += 1

print(f"✓ Done! {created} products created, {len(products) - created} already existed.")
print(f"  Categories: {Category.objects.count()}")
print(f"  Products:   {Product.objects.count()}")
