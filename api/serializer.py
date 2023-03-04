from rest_framework import serializers
from .models import *

class PortDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = PortData
        fields = "__all__"

class EmployeeDataSerializer(serializers.ModelSerializer):
    class Meta():
        model = EmployeeData
        fields = "__all__"

class ImageSetializer(serializers.ModelSerializer):
    class Meta():
        model = Image
        fields = "__all__"
        
        
class DocumentSetializer(serializers.ModelSerializer):
    class Meta():
        model = Document
        fields = "__all__"