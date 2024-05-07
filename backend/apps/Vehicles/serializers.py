from rest_framework import serializers
from .models import Vehicle,Vtype, Maintenance,Mtype


from rest_framework import serializers
from .models import Vehicle, Vtype

class VehicleSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()
    # tool_display = serializers.SerializerMethodField()
    # Vtype_display = serializers.CharField(source='Vtype.name', read_only=True)

    class Meta:
        model = Vehicle
        fields = '__all__'

    def get_status_display(self, obj):
        return obj.get_status_display()
    

    def create(self, validated_data):
    
        vehicle = Vehicle.objects.create(**validated_data)
        return vehicle

    def update(self, instance, validated_data):
       
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance


    
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
    
