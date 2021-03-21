from django.urls import path

from .views import *

urlpatterns = [
    path('<str:product_class>', ObjectListView.as_view()),
    path('<str:product_class>/<int:pk>', ObjectDetailView.as_view()),
    path('', AllProductsSearchView.as_view())
]
