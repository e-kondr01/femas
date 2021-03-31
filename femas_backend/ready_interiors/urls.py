from django.urls import path

from .views import *

urlpatterns = [
    path('/<str:uuid>', InteriorDetailView.as_view()),
    path('', InteriorListView.as_view()),
]
