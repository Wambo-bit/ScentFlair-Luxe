from django.db import models
from django.conf import settings
from orders.models import Order

# Create your models here.
class Payment(models.Model):
    ORDER_STATUS_CHOICES=(
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        
    )
    order=models.OneToOneField(Order, related_name='payment', on_delete=models.CASCADE)
    mpesa_number=models.CharField(max_length=20, blank=True, null=True)
    transaction_code=models.CharField(max_length=20, unique=True)
    transaction_date=models.DateTimeField(auto_now_add=True)
    amount=models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    status=models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='pending')
    created_at=models.DateTimeField(auto_now_add=True)
    verified_at=models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"Payment {self.id} - {self.order.id}"


