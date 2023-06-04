from django.contrib import admin
from .models import *

admin.site.register([PortData,EmployeeData,Image,Document, Leave, 
                     LeavePolicy, SpecialLeave, CompanyLeavePolicy, 
                     CompanyIMSForm, CompanyManual, CompanyPolicy,
                     IMSProcedure, IMSForm, DepartmentalProcedure, DepartmentalForm,
                        IMSFormData, DepartmentalFormData, Location, ReportType, SubmitTo,
                     ])
