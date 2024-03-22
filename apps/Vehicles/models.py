from django.db import models


class Vehicle(models.Model):

    vehicle_id = models.CharField(max_length=20) 
    make = models.CharField(max_length=20) 
    model = models.CharField(max_length=20) 
    age = models.IntegerField()
    status = models.CharField(max_length=20) 
    Vtype = models.CharField(max_length=20) 
    kms = models.CharField(max_length=20) 
    notification_time = models.CharField(max_length=20) 
    notification_mileage = models.CharField(max_length=20) 

def __str__(self):
    return self.vehicle_id

class Vtype(models.Model):

    type_id = models.IntegerField()
    name = models.CharField(max_length=20) 
    description = models.CharField(max_length=20) 
    
    
def __str__(self):
    return self.type_id

class Maintenance(models.Model):

    employee_id = models.IntegerField()
    dname = models.CharField(max_length=20) 
    lname = models.CharField(max_length=20) 
    number = models.IntegerField()
    address = models.CharField(max_length=20) 
    role_id = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    username = models.CharField(max_length=20) 
    password = models.CharField(max_length=20) 
    
def __str__(self):
    return self.employee_id

class MType(models.Model):

    record_id = models.IntegerField()
    vehicle_id = models.CharField(max_length=20) 
    start_time = models.CharField(max_length=20) 
    end_time = models.IntegerField()
    m_type = models.CharField(max_length=20) 
    decription = models.CharField(max_length=20)
    cost = models.IntegerField()
    kms = models.CharField(max_length=20) 
    
def __str__(self):
    return self.record_id
