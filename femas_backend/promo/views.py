from rest_framework import generics

from .models import Promo
from .serializers import PromoSerializer


class ActivePromoView(generics.ListAPIView):
    queryset = Promo.objects.filter(active=True)
    serializer_class = PromoSerializer
    filterset_fields = []
