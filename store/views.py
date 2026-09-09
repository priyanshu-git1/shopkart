# from django.shortcuts import render, redirect

# # PRODUCTS = {
# #     "Laptop": 50000,
# #     "Mobile": 20000,
# #     "Headphones": 2000,
# # }
# def products(request):
#     product_list = [
#         {"name": "Laptop", "price": 50000},
#         {"name": "Mobile", "price": 20000},
#         {"name": "Headphones", "price": 2000},
#     ]

#     cart = request.session.get('cart', {})
#     cart_count = sum(cart.values()) if isinstance(cart, dict) else len(cart)

#     return render(request, 'store/products.html', {
#         "products": product_list,
#         "cart_count": cart_count
#     })
# def home(request):
#     return render(request, 'store/home.html')

# def products(request):
#     cart = request.session.get('cart', {})
#     cart_count = sum(cart.values()) if isinstance(cart, dict) else len(cart)

#     return render(request, 'store/products.html', {
#         "products": PRODUCTS,
#         "cart_count": cart_count
#     })

# def add_to_cart(request, product_name):
#     cart = request.session.get('cart', {})

#     if isinstance(cart, list):
#         new_cart = {}
#         for item in cart:
#             if item in new_cart:
#                 new_cart[item] += 1
#             else:
#                 new_cart[item] = 1
#         cart = new_cart

#     if product_name in cart:
#         cart[product_name] += 1
#     else:
#         cart[product_name] = 1

#     request.session['cart'] = cart
#     request.session.modified = True

#     return redirect('/products/')

# def cart(request):
#     cart = request.session.get('cart', {})
#     if isinstance(cart, list):
#         new_cart = {}
#         for item in cart:
#             if item in new_cart:
#                 new_cart[item] += 1
#             else:
#                 new_cart[item] = 1
#         cart = new_cart
#         request.session['cart'] = cart
#         request.session.modified = True

#     price_map = {p["name"]: p["price"] for p in PRODUCTS}
#     total_price = 0

#     for item, qty in cart.items():
#         total_price += price_map.get(item, 0) * qty

#     return render(request, 'store/cart.html', {
#         'cart': cart,
#         'total_price': total_price
#     })

# def clear_cart(request):
#     request.session['cart'] = {}
#     request.session.modified = True
#     return redirect('/cart/')

# def remove_item(request, product_name):
#     cart = request.session.get('cart', {})

#     if product_name in cart:
#         del cart[product_name]

#     request.session['cart'] = cart
#     request.session.modified = True

#     return redirect('/cart/')

# def increase_qty(request, product_name):
#     cart = request.session.get('cart', {})

#     if product_name in cart:
#         cart[product_name] += 1

#     request.session['cart'] = cart
#     request.session.modified = True

#     return redirect('/cart/')


# def decrease_qty(request, product_name):
#     cart = request.session.get('cart', {})

#     if product_name in cart:
#         cart[product_name] -= 1

#         if cart[product_name] <= 0:
#             del cart[product_name]

#     request.session['cart'] = cart
#     request.session.modified = True

#     return redirect('/cart/')

# def cart(request):
#     cart = request.session.get('cart', {})

#     total_price = 0
#     total_items = 0

#     for item, qty in cart.items():
#         price = PRODUCTS.get(item, 0)
#         total_price += price * qty
#         total_items += qty

#     return render(request, 'store/cart.html', {
#         "cart": cart,
#         "total_price": total_price,
#         "total_items": total_items
#     })

from django.shortcuts import render, redirect

PRODUCTS = {
    "Laptop": 50000,
    "Mobile": 20000,
    "Headphones": 2000,
}


def home(request):
    return render(request, 'store/home.html')


def products(request):
    product_list = [
        {"name": "Laptop", "price": 50000},
        {"name": "Mobile", "price": 20000},
        {"name": "Headphones", "price": 2000},
    ]

    cart = request.session.get('cart', {})
    cart_count = sum(cart.values()) if isinstance(cart, dict) else len(cart)

    return render(request, 'store/products.html', {
        "products": product_list,
        "cart_count": cart_count
    })


def add_to_cart(request, product_name):
    cart = request.session.get('cart', {})

    if isinstance(cart, list):
        new_cart = {}
        for item in cart:
            if item in new_cart:
                new_cart[item] += 1
            else:
                new_cart[item] = 1
        cart = new_cart

    if product_name in cart:
        cart[product_name] += 1
    else:
        cart[product_name] = 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('/products/')


def cart(request):
    cart = request.session.get('cart', {})

    if isinstance(cart, list):
        new_cart = {}
        for item in cart:
            if item in new_cart:
                new_cart[item] += 1
            else:
                new_cart[item] = 1
        cart = new_cart
        request.session['cart'] = cart
        request.session.modified = True

    total_price = 0
    total_items = 0

    for item, qty in cart.items():
        price = PRODUCTS.get(item, 0)
        total_price += price * qty
        total_items += qty

    return render(request, 'store/cart.html', {
        "cart": cart,
        "total_price": total_price,
        "total_items": total_items
    })


def clear_cart(request):
    request.session['cart'] = {}
    request.session.modified = True
    return redirect('/cart/')


def remove_item(request, product_name):
    cart = request.session.get('cart', {})

    if product_name in cart:
        del cart[product_name]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('/cart/')


def increase_qty(request, product_name):
    cart = request.session.get('cart', {})

    if product_name in cart:
        cart[product_name] += 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('/cart/')


def decrease_qty(request, product_name):
    cart = request.session.get('cart', {})

    if product_name in cart:
        cart[product_name] -= 1

        if cart[product_name] <= 0:
            del cart[product_name]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('/cart/')