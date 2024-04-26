from django.shortcuts import render
from rest_framework import viewsets
from .models import Mission, Driver, MissionParticipant
from .serializers import MissionSerializer, DriverSerializer, MissionParticipantSerializer

class MissionViewSet(viewsets.ModelViewSet):
    queryset = Mission.objects.all()
    serializer_class = MissionSerializer

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class MissionParticipantViewSet(viewsets.ModelViewSet):
    queryset = MissionParticipant.objects.all()
    serializer_class = MissionParticipantSerializer