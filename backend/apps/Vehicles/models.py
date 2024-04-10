from django.db import models

class Vtype(models.Model):

    name = models.CharField(max_length=20) 
    description = models.CharField(max_length=500) 
    
    def __str__(self):
        return self.name

class Vehicle(models.Model):

    brand = models.CharField(max_length=20) 
    model = models.CharField(max_length=20) 
    age = models.IntegerField()
    status_choices=[
        ("1","maintenance"),
        ("2","available"),
        ("3","booked"),
    ]
    status=models.CharField(choices=status_choices,default="2")
    Vtype = models.ForeignKey(Vtype,on_delete=models.CASCADE)
    kms = models.CharField(max_length=20) 
    notification_time_year = models.IntegerField()
    notification_mileage = models.FloatField()

    def __str__(self):
        return self.brand

class Mtype(models.Model):

    name = models.CharField(max_length=20) 
    description = models.CharField(max_length=500) 
    
    
    def __str__(self):
        return self.name


class Maintenance(models.Model):

    title=models.CharField(max_length=20)
    vehicle_id = models.CharField(max_length=20) 
    start_time = models.CharField(max_length=20) 
    end_time = models.IntegerField()
    m_type = models.ForeignKey(Mtype,on_delete=models.CASCADE)
    decription = models.CharField(max_length=500)
    cost = models.FloatField()
    kms = models.FloatField(max_length=20) 
    
    def __str__(self):
        return self.title
