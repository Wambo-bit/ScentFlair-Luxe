from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    email=models.EmailField('email address')#unique=True)
    ROLE_CHOICES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    )
    role=models.CharField (max_length=20, choices=ROLE_CHOICES, default='customer')
    contact_info=models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

        
    def __str__(self):
        return f"{self.username} ({self.email})"