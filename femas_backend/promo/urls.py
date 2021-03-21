from django.urls import path

from .views import *

urlpatterns = [
    path('/active', ActivePromoView.as_view()),
]
