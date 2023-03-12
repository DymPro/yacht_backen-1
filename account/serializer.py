from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        # fields = "__all__"
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role','gender','pincode','date_of_birth', 'is_hr', 'is_superuser']

