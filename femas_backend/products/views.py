from rest_framework import generics

from .models import *
from .serializers import *


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
