from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('user/', UserView.as_view()),
    path('login/', LoginView.as_view()),
    path('register',
         RegisterView.as_view({'post': 'create'}), name='auth_register'),
path('user/<pk>', RegisterView.as_view(
    {'get': 'retrieve', 
    'patch': 'partial_update', 
    'delete': 'destroy', 
    'put': 'update' }), name='auth_re'),
 path('department',DepartmentView.as_view({'post': 'create', 'get':'list'})),
path('department/<pk>', DepartmentView.as_view({'get': 'retrieve', 
    'patch': 'partial_update', 
    'delete': 'destroy', 
    'put': 'update' })),
 path('position',PositionView.as_view({'post': 'create', 'get':'list'})),
path('position/<pk>', PositionView.as_view({'get': 'retrieve', 
    'patch': 'partial_update', 
    'delete': 'destroy', 
    'put': 'update' })),
path('change_password/<int:pk>', ChangePasswordView.as_view(), name='auth_change_password')
]
