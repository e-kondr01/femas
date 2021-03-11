from rest_framework import serializers

from .models import *


class ProductSerializer(serializers.ModelSerializer):
    # photos = serializers.SlugRelatedField(
    #     many=True,
    #     slug_field='photo',
    #     read_only=True,
    #     required=False,
    # )
    # videos = serializers.SlugRelatedField(
    #     many=True,
    #     slug_field='video',
    #     read_only=True,
    #     required=False
    #     # нужно ли
    # )
    # По-другому надо

    class Meta:
        model = Product
        fields = [
            'name', 'description',
            ]


class SofaSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = Sofa
        fields = [
            'id', 'product', 'size', 'mechanism',
            'collection', 'code'
        ]
