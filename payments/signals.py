from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Payment
from django.core.mail import send_mail

@receiver(post_save, sender=Payment)
def send_payment_confirmation(sender, instance, **kwargs):
    if instance.status == 'verified':
        send_mail(
            'Payment Verified - ScentFlair Luxe',
            f'Dear {instance.order.customer.username}, your payment {instance.transaction_code} of Ksh {instance.amount} has been confirmed. Thank you!',
            'noreply@scentflairluxe.com',
            [instance.order.customer.email],
            fail_silently=True
        )
