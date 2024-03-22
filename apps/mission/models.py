from django.db import models
from ..Employee.models import users



class Mission(models.Model):

    driver_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    mission_id=models.IntegerField()
    start_time=models.DateField() 
    end_time=models.DateField()
    status=models.CharField(max_length=20) 
    flag=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.mission_id 
    
class Driver(models.Model):
    driver_id = models.ForeignKey(Employee,on_delete=models.CASCADE)
    mission_id=models.IntegerField()
    vehicle_id=models.CharField(max_length=20)

    def __str__(self):
        return self. driver_id  

class MissionRequest(models.Model):

    request_id=models.IntegerField()
    mission_id=models.ForeignKey(Mission,on_delete=models.CASCADE)
    requester_id=models.ForeignKey(Mission,on_delete=models.CASCADE)
    request_time=models.CharField(max_length=20)
    m_status=models.CharField(max_length=20)
    p_status=models.CharField(max_length=20)

    def __str__(self):
        return self.request_id