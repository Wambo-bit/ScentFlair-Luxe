from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from products.models import Product
from .models import Order, Payment


def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})

    # If product is already in cart, increase quantity
    if str(product_id) in cart:
        cart[str(product_id)]['quantity'] += 1
    else:
        cart[str(product_id)] = {
            'name': product.name,
            'price': float(product.price),
            'quantity': 1,
            'image': product.image.url if product.image else ''
        }

    request.session['cart'] = cart
    return redirect('view_cart')


def view_cart(request):
    cart = request.session.get('cart', {})
    cart_items = []
    grand_total = 0

    for product_id, item in cart.items():
        item_total = item['price'] * item['quantity']
        cart_items.append({
            'product_id': product_id,
            'name': item['name'],
            'price': item['price'],
            'quantity': item['quantity'],
            'image': item['image'],
            'total': item_total
        })
        grand_total += item_total

    return render(request, 'cart/cart.html', {
        'cart_items': cart_items,
        'grand_total': grand_total,
    })


def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('view_cart')


@login_required
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return redirect('view_cart')

    total = sum(item['price'] * item['quantity'] for item in cart.values())

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        address = request.POST.get('address')
        mpesa_number = request.POST.get('mpesa_number')
        transaction_code = request.POST.get('transaction_code')

        if not all([full_name, phone_number, address, mpesa_number, transaction_code]):
            return render(request, 'cart/checkout.html', {
                'cart_items': cart,
                'total': total,
                'error': 'Please fill in all fields.'
            })

        # Create the order
        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            phone_number=phone_number,
            address=address,
            date_created=timezone.now()
        )

        # Save payment details
        Payment.objects.create(
            order=order,
            mpesa_number=mpesa_number,
            transaction_code=transaction_code,
            amount=total,
            confirmed=False
        )

        # Clear session cart
        request.session['cart'] = {}

        return render(request, 'cart/checkout_success.html', {'order': order})

    return render(request, 'cart/checkout.html', {'cart_items': cart, 'total': total})
