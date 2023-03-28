from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('portInformation/', PortInformation.as_view()),
    # path('employee/',EmployeeView.as_view()),
    path('image/', ImageView.as_view()),
    path('document/', DocumentAPIView.as_view({
<<<<<<< HEAD
        'get': 'list',
        'post': 'create'
    })),
=======
'get':'list', 'post':'create'
})),
>>>>>>> 6984e7e05350154c0a13e402d654411a0324fe67
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
    path('employee/add/', EmployeeAPIView.as_view({
        'post': 'create'
    })),

    path('leave/add', LeaveAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('leave', LeaveDataAPIView.as_view({
        'get': 'list',
    })),
    path('leave/<int:pk>', LeaveAPIView.as_view(
        {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'})),
    path('leave-policy/add', LeavePolicyAPIView.as_view({'get': 'list',
                                                         'post': 'create'})),
    path('leave-policy/<int:pk>', LeavePolicyAPIView.as_view({'get': 'retrieve',
                                                             'patch': 'partial_update',
                                                              'delete': 'destroy', 'put': 'update'})),
    path('special-leave/add',
         SpecialLeaveAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('special-leave/<int:pk>', SpecialLeaveAPIView.as_view(
        {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'})),
        path('company-policy/add',
         CompanyLeavePolicyAPIView.as_view({'get': 'list', 'post': 'create'})),
    path('company-policy/<int:pk>', CompanyLeavePolicyAPIView.as_view(
        {'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'})),

]
