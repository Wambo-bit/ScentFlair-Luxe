from django.contrib import admin
from .models import Payment

# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('transaction_code', 'order', 'mpesa_number', 'amount', 'status', 'created_at')
    list_filter = ('status',)
    search_fields = ('transaction_code', 'mpesa_number')

# Automatically update order when verified
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if obj.status == 'verified':
            obj.order.status = 'paid'
            obj.order.save()
