from django.db import models

# Create your models here.

from django.contrib.postgres.fields import ArrayField

class Form(models.Model):
    title = models.CharField(null=True,blank=True,max_length=250)
    delete = models.BooleanField(default=False)
    sort_order = models.IntegerField(null=True,blank=True)

    def __str__(self):
        return self.title

    class Meta():
        ordering = ['sort_order']
        
class Tabs(models.Model):
    form = models.ForeignKey(
        Form, on_delete=models.SET_NULL, null=True, blank=True,related_name="tabs")
    title = models.CharField(null=True,blank=True,max_length=250)
    sort_order = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.form.title +"-->"+ self.title

    class Meta():
        ordering = ['sort_order']

class Card(models.Model):
    tabs = models.ForeignKey(
        Tabs, on_delete=models.SET_NULL, null=True, blank=True,related_name="card")
    title = models.CharField(null=True,blank=True,max_length=250)
    sort_order = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.title

    class Meta():
        ordering = ['sort_order']

FieldsType = (
    ('text', 'Text'),
    ('file', 'File'),
    ('switch', 'Switch'),
    ('checkbox', 'Checkbox'),
    ('textarea', 'TextArea'),
    ('dropdown', 'Dropdown'),
    ('number', 'Number'),
    ('date', 'Date'),
)

class CardFields(models.Model):
    card = models.ForeignKey(
        Card, on_delete=models.SET_NULL, null=True, blank=True,related_name="fields")
    label = models.CharField(null=True,blank=True,max_length=250)
    type = models.CharField(null=True,blank=True,max_length=250,choices=FieldsType,default="text")
    mandatory = models.BooleanField(default=False)
    placeholder = models.CharField(null=True,blank=True,max_length=250)
    name = models.CharField(null=True,blank=True,max_length=250)
    value = models.CharField(null=True,blank=True,max_length=250)
    options = models.JSONField(null=True,blank=True)
    extra_data = models.JSONField(null=True,blank=True)
    sort_order = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.label

    class Meta():
        ordering = ['sort_order']



class ExtraFields(models.Model):
    fields = models.ForeignKey(
        CardFields, on_delete=models.SET_NULL, null=True, blank=True,related_name="extra_fields")
    label = models.CharField(null=True,blank=True,max_length=250)
    type = models.CharField(null=True,blank=True,max_length=250,choices=FieldsType,default="text")
    mandatory = models.BooleanField(default=False)
    placeholder = models.CharField(null=True,blank=True,max_length=250)
    name = models.CharField(null=True,blank=True,max_length=250)
    value = models.CharField(null=True,blank=True,max_length=250)
    options = models.JSONField(null=True,blank=True)
    extra_data = models.JSONField(null=True,blank=True)
    sort_order = models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.label

    class Meta():
        ordering = ['sort_order']