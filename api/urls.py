from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('portInformation/',PortInformation.as_view()),
    # path('employee/',EmployeeView.as_view()),
    path('image/',ImageView.as_view()),
    path('document/',DocumentView.as_view()),
]
