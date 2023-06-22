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
from structure import port_information
from config.models import Form,Card,Tabs
from config.serializer import FormSerializer,CardsSerializer,TabsSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView

# Create your views here.

class EmployeeView(viewsets.ModelViewSet):
    queryset = EmployeeData.objects.filter(is_delete = False)
    serializer_class = EmployeeDataSerializer

class EmployeeAPIView(viewsets.ModelViewSet):
    queryset = EmployeeData.objects.filter(is_delete = False)
    serializer_class = EmployeeDataRegisterSerializer


class PortView(viewsets.ModelViewSet):
    queryset = PortData.objects.all()
    serializer_class = PortData

class PortInformation(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = (IsAuthenticated,)
    
    def get(self,request,format=None):
        if request.user.is_anonymous:
            return Response({'success': False, 'message': 'Unauthorized ,Please Login','code':401})

        get_structure = self.request.query_params.get('get_structure',None)
        port_id = self.request.query_params.get('port_id',None)
        
        if get_structure is None:
            if (request.user.is_superuser == False and request.user.role != 'superadmin'):
                try:
                    data = PortDataSerializer(PortData.objects.get(id=request.user.port.id)).data
                except PortData.DoesNotExist:
                    pass      
            else:
                data = PortDataSerializer(PortData.objects.all().exclude(is_delete=True).order_by('id'),many=True).data
        if port_id is not None:
            if request.user.is_superuser == False and request.user.role != 'superadmin':
                data = PortDataSerializer(PortData.objects.get(
                id=request.user.port.id)).data
            else:
                data = PortDataSerializer(PortData.objects.get(id=port_id)).data
        if get_structure is not None:
            # data = {'form' : TabsSerializer(Tabs.objects.filter(form__id=1),many=True).data}
            data = port_information.port_structure
        return Response(fetch_msg(data))

    def post(self,request,format=None):
        if request.user.is_anonymous:
            return Response({'success': False, 'message': 'Unauthorized ,Please Login','code':401})
        data = request.data
        PortData.objects.create(data=data)
        return Response(save_msg())

    def put(self,request,format=None):
        if request.user.is_anonymous:
            return Response({'success': False, 'message': 'Unauthorized ,Please Login','code':401})
        data = request.data
        PortData.objects.filter(id=data['port_id']).update(data=data['data'])
        return Response(update_msg())

    def delete(self,request,format=None):
        if request.user.is_anonymous:
            return Response({'success': False, 'message': 'Unauthorized ,Please Login','code':401})
        port_id = self.request.query_params.get('port_id',None)
        archive = self.request.query_params.get('archive',None)
        if port_id is None:
            return Response(failed_msg('Please send the port id'))
        if archive is not None:
            PortData.objects.filter(id=port_id).update(archive=archive) 
            return Response(update_msg())
        PortData.objects.filter(id=port_id).update(is_delete=True)
        return Response(delete_msg())




# class EmployeeView(APIView):
#     authentication_classes = [TokenAuthentication, ]
#     permission_classes = [IsAuthenticated, ]
    
#     def get(self,request,format=None):
#         print(f"re{self.request.user}")
#         data = PersonalInformationSerializer(
#             PersonalInformation.objects.all().order_by('id'), many=True).data
   
#         return Response(fetch_msg(data))

#     def post(self,request,format=None):
#         if request.user.is_anonymous:
#             return Response({'success': False, 'message': 'Unauthorized ,Please Login','code':401})
#         data = request.data
#         EmployeeData.objects.create(data=data)
#         return Response(save_msg())

#     def put(self,request,format=None):
#         if request.user.is_anonymous:
#             return Response({'success': False, 'message': 'Unauthorized ,Please Login','code':401})
#         data = request.data
#         EmployeeData.objects.filter(id=data['employee_id']).update(data=data['data'])
#         return Response(update_msg())

#     def delete(self,request,format=None):
#         if request.user.is_anonymous:
#             return Response({'success': False, 'message': 'Unauthorized ,Please Login','code':401})
#         employee_id = self.request.query_params.get('employee_id',None)
#         archive = self.request.query_params.get('archive',None)
#         if employee_id is None:
#             return Response(failed_msg('Please send the employee id'))
#         if archive is not None:
#             EmployeeData.objects.filter(id=employee_id).update(archive=archive) 
#             return Response(update_msg())
#         EmployeeData.objects.filter(id=employee_id).update(is_delete=True)
#         return Response(delete_msg())


class ImageView(APIView):

    authentication_classes = [TokenAuthentication, ]
    permission_classes = (IsAuthenticated,)

    def get(self,request,format=None):
        if request.user.is_anonymous:
            return Response({'success': False, 'message': 'Unauthorized ,Please Login','code':401})
        image_id = self.request.query_params.get("image_id",None)
        data = ImageSerializer(Image.objects.get(id=image_id)).data
        return Response(fetch_msg(data))

    def post(self,request,format=None):
        if request.user.is_anonymous:
            return Response({'success': False, 'message': 'Unauthorized ,Please Login','code':401})
        image = Image.objects.create(image=request.FILES.get('image'))
        return Response(save_msg(ImageSerializer(image).data))


class DocumentView(APIView):

    authentication_classes = [TokenAuthentication, ]
    permission_classes = (IsAuthenticated,)

    def get(self,request,format=None):
        if request.user.is_anonymous:
            return Response({'success': False, 'message': 'Unauthorized ,Please Login','code':401})
        document_id = self.request.query_params.get("document_id",None)
        data = DocumentSerializer(Document.objects.get(id=document_id)).data
        return Response(fetch_msg(data))

    def post(self,request,format=None):
        if request.user.is_anonymous:
            return Response({'success': False, 'message': 'Unauthorized ,Please Login','code':401})
        document = Document.objects.create(files=request.FILES.get('document'))
        return Response(save_msg(DocumentSerializer(document).data))
    
class LeaveAPIView(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer

class LeaveDataAPIView(viewsets.ModelViewSet):
    queryset = Leave.objects.all()
    serializer_class = LeaveDataSerializer

class LeavePolicyAPIView(viewsets.ModelViewSet):
    queryset = LeavePolicy.objects.all()
    serializer_class = LeavePolicySerializer

class SpecialLeaveAPIView(viewsets.ModelViewSet):
    queryset = SpecialLeave.objects.all()
    serializer_class = SpecialLeaveSerializer

class CompanyLeavePolicyAPIView(viewsets.ModelViewSet):
    queryset = CompanyLeavePolicy.objects.all()
    serializer_class = CompanyLeavePolicySerializer

class DocumentAPIView(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class CompanyManualAPIView(viewsets.ModelViewSet):
    queryset = CompanyManual.objects.all()
    serializer_class = CompanyManualSerializer

class CompanyPolicyAPIView(viewsets.ModelViewSet):
    queryset = CompanyPolicy.objects.all()
    serializer_class = CompanyPolicySerializer

class IMSProcedureAPIView(viewsets.ModelViewSet):
    queryset = IMSProcedure.objects.all()
    serializer_class = IMSProcedureSerializer

class IMSFormAPIView(viewsets.ModelViewSet):
    queryset = IMSForm.objects.all()
    serializer_class = IMSFormSerializer

class DepartmentalProcedureAPIView(viewsets.ModelViewSet):
    queryset = DepartmentalProcedure.objects.all()
    serializer_class = DepartmentalProcedureSerializer
    
class DepartmentalFormAPIView(viewsets.ModelViewSet):
    queryset = DepartmentalForm.objects.all()
    serializer_class = DepartmentalFormSerializer

class CompanyIMSFormAPIView(viewsets.ModelViewSet):
    queryset = CompanyIMSForm.objects.all()
    serializer_class = CompanyIMSFormSerializer

class IMSFormDataAPIView(viewsets.ModelViewSet):
    queryset = IMSFormData.objects.all()
    serializer_class = IMSFormDataSerializer

class DepartmentalFormDataAPIView(viewsets.ModelViewSet):
    queryset = DepartmentalFormData.objects.all()
    serializer_class = DepartmentalFormDataSerializer

class DepartmentalFormDataViewAPIView(viewsets.ModelViewSet):
    queryset = DepartmentalFormData.objects.all()
    serializer_class = DepartmentalFormDataViewSerializer

class LocationAPIView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class ReportTypeAPIView(viewsets.ModelViewSet):
    queryset = ReportType.objects.all()
    serializer_class = ReportTypeSerializer

class SubmitToAPIView(viewsets.ModelViewSet):
    queryset = SubmitTo.objects.all()
    serializer_class = SubmitToSerializer
