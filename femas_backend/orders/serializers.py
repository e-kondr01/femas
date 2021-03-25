from sys import modules

from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *


class RetrieveOrderedProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderedProduct
        fields = ['name', 'price', 'quantity', ]


class CreateOrderedProductSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()
    class_name = serializers.CharField()

    class Meta:
        model = OrderedProduct
        fields = [
            'quantity', 'id', 'class_name']


class RetrieveOrderSerializer(serializers.ModelSerializer):
    products = RetrieveOrderedProductSerializer(
        many=True
    )

    class Meta:
        model = Order
        fields = ['id',
                  'name', 'surname', 'phone', 'email',
                  'city', 'delivery_address', 'entrance',
                  'floor',
                  'total_price',
                  'products'
                  ]


class CreateOrderSerializer(serializers.ModelSerializer):
    ordered_products = CreateOrderedProductSerializer(
        many=True, required=False
    )

    class Meta:
        model = Order
        fields = [
            'name', 'surname', 'phone', 'email',
            'city', 'delivery_address', 'entrance',
            'floor',
            'ordered_products',
        ]

    def create(self, validated_data):
        ordered_products_data = validated_data.pop('ordered_products', [])
        if not ordered_products_data:
            raise ValidationError({'error': 'must include ordered products'})
        order = Order.objects.create(**validated_data)
        for ordered_product in ordered_products_data:
            id = ordered_product.pop('id')
            class_name = ordered_product.pop('class_name')
            if "Option" in class_name:
                product_option_class = getattr(modules[__name__], class_name)
                product_object = product_option_class.objects.get(
                    pk=id).product
                product_version = product_object.versions.get(current=True)
                OrderedProduct.objects.create(
                    product_version=product_version,
                    order=order,
                    option_id=id,
                    **ordered_product)
            else:
                product_class = getattr(modules[__name__], class_name)
                product_object = product_class.objects.get(pk=id)
                if product_object.has_options():
                    raise ValidationError(
                        {'error': ('Cannot order product with unspecified '
                                   'options, as it has options')})
                product_version = product_object.versions.get(current=True)
                OrderedProduct.objects.create(
                    product_version=product_version,
                    order=order, **ordered_product)
        return order
