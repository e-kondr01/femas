from django.db.models import query
from django.db.models.query import QuerySet
from rest_framework import generics, status
from rest_framework.response import Response
from sys import modules

from .models import *
from .serializers import *


non_filter_properties = [
    '__module__', '__str__', '__doc__',
    '_meta', 'DoesNotExist', 'MultipleObjectsReturned',
    'proudct_id', 'product', 'id', 'objects'
]

allowed_objects = [
    'sofa', 'bed', 'table',
    'armchair', 'chair', 'kitchenware',
    'accessory'
]


class ObjectListView(generics.ListAPIView):
    filterset_fields = []

    def get_queryset(self):
        object_name = self.kwargs['product_class'][:len(self.kwargs['product_class'])-1]
        if object_name not in allowed_objects:
            content = {'please move along': 'nothing to see here'}
            return Product.objects.none()
        object_name = object_name.capitalize()
        obj = getattr(modules[__name__], object_name)
        temp = vars(obj)
        for property in vars(obj):
            if property not in non_filter_properties:
                self.filterset_fields.append(property)
        queryset = obj.objects.all()

        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset

    def get_serializer_class(self):
        object_name = self.kwargs['product_class'][:len(self.kwargs['product_class'])-1]
        if object_name not in allowed_objects:
            content = {'please move along': 'nothing to see here'}
            return ProductSerializer
        object_name = object_name.capitalize()
        serializer_name = object_name + 'Serializer'
        obj = getattr(modules[__name__], serializer_name)
        self.serializer_class = obj

        return self.serializer_class
