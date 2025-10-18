from django.urls import path
from . import views
from products.views import shop_view

urlpatterns = [
    path('', views.home, name='home'),
     path('shop/', shop_view, name='shop'),
     
]


