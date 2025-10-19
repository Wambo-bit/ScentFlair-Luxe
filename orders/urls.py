from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrderViewSet
from .views import add_to_cart, view_cart, checkout_view

router = DefaultRouter()
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', view_cart, name='view_cart'),
    path('checkout/', checkout_view, name='checkout'),
]

