from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer
from products.models import Product
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem


# Create your views here.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'admin':
            return Order.objects.all()
        return Order.objects.filter(customer=user)
#checkout page
def checkout_view(request):
    product_id = request.GET.get('product_id')
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'checkout.html', {'product': product})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    # Check if product already in cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not item_created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('view_cart')  # Redirect to the cart page

@login_required
def view_cart(request):
    cart = Cart.objects.filter(user=request.user).first()
    items = cart.items.all() if cart else []
    return render(request, 'orders/cart.html', {'cart_items': items})
@login_required
def checkout_view(request):
    cart = Cart.objects.filter(user=request.user).first()
    items = cart.items.all() if cart else []
    
    if request.method == "POST":
        # Here you can integrate MPesa API payment
        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone_number')
        address = request.POST.get('address')
        # Process payment logic goes here...
        return redirect('order_success')  # Redirect to success page

    return render(request, 'orders/checkout.html', {'cart_items': items})