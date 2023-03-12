from django.db import models
from api.models  import PortData
from django.conf import settings
# Create your models here.
User = settings.AUTH_USER_MODEL

class PersonalInformation(models.Model):
    user = models.OneToOneField(User,
                             on_delete=models.CASCADE, null=True, blank=True,)
    port = models.ForeignKey(PortData, on_delete=models.CASCADE, null=True, blank=True, default=1)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    email = models.CharField(max_length=256)
    full_name = models.CharField(max_length=256)
    nationality = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    state = models.CharField(max_length=256)
    country = models.CharField(max_length=256)
    zip_code = models.CharField(max_length=256)
    marital_status = models.CharField(max_length=256)
    date_of_birth = models.DateField(null=True, blank=True)
    spouse = models.CharField(max_length=256)
    home_contact = models.CharField(max_length=256)
    ncp_contact = models.CharField(max_length=256)
    nib_number = models.CharField(max_length=256)
    date_of_hire = models.DateField(null=True, blank=True)
    job_title = models.CharField(max_length=256, null=True, blank=True)
    department = models.CharField(max_length=256, null=True, blank=True)
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
    qualification = models.CharField(max_length=256)
    experience = models.CharField(max_length=256)
    safety_certificate = models.FileField(
        upload_to='files/', blank=True, null=True)
    qualification_certificate = models.FileField(
        upload_to='files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False,auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True,auto_now_add=False)