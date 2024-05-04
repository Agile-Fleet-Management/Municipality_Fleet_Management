from rest_framework import serializers
from .models import Vehicle,Vtype, Maintenance,Mtype

class VehicleSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()  # For the display value of status
    Vtype_display = serializers.CharField(source='Vtype.name')  # Use source to specify the attribute

    class Meta:
        model = Vehicle
        fields = [
            'id','brand', 'model', 'age', 'status', 'status_display', 
            'Vtype_display', 'kms', 'notification_time_year', 
            'notification_mileage', 'picture'
        ]

    def get_status_display(self, obj):
        return obj.get_status_display()
    
class VtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vtype
        fields = ['id', 'name', 'description']

class MtypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mtype
        fields = ['id', 'name', 'description']

class MaintenanceSerializer(serializers.ModelSerializer):
    m_type_display = serializers.SerializerMethodField()

    class Meta:
        model = Maintenance
        fields = [
            'id', 'title', 'vehicle_id', 'start_time', 'end_time', 'm_type', 
            'm_type_display', 'description', 'cost', 'kms'
        ]

    def get_m_type_display(self, obj):
        return str(obj.m_type) 