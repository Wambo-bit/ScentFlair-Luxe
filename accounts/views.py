from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import RegisterSerializer
from django.http import HttpResponse

# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

#To test the order list page
def order_list(request):
    return HttpResponse("Orders page is working fine!")
