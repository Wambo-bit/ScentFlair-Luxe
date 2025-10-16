from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Payment
from .serializers import PaymentSerializer
from orders.models import Order


# Create your views here.
class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        order_id = self.request.data.get('order')
        try:
            order = Order.objects.get(id=order_id, customer=self.request.user)
            serializer.save(order=order, status='pending')
            order.status = 'awaiting_payment'
            order.save()
        except Order.DoesNotExist:
            raise serializers.ValidationError("Invalid order ID or unauthorized access.")
