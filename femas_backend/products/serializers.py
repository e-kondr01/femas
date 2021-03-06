from rest_framework import serializers

from .models import *

default_product_fields = ['id', 'name', 'description']
default_product_detail_fields = [
    'id', 'name', 'description', 'photos', 'videos']


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


class ProductDetailSerializer(serializers.ModelSerializer):
    photos = PhotoUrlField(many=True, read_only=True)
    videos = VideoUrlField(many=True, read_only=True)


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


class SofaDetailSerializer(ProductDetailSerializer):
    options = SofaOptionSerializer(many=True)

    class Meta:
        model = Sofa
        fields = default_product_detail_fields
        fields.extend([
            'mechanism', 'collection', 'code',
            'options',
        ])
