from rest_framework import generics

from .models import *
from .serializers import *


class CreateOrderView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
