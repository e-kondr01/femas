from copy import copy

from rest_framework import serializers

from .models import *

default_product_fields = ['uuid', 'name', 'price',
                          'class_name', 'description', 'main_photo']
default_product_detail_fields = [
    'uuid', 'name', 'class_name', 'description',
    'main_photo', 'photos', 'videos']


class PhotoUrlField(serializers.RelatedField):
    """Needed to serialize photo from related object """

    def to_representation(self, instance):
        url = instance.photo.url
        request = self.context.get('request', None)
        if request:
            return request.build_absolute_uri(url)
        return url


class VideoUrlField(serializers.RelatedField):
    """Needed to serialize video from related object """

    def to_representation(self, instance):
        url = instance.video.url
        request = self.context.get('request', None)
        if request:
            return request.build_absolute_uri(url)
        return url


class ProductListSerializer(serializers.ModelSerializer):
    photos = PhotoUrlField(many=True, read_only=True)


class ProductDetailSerializer(serializers.ModelSerializer):
    photos = PhotoUrlField(many=True, read_only=True)
    videos = VideoUrlField(many=True, read_only=True)


class SofaListSerializer(ProductListSerializer):

    class Meta:
        model = Sofa
        fields = copy(default_product_fields)
        fields.extend([
            'mechanism', 'collection',
        ])


class SofaOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SofaOption
        fields = ['uuid', 'size', 'class_name']


class SofaDetailSerializer(ProductDetailSerializer):
    options = SofaOptionSerializer(many=True)

    class Meta:
        model = Sofa
        fields = copy(default_product_detail_fields)
        fields.extend([
            'mechanism', 'collection',
            'options',
        ])


class BedListSerializer(ProductListSerializer):

    class Meta:
        model = Bed
        fields = copy(default_product_fields)
        fields.extend([
            'mechanism', 'size', 'headboard'
        ])


class BedDetailSerializer(ProductDetailSerializer):

    class Meta:
        model = Bed
        fields = copy(default_product_detail_fields)
        fields.extend([
            'mechanism', 'size', 'headboard'
        ])


class TableListSerializer(ProductListSerializer):

    class Meta:
        model = Table
        fields = copy(default_product_fields)
        fields.extend([
            'type', 'collection'
        ])


class TableDetailSerializer(ProductDetailSerializer):

    class Meta:
        model = Table
        fields = copy(default_product_detail_fields)
        fields.extend([
            'type', 'collection'
        ])


class ArmchairListSerializer(ProductListSerializer):

    class Meta:
        model = Armchair
        fields = copy(default_product_fields)
        fields.extend([
            'type'
        ])


class ArmchairDetailSerializer(ProductDetailSerializer):

    class Meta:
        model = Armchair
        fields = copy(default_product_detail_fields)
        fields.extend([
            'type'
        ])


class ChairListSerializer(ProductListSerializer):

    class Meta:
        model = Chair
        fields = copy(default_product_fields)
        fields.extend([
            'type'
        ])


class ChairDetailSerializer(ProductDetailSerializer):

    class Meta:
        model = Chair
        fields = copy(default_product_detail_fields)
        fields.extend([
            'type'
        ])


class KitchenwareListSerializer(ProductListSerializer):

    class Meta:
        model = Kitchenware
        fields = copy(default_product_fields)
        fields.extend([
        ])


class KitchenwareDetailSerializer(ProductDetailSerializer):

    class Meta:
        model = Kitchenware
        fields = copy(default_product_detail_fields)
        fields.extend([
        ])


class AccessoryListSerializer(ProductListSerializer):

    class Meta:
        model = Accessory
        fields = copy(default_product_fields)
        fields.extend([
            'type'
        ])


class AccessoryDetailSerializer(ProductDetailSerializer):

    class Meta:
        model = Accessory
        fields = copy(default_product_detail_fields)
        fields.extend([
            'type'
        ])


class AllProductsSerializer(serializers.Serializer):
    uuid = serializers.CharField()
    name = serializers.CharField()
    main_photo = serializers.CharField()
    class_name = serializers.CharField()

    class Meta:
        fields = ['uuid', 'name', 'main_photo', 'class_name']
