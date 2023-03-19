from django.db import models
from django.contrib.auth.models import AbstractUser
from api.models import PortData
# Create your models here.


USER_ROLES = (
    ('superadmin', 'Super Admin'),
    ('staff', 'Staff'),
    ('hr', 'HR'),
)
GENDER = (
    ('male', 'Male'),
    ('female', 'Female'),
    ('other', 'Other'),
)

class User(AbstractUser):
    role = models.CharField(max_length=25, choices=USER_ROLES,
                            default='staff', null=True, blank=True)
    device_token = models.CharField(max_length=225, null=True, blank=True)
    port = models.ForeignKey(PortData, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField( choices=GENDER,max_length=225, null=True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=225, null=True, blank=True)
    position = models.CharField(max_length=225, null=True, blank=True)
    nationality = models.CharField(max_length=225, null=True, blank=True)
    address = models.CharField(max_length=225, null=True, blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    is_hr = models.BooleanField(default=False)


    def __str__(self):
        return f'{self.first_name} {self.username}'