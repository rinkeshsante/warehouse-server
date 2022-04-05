from django.urls import path
from . import api

urlpatterns = [
    path('api/next-task/', api.nextTask, name='next-task'),
]
