from rest_framework import serializers

from .models import *


class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = [
            'quantity', 'product_id', 'product_option_id',
            'price', 'name', 'product_code'
        ]
        read_only_fields = ['price', 'name', 'product_code']


class OrderSerializer(serializers.ModelSerializer):
    ordered_products = OrderedProductSerializer(
        many=True, queryset=OrderedProduct.objects.all()
    )

    class Meta:
        model = Order
        fields = [
            'name', 'surname', 'phone', 'email',
            'city', 'delivery_address', 'entrance',
            'floor', 'ordered_products',
            'total_price'
        ]
        read_only_fields = ['total_price']
