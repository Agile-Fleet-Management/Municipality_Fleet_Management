from rest_framework import viewsets
from .models import Vehicle,Vtype,Mtype, Maintenance
from .serializers import VehicleSerializer,VtypeSerializer,MtypeSerializer, MaintenanceSerializer
from rest_framework.viewsets import ModelViewSet

class VehicleViewSet(viewsets.ModelViewSet):
    """
    A ViewSet for viewing and editing vehicles.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class VtypeViewSet(viewsets.ModelViewSet):
    queryset = Vtype.objects.all()
    serializer_class = VtypeSerializer


class MtypeViewSet(ModelViewSet):
    queryset = Mtype.objects.all()
    serializer_class = MtypeSerializer

class MaintenanceViewSet(ModelViewSet):
    queryset = Maintenance.objects.all()
    serializer_class = MaintenanceSerializer

