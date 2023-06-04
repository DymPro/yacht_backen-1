from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('portInformation/', PortInformation.as_view()),
    # path('employee/',EmployeeView.as_view()),
    path('image/', ImageView.as_view()),
    path('document/', DocumentAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),

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

    path('company-manual/add', CompanyManualAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('company-manual/<int:pk>', CompanyManualAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
    path('company-policy-form/add', CompanyPolicyAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('company-policy-form/<int:pk>', CompanyPolicyAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
    path('company-procedure/add', IMSProcedureAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('company-procedure/<int:pk>', IMSProcedureAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
    path('ims-form/add', IMSFormAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('ims-form/<int:pk>', IMSFormAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
    path('departmental-procedure/add', DepartmentalProcedureAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('departmental-procedure/<int:pk>', DepartmentalProcedureAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
         })),
    path('departmental-form/add', DepartmentalFormAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('departmental-form/<int:pk>', DepartmentalFormAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
         })),
    path('manage-ims/add', CompanyIMSFormAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('manage-ims/<int:pk>', CompanyIMSFormAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
    path('ims-formdata/', IMSFormDataAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('ims-formdata/<int:pk>', IMSFormDataAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
     path('departmental-formdata/', DepartmentalFormDataAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('departmental-formdata/<int:pk>', DepartmentalFormDataAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
    path('location', LocationAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('location/<int:pk>', LocationAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
        path('report-type', ReportTypeAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('report-type/<int:pk>', ReportTypeAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
        path('submit-to', SubmitToAPIView.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('submit-to/<int:pk>', SubmitToAPIView.as_view({
        'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update'
    })),
]
