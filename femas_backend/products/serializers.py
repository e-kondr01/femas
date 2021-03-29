from rest_framework import serializers

from .models import *

default_product_fields = ['uuid', 'name', 'price', 'description', 'photos']
default_product_detail_fields = [
    'uuid', 'name', 'class_name', 'description', 'photos', 'videos']


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
        fields = default_product_fields
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
        fields = default_product_detail_fields
        fields.extend([
            'mechanism', 'collection',
            'options',
        ])


class SearchProductsSerializer(serializers.Serializer):
    uuid = serializers.CharField()
    name = serializers.CharField()

    class Meta:
        fields = ['uuid', 'name']
