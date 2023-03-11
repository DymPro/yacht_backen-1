from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from api.models import PortData
from .serializers import *
from .models import *
# Create your views here.

class PersonalInfoAPI(viewsets.ModelViewSet):
    queryset = PersonalInformation.objects.all()
    serializer_class = PersonalInformationSerializer


class PortView(viewsets.ModelViewSet):
    queryset = PortData.objects.all()
    serializer_class = PortDataV