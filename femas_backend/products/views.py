from sys import modules

from django.db.models.query import QuerySet
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

non_filter_properties = [
    "__module__",
    "__str__",
    "__doc__",
    "_meta",
    "DoesNotExist",
    "MultipleObjectsReturned",
    "product_id",
    "product",
    "id",
    "objects",
    'photos',
    'videos',
    'versions'
]

allowed_objects = [
    "sofa",
    "bed",
    "table",
    "armchair",
    "chair",
    "kitchenware",
    "accessory",
]


class ObjectListView(generics.ListAPIView):
    filterset_fields = []

    def get_queryset(self):
        object_name = self.kwargs["product_class"][
            : len(self.kwargs["product_class"]) - 1
        ]
        if object_name not in allowed_objects:
            raise Http404
        object_name = object_name.capitalize()
        obj = getattr(modules[__name__], object_name)
        for property in vars(obj):
            if property not in non_filter_properties:
                self.filterset_fields.append(property)
        queryset = obj.objects.all()

        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset

    def get_serializer_class(self):
        object_name = self.kwargs["product_class"][
            : len(self.kwargs["product_class"]) - 1
        ]
        if object_name not in allowed_objects:
            raise Http404
        object_name = object_name.capitalize()
        serializer_name = object_name + "ListSerializer"
        obj = getattr(modules[__name__], serializer_name)
        self.serializer_class = obj
        return self.serializer_class


class ObjectDetailView(generics.RetrieveAPIView):
    lookup_field = 'uuid'

    def get_queryset(self):
        object_name = self.kwargs["product_class"][
            : len(self.kwargs["product_class"]) - 1
        ]
        if object_name not in allowed_objects:
            raise Http404
        object_name = object_name.capitalize()
        obj = getattr(modules[__name__], object_name)
        queryset = obj.objects.all()

        if isinstance(queryset, QuerySet):
            # Ensure queryset is re-evaluated on each request.
            queryset = queryset.all()
        return queryset

    def get_serializer_class(self):
        object_name = self.kwargs["product_class"][
            : len(self.kwargs["product_class"]) - 1
        ]
        if object_name not in allowed_objects:
            raise Http404
        object_name = object_name.capitalize()
        serializer_name = object_name + "DetailSerializer"
        obj = getattr(modules[__name__], serializer_name)
        self.serializer_class = obj
        return self.serializer_class


class AllProductsSearchView(generics.ListAPIView):
    serializer_class = SearchProductsSerializer

    def get_queryset(self):
        name = self.request.query_params.get(
            'name', None)
        q = Sofa.objects.values('uuid', 'name').filter(name__contains=name)
        for object_name in allowed_objects:
            class_name = object_name.capitalize()
            obj = getattr(modules[__name__], class_name)
            q1 = obj.objects.values('uuid', 'name').filter(
                name__contains=name)
            q = q.union(q1)
        return q


class CategoriesListView(APIView):

    def get(self, request, *args, **kwargs):
        categories = [
            {'name': 'диваны',
             'link': 'sofas'},
            {'name': 'кровати',
             'link': 'beds'},
            {'name': 'столы',
             'link': 'tables'},
            {'name': 'кресла',
             'link': 'armchairs'},
            {'name': 'стулья',
             'link': 'chairs'},
            {'name': 'кухонная утварь',
             'link': 'kitchenwares'},
            {'name': 'аксессуары',
             'link': 'accessorys'},
        ]
        return Response(categories)
