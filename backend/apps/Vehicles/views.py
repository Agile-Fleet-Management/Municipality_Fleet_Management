from rest_framework import viewsets
from .models import Vtype, Vehicle, Mtype, Maintenance
from .serializers import VtypeSerializer, VehicleSerializer, MtypeSerializer, MaintenanceSerializer

class VtypeViewSet(viewsets.ModelViewSet):
    queryset = Vtype.objects.all()
    serializer_class = VtypeSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class MtypeViewSet(viewsets.ModelViewSet):
    queryset = Mtype.objects.all()
    serializer_class = MtypeSerializer

class MaintenanceViewSet(viewsets.ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer
