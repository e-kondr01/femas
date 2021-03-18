from django.urls import path

from .views import *

urlpatterns = [
    path('', CreateOrderView.as_view()),
]
