from django.urls import path

from .views import *


urlpatterns = [
    path('<str:product_class>', ObjectListView.as_view()),
]
