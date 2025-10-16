from django.shortcuts import render
from rest_framework import viewsets, permissions, filters
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from django.http import HttpResponse


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAdminUser] 

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
 #Add search, ordering, and filtering backends   
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]

# Fields that can be filtered 
    filterset_fields = ['category', 'size']

#Fields that can be searched
    search_fields = ['name','scent_notes']

#Fields that can be ordered
    ordering_fields = ['price','name']

#Permission handling
    def get_permissions(self):
        if self.action in ['list','retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
def home(request):
    return HttpResponse("Welcome to ScentFlair Luxe!")