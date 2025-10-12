from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=255)
    slug=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    image=models.ImageField(upload_to='categories/', blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def__str__(self):
        return self.name

class Product(models.Model):
    SIZE_CHOICES=(
        ('15ml', '15ml'), ('30ml', '30ml'), ('50ml','50ml')
    )
    name=models.CharField(max_length=255)
    description=models.CharField(max_length=255)
    category=models.ForeignKey(category, on_delete=models.CASCADE, related_name='products')
    price=models.DecimalField(max_digits=10, decimal_places=2)
    size=models.CharField(max_length=10, choices=SIZE_CHOICES))
    scent=
