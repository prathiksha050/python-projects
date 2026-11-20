from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Product
from .cart import get_cart


def product_list(request):
    products = Product.objects.filter(is_available=True, stock__gt=0)
    return render(request, "shop/product_list.html", {"products": products})


@require_POST
def cart_add(request, product_id):
    product = Product.objects.get(id=product_id)

    cart = request.session.get("shopping_cart", {})
    key = str(product.id)

    if product.is_available and product.stock > cart.get(key, 0):
        cart[key] = cart.get(key, 0) + 1

    request.session["shopping_cart"] = cart
    return redirect("shop:product_list")


def cart_detail(request):
    items, total = get_cart(request)
    return render(request, "shop/cart_detail.html", {
        "items": items,
        "total": total,
    })


@require_POST
def cart_update(request, product_id):
    cart = request.session.get("shopping_cart", {})
    product = Product.objects.get(id=product_id)

    quantity = int(request.POST.get("quantity", 1))

    if quantity <= 0:
        cart.pop(str(product_id), None)
    elif product.is_available:
        cart[str(product_id)] = min(quantity, product.stock)

    request.session["shopping_cart"] = cart
    return redirect("shop:cart_detail")


@require_POST
def cart_remove(request, product_id):
    cart = request.session.get("shopping_cart", {})
    cart.pop(str(product_id), None)

    request.session["shopping_cart"] = cart
    return redirect("shop:cart_detail")