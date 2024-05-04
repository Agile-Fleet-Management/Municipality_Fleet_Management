from django.db import models
import os


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
    status=models.CharField(choices=status_choices,default="2",max_length=20)
    Vtype = models.ForeignKey(Vtype,on_delete=models.CASCADE)
    kms = models.FloatField() 
    notification_time_year = models.IntegerField()
    notification_mileage = models.FloatField()

    picture = models.ImageField(upload_to='vehicle_pictures/', null=True)

    def save(self, *args, **kwargs):
        # Check if the picture filename is too long
        if self.picture and len(self.picture.name) > 100:
            # Truncate the filename but keep the extension
            filename_base, filename_ext = os.path.splitext(self.picture.name)
            self.picture.name = filename_base[:95] + filename_ext

        super(Vehicle, self).save(*args, **kwargs)

    def __str__(self):
        return self.brand

class Mtype(models.Model):

    name = models.CharField(max_length=20) 
    description = models.CharField(max_length=500) 
    
    
    def __str__(self):
        return self.name


class Maintenance(models.Model):
    title = models.CharField(max_length=20)
    vehicle = models.ForeignKey(Vehicle, null=True, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    m_type = models.ForeignKey(Mtype, on_delete=models.CASCADE)
    description = models.CharField(max_length=500)
    cost = models.FloatField()
    kms = models.FloatField()

    def __str__(self):
        return self.title


