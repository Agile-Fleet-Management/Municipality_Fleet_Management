from rest_framework import serializers
from .models import Mission,Driver, MissionParticipant

class MissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mission
        fields = '__all__'
    def validate(self, data):
        if data['start_time'] > data['end_time']:
            raise serializers.ValidationError("End date must be after start date")
        if data['start_time'] > data['expected_arrival']:
            raise serializers.ValidationError("Expected arrival date must be after start date")
        return data

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = '__all__'

class MissionParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = MissionParticipant
        fields = '__all__'