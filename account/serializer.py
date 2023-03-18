from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        # fields = "__all__"
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role','gender','phone','pincode','date_of_birth', 'is_hr', 'is_superuser', 'port']

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    # password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('password', 'email', 'username',
                  'role', 'date_of_birth', 'gender', 'port', 'id','first_name', 'last_name',)

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            role=validated_data['role'],
            date_of_birth=validated_data['date_of_birth'],
            gender = validated_data['gender'],
            port = validated_data['port'],
            first_name = validated_data['first_name'],
            last_name = validated_data['lastname'],
            phone = validated_data['phone'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user