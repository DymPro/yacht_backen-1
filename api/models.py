from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
User = settings.AUTH_USER_MODEL
# Create your models here.


class PortData(models.Model):
    data = models.JSONField(null=True, blank=True)
    is_delete = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)


class EmployeeData(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)
    data = models.JSONField(null=True, blank=True)
    is_delete = models.BooleanField(default=False)
    archive = models.BooleanField(default=False)
    port = models.ForeignKey(
        PortData, on_delete=models.CASCADE, null=True, blank=True)

    image = models.ImageField(upload_to='image/', blank=True, null=True)
    leave_taken = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return str(self.user)


class Image(models.Model):
    image = models.ImageField(upload_to='image/', blank=True, null=True)


class Document(models.Model):
    files = models.FileField(upload_to='files/')


class LeavePolicy(models.Model):
    designation = models.CharField(max_length=265, null=True, blank=True)
    sick_leave_per_month = models.IntegerField(null=True, blank=True)
    casual_leave_per_month = models.IntegerField(null=True, blank=True)
    port = models.ForeignKey(
        PortData, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.designation


class CompanyLeavePolicy(models.Model):
    company_leave_policy = models.FileField(
        upload_to='files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    port = models.ForeignKey(PortData, on_delete=models.CASCADE,null=True, blank=True )

class SpecialLeave(models.Model):
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_leave_per_month = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.employee.username


class Leave(models.Model):
    employee = models.ForeignKey(
        User, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=265, null=True, blank=True)
    from_date = models.DateField(null=True, blank=True)
    to_date = models.DateField(null=True, blank=True)
    reason = models.TextField(null=True, blank=True)
    duration = models.IntegerField(default=0)
    approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='approved_by')
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    port = models.ForeignKey(
        PortData, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.employee.username

class CompanyIMSForm(models.Model):
    title = models.CharField(max_length=265, null=True, blank=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    port = models.ForeignKey(PortData, on_delete=models.CASCADE,null=True, blank=True )

class CompanyManual(models.Model):
    company_manual = models.FileField(
        upload_to='files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    port = models.ForeignKey(PortData, on_delete=models.CASCADE,null=True, blank=True )

class CompanyPolicy(models.Model):
    data = models.JSONField(null=True, blank=True)
    name = models.CharField(max_length=256, null=True, blank=True)
    company_policy = models.FileField(
        upload_to='files/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    port = models.ForeignKey(PortData, on_delete=models.CASCADE,null=True, blank=True )

class CompanyProcedure(models.Model):
    procedure_name = models.CharField(max_length=265, null=True, blank=True)
    procedure = models.FileField(upload_to='files/', blank=True, null=True)
    user = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    port = models.ForeignKey(PortData, on_delete=models.CASCADE,null=True, blank=True )

class IMSForm(models.Model):
    company_ims = models.ForeignKey(CompanyIMSForm, on_delete=models.CASCADE)
    ims_form = models.FileField(upload_to='files/', blank=True, null=True)
    user = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    port = models.ForeignKey(PortData, on_delete=models.CASCADE,null=True, blank=True )
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)

class DepartmentalProcedure(models.Model):
    procedure_name = models.CharField(max_length=265, null=True, blank=True)
    procedure = models.FileField(upload_to='files/', blank=True, null=True)

    user = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    port = models.ForeignKey(PortData, on_delete=models.CASCADE,null=True, blank=True )

