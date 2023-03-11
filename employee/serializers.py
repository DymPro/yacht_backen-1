from rest_framework import serializers
from .models import *
from api.models import PortData

class PersonalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInformation
        fields = "__all__"


class PortDataV(serializers.ModelSerializer):
    
    class Meta:
        model = PortData
        fields = ['id', ]