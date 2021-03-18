from sys import modules

from rest_framework import serializers

from .models import *


class OrderedProductSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    class_name = serializers.CharField()

    class Meta:
        model = OrderedProduct
        fields = [
            'quantity', 'product_id', 'class_name']


class OrderedProductOptionSerializer(serializers.ModelSerializer):
    option_id = serializers.IntegerField()
    class_name = serializers.CharField()

    class Meta:
        model = OrderedProductOption
        fields = [
            'quantity', 'option_id', 'class_name']


class OrderSerializer(serializers.ModelSerializer):
    ordered_products = OrderedProductSerializer(
        many=True, required=False
    )
    ordered_product_options = OrderedProductOptionSerializer(
        many=True, required=False
    )

    class Meta:
        model = Order
        fields = [
            'name', 'surname', 'phone', 'email',
            'city', 'delivery_address', 'entrance',
            'floor',
            'ordered_products', 'ordered_product_options',
            'total_price'
        ]
        read_only_fields = ['total_price']

    def create(self, validated_data):
        ordered_products_data = validated_data.pop('ordered_products', [])
        ordered_options_data = validated_data.pop(
            'ordered_product_options_data', [])
        order = Order.objects.create(**validated_data)
        for ordered_product in ordered_products_data:
            product_id = ordered_product.pop('product_id')
            class_name = ordered_product.pop('class_name')
            product_class = getattr(modules[__name__], class_name)
            product_object = product_class.objects.get(pk=product_id)
            product_version = product_object.versions.get(current=True)
            OrderedProduct.objects.create(
                product_version=product_version,
                order=order, **ordered_product)
        for ordered_option in ordered_options_data:
            option_id = ordered_option.pop('option_id')
            class_name = ordered_option.pop('class_name')
            option_class = getattr(modules[__name__], class_name)
            option_object = option_class.objects.get(pk=option_id)
            option_version = option_object.versions.get(current=True)
            OrderedProductOption.objects.create(
                product_option_version=option_version,
                order=order,
                **ordered_option)
        return order
