from .views import *
from django.urls import path


urlpatterns = [
    path('personalinfo/', PersonalInfoAPI.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('personalinfo/<int:pk>', PersonalInfoAPI.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
]
