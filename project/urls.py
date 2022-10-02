from django.urls import path
from . import views

urlpatterns = [
    path('api/list_statistics/', views.list_statistics, name='list_statistics'),
]

