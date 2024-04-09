from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Vtype, Vehicle, Mtype, Maintenance
from .serializers import VtypeSerializer, VehicleSerializer, MtypeSerializer, MaintenanceSerializer
from django.http import JsonResponse
from .models import Vehicle
from .serializers import VehicleSerializer

class VtypeViewSet(viewsets.ModelViewSet):
    queryset = Vtype.objects.all()
    serializer_class = VtypeSerializer
    

# class VehicleViewSet(viewsets.ModelViewSet):
#     queryset = Vehicle.objects.all()
#     serializer_class = VehicleSerializer
# class VehicleListView(APIView):
#     def get(self, request, format=None):
#         """
#         Return a list of all vehicles.
#         """
#         vehicles = Vehicle.objects.all()
#         serializer = VehicleSerializer(vehicles, many=True)
#         return Response(serializer.data)

from django.http import JsonResponse
from .models import Vehicle
from .serializers import VehicleSerializer



from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Vehicle
from .serializers import VehicleSerializer
from rest_framework import status



# views.py in your Vehicles app

from rest_framework import viewsets

class VehicleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    A simple ViewSet for viewing vehicles.
    """
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


# class MtypeViewSet(viewsets.ModelViewSet):
#     queryset = Mtype.objects.all()
#     serializer_class = MtypeSerializer

# class MaintenanceViewSet(viewsets.ModelViewSet):
#     queryset = Maintenance.objects.all()
#     serializer_class = MaintenanceSerializer
