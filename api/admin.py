from django.contrib import admin
# Register your models here.
from .models import *

admin.site.register([PortData,EmployeeData,Image,Document, Leave, 
                     LeavePolicy, SpecialLeave, CompanyLeavePolicy, 
                     CompanyIMSForm, CompanyManual, CompanyPolicy,
                     IMSProcedure, IMSForm, DepartmentalProcedure, DepartmentalForm,
                        IMSFormData, DepartmentalForm, Location, ReportType, SubmitTo,
                     ])
