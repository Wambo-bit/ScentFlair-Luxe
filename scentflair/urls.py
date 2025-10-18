from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, CategoryViewSet
from orders.views import OrderViewSet
from accounts.views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse
from products.views import shop_view, product_detail
from orders.views import checkout_view
from django.conf import settings
from django.conf.urls.static import static


# Home view
def home(request):
    return JsonResponse({
        "message": "Welcome to the ScentFlair API!",
        "available_endpoints": [
            "/api/auth/register/",
            "/api/auth/login/",
            "/api/auth/token/refresh/",
            "/api/products/",
            "/api/orders/",
            "/api/categories/"
        ]
    })

# Routers for API endpoints
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)

# URL patterns
urlpatterns = [
    path('', home, name='home'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/payments/', include('payments.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/products/', include('products.urls')),
    path('shop/', shop_view, name='shop'),
    path('shop/', shop_view, name='shop'),
    path('product/<int:pk>/', product_detail, name='product-detail'),
    path('checkout/', checkout_view, name='checkout'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
