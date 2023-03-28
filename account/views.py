from datetime import datetime,timedelta
from django.utils import timezone
from django.shortcuts import render
from .serializer import *
from .models import *
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login
import random
from rest_framework import status
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
import time
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError
from rest_framework import viewsets

class UserView(APIView):
    authentication_classes = [TokenAuthentication, ]
    def get(self,request,format=None):
        userData = UserSerializer(request.user).data
        return Response({'success':True,'message':'User Account have been fetched','user': userData })

    @csrf_exempt
    def post(self,request,format=None):
        try:
            data = request.data
            user = Users()
            user.username = data['username']
            user.first_name = data['first_name']
            user.password = data['password']
            user.email = data['email']
            user.set_password(data['password'])
            user.save()
            userData = UserSerializer(user).data
            token, created = Token.objects.get_or_create(user=user)
            return Response({'success':True,'message':'User Account have been created','token': token.key,'user': userData })
        except IntegrityError:
            return Response({'success': False, 'message': 'Mobile  already exists,please try to change username'})
        except:
            return Response({'success':False,'message':'Check the user details'})


class LoginView(APIView):
    authentication_classes = [BasicAuthentication, ]

    def post(self, request, format='json'):
        data = request.data
        email = data["email"]
        password = data["password"]
        user = authenticate(request, username=email, password=password)
        if user is None:
            try:
                user = Users.objects.get(email=email)
            except:
                user = None
            if user is not None:
                user = authenticate(
                    request, username=user.username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            userData = UserSerializer(user).data
            return Response({'success': True, 'message':  'lOGGED IN SUCESSFULLY', 'token': token.key, 'user': userData})
        else:
            return Response({'success': False, 'message': 'Username/password entered is wrong'})

class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class PositionView(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer

