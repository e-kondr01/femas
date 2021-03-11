from django.urls import path

from .views import *


urlpatterns = [
    path('sofas', SofaListView.as_view()),
]
