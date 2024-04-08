from rest_framework import serializers
from .models import Vtype, Vehicle, Mtype, Maintenance

class VtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vtype
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = '__all__'

class MtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mtype
        fields = '__all__'

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'
