from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    slug=models.CharField(max_length=255, unique=True)
    description=models.TextField(max_length=255)
    image=models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.name

 

class Product(models.Model):
    SIZE_CHOICES=(
        ('15ml', '15ml'), ('30ml', '30ml'), ('50ml','50ml')
    )
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    category=models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    price=models.DecimalField(max_digits=10, decimal_places=2)
    size=models.CharField(max_length=10, choices=SIZE_CHOICES)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    stock_quantity = models.PositiveIntegerField(default=0)
    scent_notes = models.CharField(max_length=255, blank=True, null=True) 

    class Meta:
        indexes = [
            models.Index(fields=['name']),
            models.Index(fields=['category']),
        ]

    def __str__(self):
        return self.name

    
