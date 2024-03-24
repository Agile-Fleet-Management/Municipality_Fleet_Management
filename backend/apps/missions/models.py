from django.db import models
from apps.users.models import User

class Mission(models.Model):

    driver_id = models.ForeignKey(User,on_delete=models.CASCADE)
    mission_id=models.IntegerField()
    start_time=models.DateField() 
    end_time=models.DateField()
    status=models.CharField(max_length=20) 
    flag=models.CharField(max_length=20)
    
    
    def __str__(self):
        return self.id 
    
class Driver(models.Model):
    mission_id = models.IntegerField()
    vehicle_id = models.CharField(max_length=20)
    driver_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('mission_id', 'vehicle_id')
    


    def __str__(self):
        return self.id 

class MissionRequest(models.Model):

    # request_id=models.IntegerField()
    mission_id=models.ForeignKey(Mission,on_delete=models.CASCADE)
    requester_id=models.ForeignKey(User,on_delete=models.CASCADE)
    request_time=models.CharField(max_length=20)
    m_status=models.CharField(max_length=20)
    p_status=models.CharField(max_length=20)

    def __str__(self):
        return self.id