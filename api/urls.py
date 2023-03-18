from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('portInformation/',PortInformation.as_view()),
    # path('employee/',EmployeeView.as_view()),
    path('image/',ImageView.as_view()),
    path('document/',DocumentView.as_view()),
    path('employee/personalinfo/', EmployeeView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('employee/personalinfo/<int:pk>', EmployeeView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
    path('employee/port/', PortView.as_view({
        'get': 'list',
    })),
]
