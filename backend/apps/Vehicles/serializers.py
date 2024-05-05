from rest_framework import serializers
from .models import Vehicle,Vtype, Maintenance,Mtype


from rest_framework import serializers
from .models import Vehicle, Vtype

class VehicleSerializer(serializers.ModelSerializer):
    status_display = serializers.SerializerMethodField()
    Vtype_display = serializers.CharField(source='Vtype.name', read_only=True)
    Vtype_name = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = Vehicle
        fields = [
            'id', 'brand', 'model', 'age', 'status', 'status_display',
            'Vtype_display', 'Vtype_name', 'kms', 'notification_time_year',
            'notification_mileage'
        ]

    def get_status_display(self, obj):
        return obj.get_status_display()

    def create(self, validated_data):
        vtype_name = validated_data.get('Vtype_name')
        if not vtype_name:
            raise serializers.ValidationError({"Vtype_name": "Vtype_name is required."})
        vtype = Vtype.objects.filter(name=vtype_name).first()
        if not vtype:
            raise serializers.ValidationError({"Vtype_name": f"No such Vtype found: '{vtype_name}'"})
        
        vehicle = Vehicle.objects.create(**validated_data, Vtype=vtype)
        return vehicle

    def update(self, instance, validated_data):
        vtype_name = validated_data.get('Vtype_name')
        if vtype_name:
            vtype = Vtype.objects.filter(name=vtype_name).first()
            if not vtype:
                raise serializers.ValidationError({"Vtype_name": f"No such Vtype found: '{vtype_name}'"})
            instance.Vtype = vtype
        
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
    
