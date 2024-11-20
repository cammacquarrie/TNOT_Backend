from django.urls import path

from . import api

urlpatterns = [
    path('', api.toys_list, name='api_toy_list'),
    path('<uuid:pk>/', api.toys_detail, name="api_toys_detail"),
]