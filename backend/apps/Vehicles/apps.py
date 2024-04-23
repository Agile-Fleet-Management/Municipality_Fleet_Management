# from django.apps import AppConfig


# class VehiclesConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'apps.Vehicles'

from django.apps import AppConfig

class VehiclesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.Vehicles'  # This should match the label used in the manage.py test command
