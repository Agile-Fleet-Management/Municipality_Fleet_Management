from django.db import models


class Role(models.Model):

    # role_id = models.IntegerField()
    name = models.CharField(max_length=20) 
    description = models.CharField(max_length=20) 

def __str__(self):
    return self.id

class User(models.Model):

    dname = models.CharField(max_length=20) 
    lname = models.CharField(max_length=20) 
    number = models.IntegerField()
    address = models.CharField(max_length=20) 
    role_id = models.CharField(max_length=20)
    picture = models.ImageField(upload_to='images/', null=True, blank=True)
    username = models.CharField(max_length=20) 
    password = models.CharField(max_length=20) 
    
def __str__(self):
    return self.id