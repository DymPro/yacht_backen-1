from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class PortData(models.Model):
    data = models.JSONField(null=True,blank=True)
    delete = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)

class EmployeeData(models.Model):
    data = models.JSONField(null=True,blank=True)
    delete = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)

class Image(models.Model):
    image = models.ImageField(upload_to='image/', blank=True, null=True)

class Document(models.Model):
    files = models.FileField(upload_to='files/')