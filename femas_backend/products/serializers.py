from rest_framework import serializers

from .models import *

default_product_fields = ['id', 'name', 'description']


class SofaListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sofa
        fields = default_product_fields
        fields.extend([
            'mechanism', 'collection', 'code',
        ])


class SofaOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SofaOption
        fields = ['id', 'size']


class SofaDetailSerializer(serializers.ModelSerializer):
    options = SofaOptionSerializer(many=True)

    class Meta:
        model = Sofa
        fields = default_product_fields
        fields.extend([
            'mechanism', 'collection', 'code',
            'options',
        ])
