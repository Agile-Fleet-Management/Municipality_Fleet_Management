from django.db import models
from apps.users.models import User
from apps.Vehicles.models import Vehicle
from datetime import datetime    

class Mission(models.Model):
    title=models.CharField(max_length=20,default="asmae")
    start_time=models.DateTimeField() 
    end_time=models.DateTimeField()
    status_choices=[
        (1,"On Going"),
        (2,"Arrived"),
        (3,"OverDue"),
        (4, "Pending"),
        (5,"Approved"),
        (6,"Rejected")
    ]
    status=models.CharField(choices=status_choices,default=4)
    expected_arrival=models.DateTimeField(max_length=20)
    requester_id=models.ForeignKey(User,on_delete=models.CASCADE)
    request_time=models.DateTimeField(default=datetime.now)
    description=models.CharField(max_length=500)

    def __str__(self):
        return  self.status
    
class Driver(models.Model):
    
    mission_id = models.ForeignKey(Mission,on_delete=models.CASCADE)
    vehicle_id = models.ForeignKey(Vehicle,on_delete=models.CASCADE)
    driver_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('mission_id', 'vehicle_id')
    
    def __str__(self):
        return self.driver_id

class MissionParticipant(models.Model):

    mission_id = models.ForeignKey(Mission,on_delete=models.CASCADE)
    participant_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('mission_id', 'participant_id')
    
    def __str__(self):
        return self.participant_id