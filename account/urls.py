from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('user/', UserView.as_view()),
    path('login/', LoginView.as_view()),
    path('register',
         RegisterView.as_view({'post': 'create'}), name='auth_register'),
path('user/<pk>', RegisterView.as_view({'get': 'retrieve', 'patch': 'partial_update', 'delete': 'destroy', 'put': 'update' }), name='auth_re'),
]
