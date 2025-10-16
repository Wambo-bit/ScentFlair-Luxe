from rest_framework import serializers
from .models import Order, OrderItem
from products.serializers import ProductSerializer
from django.db import transaction
from products.models import Product

class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(), 
        write_only=True, 
        source='product')

    class Meta:
        model = OrderItem
        fields = ['id','product','product_id','quantity','price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'customer', 'total_price', 'status', 'created_at', 'items']
        read_only_fields = ['total_price', 'created_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        user = self.context['request'].user

        with transaction.atomic():
            order = Order.objects.create(customer=user, **validated_data)

            for item in items_data:
                product = Product.objects.select_for_update().get(pk=item['product'].id)
#stock verification
                if product.stock_quantity < item['quantity']:
                    raise serializers.ValidationError(
                        f"Not enough stock for {product.name}. Only {product.stock_quantity} left."
                    )

# Deduct stock
                product.stock_quantity -= item['quantity']
                product.save()

# Create order item
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item['quantity'],
                    price=item.get('price', product.price)
                )

# Recalculate total price after adding all items
            order.recalc_total()

            return order
