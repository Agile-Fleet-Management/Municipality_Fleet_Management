# from django.urls import path
# from django.contrib import admin
# from . import views

# urlpatterns = [
#     path('vehicle/', views.VehicleListView.as_view(), name='vehicle-list'),
# ]



# urls.py in your Vehicles app

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VehicleViewSet, VtypeViewSet, MtypeViewSet, MaintenanceViewSet

router = DefaultRouter()
router.register(r'vehicles', VehicleViewSet, basename='vehicles')
router.register(r'vtypes', VtypeViewSet, basename='vtypes')
router.register(r'mtypes', MtypeViewSet, basename='mtypes')
router.register(r'maintenances', MaintenanceViewSet, basename='maintenances')

urlpatterns = [
    path('', include(router.urls)),
]















# from .views import VtypeAPIView, VehicleAPIView, MtypeAPIView, MaintenanceAPIView

# urlpatterns = [
#     path('vtypes/', VtypeAPIView.as_view()),
#     path('vehicles/', VehicleAPIView.as_view()),
#     path('mtypes/', MtypeAPIView.as_view()),
#     path('maintenances/', MaintenanceAPIView.as_view()),
# ]

# from rest_framework.routers import DefaultRouter
# from django.urls import include, path
# from .views import VtypeViewSet, VehicleViewSet, MtypeViewSet, MaintenanceViewSet

# router = DefaultRouter()
# router.register(r'vtypes', VtypeViewSet)
# router.register(r'vehicles', VehicleViewSet)
# router.register(r'mtypes', MtypeViewSet)
# router.register(r'maintenances', MaintenanceViewSet)



# from .views import VehicleListView

# urlpatterns = [
#     path('vehicles/', VehicleListView.as_view(), name='vehicle-list'),
# ]

