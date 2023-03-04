from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    path('menu/', MenuView.as_view()),
    path('cards/', CardsView.as_view()),
    path('cards_fields/', CardsFieldsView.as_view()),
]
