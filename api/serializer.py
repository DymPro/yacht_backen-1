from rest_framework import serializers
from .models import *
from account.serializer import UserSerializer

class PortDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = PortData
        fields = "__all__"

class EmployeeDataSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta():
        model = EmployeeData
        fields = "__all__"

class EmployeeDataRegisterSerializer(serializers.ModelSerializer):
    class Meta():
        model = EmployeeData
        fields = "__all__"

class ImageSerializer(serializers.ModelSerializer):
    class Meta():
        model = Image
        fields = "__all__"
        
        
class DocumentSerializer(serializers.ModelSerializer):
    class Meta():
        model = Document
        fields = "__all__"

class PortDataV(serializers.ModelSerializer):
    
    class Meta:
        model = PortData
        fields = ['id', ]