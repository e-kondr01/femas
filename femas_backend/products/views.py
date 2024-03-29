from sys import modules

from django.db.models.query import QuerySet
from django.http import Http404
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *
from .product_class_names import allowed_objects

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
    'versions',
    'main_photo'
]

host = 'https://e-kondr01.ru'


class ObjectListView(generics.ListAPIView):
    filterset_fields = []

    def get_queryset(self):
        self.filterset_fields = []
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
    serializer_class = AllProductsSerializer

    def get_queryset(self):
        name = self.request.query_params.get(
            'name', None)
        queryset = []
        for object_name in allowed_objects:
            class_name = object_name.capitalize()
            klass = getattr(modules[__name__], class_name)
            if name:
                objects = list(klass.objects.values(
                    'uuid', 'name', 'main_photo').filter(
                    name__contains=name))
            else:
                objects = klass.objects.values('uuid', 'name', 'main_photo')
            for obj in objects:
                obj['class_name'] = class_name
            queryset.extend(objects)
        return queryset


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
