# from django.urls import path
# from .views import VtypeAPIView, VehicleAPIView, MtypeAPIView, MaintenanceAPIView

# urlpatterns = [
#     path('vtypes/', VtypeAPIView.as_view()),
#     path('vehicles/', VehicleAPIView.as_view()),
#     path('mtypes/', MtypeAPIView.as_view()),
#     path('maintenances/', MaintenanceAPIView.as_view()),
# ]

from rest_framework.routers import DefaultRouter
from django.urls import include, path
from .views import VtypeViewSet, VehicleViewSet, MtypeViewSet, MaintenanceViewSet

router = DefaultRouter()
router.register(r'vtypes', VtypeViewSet)
router.register(r'vehicles', VehicleViewSet)
router.register(r'mtypes', MtypeViewSet)
router.register(r'maintenances', MaintenanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
