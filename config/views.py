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
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, BasicAuthentication
from helper.response_creater import fetch_msg,save_msg,update_msg,delete_msg,failed_msg
from config.serializer import FormSerializer,CardsSerializer

class MenuView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = (IsAuthenticated,)

    def get(self,request,format=None):
        if request.user.is_anonymous:
            return Response({'success': False, 'message': 'Unauthorized ,Please Login','code':401})
        data = FormSerializer(Form.objects.all().exclude(delete=True),many=True).data
        return Response(fetch_msg(data))

    def post(self,request,format=None):
        data = request.data
        Form.objects.create(data=data)
        return Response(save_msg())

    def put(self,request,format=None):
        data = request.data
        if data['menu_id'] is None:
            return Response(failed_msg('Please send the menu id!!'))
        Form.objects.filter(id=data['menu_id']).update(data=data['menu'])
        return Response(update_msg())

    def delete(self,request,format=None):
        menu_id = self.request.query_params.get('menu_id',None)
        if menu_id is None:
            return Response(failed_msg('Please send the menu id'))
        Form.objects.filter(id=menu_id).update(delete=True)
        return Response(delete_msg())


class CardsView(APIView):
    authentication_classes = [TokenAuthentication, ]

    def get(self,request,format=None):
        data = CardsSerializer(Cards.objects.all().exclude(delete=True),many=True).data
        return Response(fetch_msg(data))

    def post(self,request,format=None):
        data = request.data
        Cards.objects.create(sub_menu=Submenu.objects.get(id=data['sub_menu_id']),data=data['card_data'])
        return Response(save_msg())

    def put(self,request,format=None):
        data = request.data
        if data['card_id'] is None:
            return Response(failed_msg('Please send the card id!!'))
        Cards.objects.filter(id=data['card_id']).update(data=data['card_data'])
        return Response(update_msg())

    def delete(self,request,format=None):
        card_id = self.request.query_params.get('card_id',None)
        if card_id is None:
            return Response(failed_msg('Please send the card id'))
        Cards.objects.filter(id=card_id).update(delete=True)
        return Response(delete_msg())


class CardsFieldsView(APIView):
    authentication_classes = [TokenAuthentication, ]

    def get(self,request,format=None):
        card_id = self.request.query_params.get('card_id',None)
        if card_id is not None:
            data = CardsFieldsSerializer(CardsFields.objects.filter(card__id=card_id).exclude(delete=True),many=True).data
        if card_id is None:
            data = CardsFieldsSerializer(CardsFields.objects.all().exclude(delete=True),many=True).data
        return Response(fetch_msg(data))

    def post(self,request,format=None):
        data = request.data
        CardsFields.objects.create(card=Cards.objects.get(id=data['card_id']),data=data['fields_data'])
        return Response(save_msg())

    def put(self,request,format=None):
        data = request.data
        if data['card_fields_id'] is None:
            return Response(failed_msg('Please send the card fields id!!'))
        CardsFields.objects.filter(id=data['card_fields_id']).update(data=data['fields_data'])
        return Response(update_msg())

    def delete(self,request,format=None):
        card_fields_id = self.request.query_params.get('card_fields_id',None)
        if card_fields_id is None:
            return Response(failed_msg('Please send the card field id'))
        CardsFields.objects.filter(id=card_fields_id).update(delete=True)
        return Response(delete_msg())



