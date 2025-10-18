from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets, permissions
from .models import Order
from .serializers import OrderSerializer
from products.models import Product

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
