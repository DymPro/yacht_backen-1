from django.contrib import admin
# Register your models here.
from employee.models import PersonalInformation
from .models import *

admin.site.register([PortData,PersonalInformation,Image,Document])