from django.db import models
from django.contrib.auth.models import AbstractUser

class Role(models.Model):

    name = models.CharField(max_length=20) 
    description = models.CharField(max_length=20) 

    def __str__(self):
        return self.name

class User(AbstractUser):
    ADMIN = 'admin'
    MANAGER = 'manager'
    FLEET_MANAGER = 'fleet_manager'

    phone_number = models.CharField(max_length=20) 
    address = models.CharField(max_length=20) 
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (MANAGER, 'Manager'),
        (FLEET_MANAGER, 'Fleet Manager'),
    ]

    role = models.CharField(
        max_length=50,
        choices=ROLE_CHOICES,
        default=MANAGER,  # Default role can be set as needed
    )
    picture = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.username