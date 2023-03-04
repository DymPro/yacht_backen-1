from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('user/', UserView.as_view()),
    path('login/', LoginView.as_view()),
]
