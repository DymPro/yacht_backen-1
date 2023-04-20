from django.db import models
from django.contrib.auth.models import AbstractUser
from api.models import PortData
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import EmployeeData
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



class Department(models.Model):
    title = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'

class Position(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'{self.title}'
class User(AbstractUser):
    role = models.CharField(max_length=25, choices=USER_ROLES,
                            default='staff', null=True, blank=True)
    device_token = models.CharField(max_length=225, null=True, blank=True)
    port = models.ForeignKey(PortData, on_delete=models.CASCADE, null=True, blank=True)
    gender = models.CharField( choices=GENDER,max_length=225, null=True, blank=True)
    raw_password = models.CharField(max_length=256, null =True, blank=True)
    pincode = models.IntegerField(null=True, blank=True)
    phone = models.CharField(max_length=225, null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    position = models.ForeignKey(Position, on_delete=models.CASCADE, null=True, blank=True)
    nationality = models.CharField(max_length=225, null=True, blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    level_of_authourity = models.CharField(max_length=256, null=True, blank=True)
    is_hr = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.first_name} {self.username}'

#@receiver(post_save, sender=User)
#def create_employee(sender, instance, created, **kwargs):
#    if created:
#        EmployeeData.objects.create(user=instance)


#@receiver(post_save, sender=User)
#def save_employee(sender, instance, **kwargs):
#   instance.employeedata.save()
