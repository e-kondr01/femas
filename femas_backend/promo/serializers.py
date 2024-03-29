from rest_framework import serializers

from .models import Promo


class PromoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Promo
        fields = ['uuid', 'title', 'main', 'photo', ]
