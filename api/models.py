from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.

class PortData(models.Model):
    data = models.JSONField(null=True,blank=True)
    is_delete = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)

class EmployeeData(models.Model):
    user = models.OneToOneField(User,
                             on_delete=models.CASCADE, null=True, blank=True,)
    data = models.JSONField(null=True,blank=True)
    is_delete = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)
    port = models.ForeignKey(PortData, on_delete=models.CASCADE, null=True, blank=True)
    nib_card = models.FileField(upload_to='files/', blank=True, null=True)
    passport = models.FileField(upload_to='files/', blank=True, null=True)
    medical_certificate = models.FileField(
        upload_to='files/', blank=True, null=True)
    driver_license = models.FileField(
        upload_to='files/', blank=True, null=True)
    police_character = models.FileField(
        upload_to='files/', blank=True, null=True)
    vaccination_card = models.FileField(
        upload_to='files/', blank=True, null=True)
    other = models.FileField(upload_to='files/', blank=True, null=True)
    safety_certificate = models.FileField(
        upload_to='files/', blank=True, null=True)
    qualification_certificate = models.FileField(
        upload_to='files/', blank=True, null=True)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)

class Image(models.Model):
    image = models.ImageField(upload_to='image/', blank=True, null=True)

class Document(models.Model):
    files = models.FileField(upload_to='files/')