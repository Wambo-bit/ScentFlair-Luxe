from itertools import product
from django.db import models
from django.conf import settings
from products.models import Product

# Create your models here.
class Order(models.Model):
    STATUS_CHOICES=(
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('shipped', 'Shipped'),
        ('delivered', 'Delivered') ,
        
    )
    customer=models.ForeignKey(settings.AUTH_USER_MODEL,  on_delete=models.CASCADE, related_name='orders')
    total_price=models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def recalc_total(self):
        total=sum([item.quantity * item.price for item in self.items.all()])
        self.total_price=total
        self.save()
        return total

        def __str__(self):
            return f"Order {self.id} - {self.customer.username}"

class OrderItem(models.Model):
    order=models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE, related_name='order_items')
    quantity= models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if not self.price:
            self.price = self.product.price
        super().save(*args, **kwargs)
   
