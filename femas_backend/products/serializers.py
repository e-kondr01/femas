from rest_framework import serializers

from .models import *


class ProductOptionChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductOptionChoice
        fields = ['id', 'name']


class ProductOptionSerializer(serializers.ModelSerializer):
    choices = ProductOptionChoiceSerializer(many=True)

    class Meta:
        model = ProductOption
        fields = ['id', 'name', 'choices']


class ProductSerializer(serializers.ModelSerializer):
    options = ProductOptionSerializer(many=True, required=False)
    photos = serializers.SlugRelatedField(
        many=True,
        slug_field='photo',
        read_only=True,
        required=False,
    )
    videos = serializers.SlugRelatedField(
        many=True,
        slug_field='video',
        read_only=True,
        required=False
        # нужно ли
    )
    # По-другому надо

    class Meta:
        model = Product
        fields = [
            'id', 'name', 'description', 'photos', 'videos', 'options'
            ]
