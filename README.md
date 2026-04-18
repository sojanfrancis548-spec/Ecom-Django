# LUXE — Django Ecommerce Store 🛍

A full-featured ecommerce web app built with Django. Luxury aesthetic, complete shopping flow.

## Features
- 🏠 **Home page** — Hero banner, featured products, categories
- 🛒 **Shop** — Browse, filter by category, search products
- 📄 **Product detail** — Full page with related products
- 🛍 **Cart** — Add/remove/update quantities (session-based, no login needed)
- 💳 **Checkout** — Order form with confirmation
- ✅ **Order success** — Summary with order ID
- 🔧 **Admin panel** — Manage products, categories, orders

## Project Structure
```
ecom_project/
├── ecom_project/
│   ├── settings.py
│   └── urls.py
├── store/
│   ├── models.py       ← Product, Category, Cart, Order
│   ├── views.py        ← All page + cart API views
│   ├── urls.py         ← URL routing
│   ├── admin.py        ← Admin config
│   └── templates/store/
│       ├── base.html
│       ├── home.html
│       ├── products.html
│       ├── product_detail.html
│       ├── cart.html
│       ├── checkout.html
│       └── order_success.html
├── seed.py             ← Sample data loader
└── manage.py
```

## Setup & Run

```bash
# 1. Install dependency
pip install django

# 2. Run migrations
python manage.py migrate

# 3. Load sample products
python seed.py

# 4. Create admin user
python manage.py createsuperuser

# 5. Start server
python manage.py runserver
```

## URLs
| URL | Page |
|-----|------|
| `/` | Home |
| `/products/` | All Products |
| `/products/?category=electronics` | Filter by category |
| `/products/?q=headphone` | Search |
| `/products/<id>/` | Product Detail |
| `/cart/` | Shopping Cart |
| `/checkout/` | Checkout |
| `/admin/` | Admin Panel |

## Admin Login
- URL: `http://127.0.0.1:8000/admin/`
- Username: `admin`
- Password: `admin123`

## Safe for GitHub ✅
No API keys, no secrets. Just Django + SQLite.
