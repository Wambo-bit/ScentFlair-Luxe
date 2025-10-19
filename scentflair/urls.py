from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet, CategoryViewSet, shop_view, product_detail
from orders.views import OrderViewSet, checkout_view
from accounts.views import RegisterView, register_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.http import JsonResponse
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

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
            "/api/categories/",
            "/api/cart/"
        ]
    })

# Routers for API endpoints
router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'orders', OrderViewSet)

# URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),

    # Root / API
    path('', home, name='home'),
    path('api/', include(router.urls)),
    path('api/auth/register/', RegisterView.as_view(), name='register'),
    path('api/auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/payments/', include('payments.urls')),
    path('api/accounts/', include('accounts.urls')),
    path('api/orders/', include('orders.urls')),
    path('api/products/', include('products.urls')),
    path('api/cart/', include('cart.urls')),

    # Frontend pages
    path('shop/', shop_view, name='shop'),
    path('product/<int:pk>/', product_detail, name='product-detail'),
    path('checkout/', checkout_view, name='checkout'),

    # Accounts (login, logout, register)
    path('accounts/login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('accounts/register/', register_view, name='register'),
]

# Include browser reload only in DEBUG mode
if settings.DEBUG:
    urlpatterns += [
        path("__reload__/", include("django_browser_reload.urls")),
        path('media/<path:path>/', include(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))),
    ]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
