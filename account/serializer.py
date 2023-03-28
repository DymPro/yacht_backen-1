from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"

class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    department =  DepartmentSerializer(read_only=True)
    position =   PositionSerializer(read_only=True)
    class Meta():
        model = User
        # fields = "__all__"
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'role','gender','phone','pincode','position', 'department', 'address', 'nationality','date_of_birth', 'is_hr', 'is_superuser', 'port']



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
                  'role', 'date_of_birth', 'gender', 'port', 'id','first_name', 'last_name', 'phone',
                  'position', 'address', 'nationality', 'department')

    def create(self, validated_data):
        user = User.objects.create(
            email=validated_data['email'],
            username=validated_data['username'],
            role=validated_data['role'],
            date_of_birth=validated_data['date_of_birth'],
            gender = validated_data['gender'],
            port = validated_data['port'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            phone = validated_data['phone'],
            department = validated_data['department'],
            position = validated_data['position'],
            nationality = validated_data['nationality'],
            address = validated_data['address'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('password',)


    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance