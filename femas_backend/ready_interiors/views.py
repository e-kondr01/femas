from rest_framework import generics

from .serializers import *


class InteriorListView(generics.ListAPIView):
    filterset_fields = ['color', 'square', 'room_type']
    queryset = Interior.objects.all()
    serializer_class = InteriorListSerializer


class InteriorDetailView(generics.RetrieveAPIView):
    queryset = Interior.objects.all()
    lookup_field = 'uuid'
    serializer_class = InteriorDetailSerializer
