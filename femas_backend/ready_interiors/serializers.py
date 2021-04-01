from rest_framework import serializers

from .models import *


class PhotoUrlField(serializers.RelatedField):
    """Needed to serialize photo from related object """

    def to_representation(self, instance):
        url = instance.photo.url
        request = self.context.get('request', None)
        if request:
            return request.build_absolute_uri(url)
        return url


class InteriorListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Interior
        fields = ['uuid', 'name', 'main_photo']


class InteriorDetailSerializer(serializers.ModelSerializer):
    photos = PhotoUrlField(many=True, read_only=True)

    class Meta:
        model = Interior
        fields = ['uuid', 'name', 'color', 'square',
                  'room_type', 'main_photo', 'photos']
