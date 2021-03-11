from rest_framework import generics

from .models import *
from .serializers import *


class SofaListView(generics.ListAPIView):
    queryset = Sofa.objects.all()
    serializer_class = SofaSerializer
    filterset_fields = ['size', 'mechanism', 'collection']


class BedListView(generics.ListAPIView):
    queryset = Bed.objects.all()
    serializer_class = SofaSerializer
    filterset_fields = ['size', 'mechanism', 'headboard']


class TableListView(generics.ListAPIView):
    queryset = Sofa.objects.all()
    serializer_class = SofaSerializer
    filterset_fields = ['size', 'mechanism', 'collection']


class SofaListView(generics.ListAPIView):
    queryset = Sofa.objects.all()
    serializer_class = SofaSerializer
    filterset_fields = ['size', 'mechanism', 'collection']

class SofaListView(generics.ListAPIView):
    queryset = Sofa.objects.all()
    serializer_class = SofaSerializer
    filterset_fields = ['size', 'mechanism', 'collection']


class SofaListView(generics.ListAPIView):
    queryset = Sofa.objects.all()
    serializer_class = SofaSerializer
    filterset_fields = ['size', 'mechanism', 'collection']


class SofaListView(generics.ListAPIView):
    queryset = Sofa.objects.all()
    serializer_class = SofaSerializer
    filterset_fields = ['size', 'mechanism', 'collection']