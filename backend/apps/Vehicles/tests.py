from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Vtype, Vehicle, Mtype, Maintenance

class VtypeTests(APITestCase):
    def setUp(self):
        self.vtype_data = {'name': 'Sedan', 'description': 'Standard Sedan type'}

    def test_create_vtype(self):
        response = self.client.post(reverse('vtype-list'), self.vtype_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], 'Sedan')

    def test_get_vtype(self):
        vtype = Vtype.objects.create(**self.vtype_data)
        response = self.client.get(reverse('vtype-detail', args=[vtype.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Standard Sedan type')

    def test_update_vtype(self):
        vtype = Vtype.objects.create(**self.vtype_data)
        new_data = {'name': 'Compact', 'description': 'Compact car type'}
        response = self.client.put(reverse('vtype-detail', args=[vtype.id]), new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        vtype.refresh_from_db()
        self.assertEqual(vtype.name, 'Compact')

    def test_delete_vtype(self):
        vtype = Vtype.objects.create(**self.vtype_data)
        response = self.client.delete(reverse('vtype-detail', args=[vtype.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Vtype.objects.filter(id=vtype.id).exists())

class VehicleTests(APITestCase):
    def setUp(self):
        self.vtype = Vtype.objects.create(name='SUV', description='Sport Utility Vehicle')
        self.vehicle_data = {
            'brand': 'Toyota',
            'model': 'RAV4',
            'age': 5,
            'status': 'available',
            'Vtype': self.vtype.id,
            'kms': 50000,
            'notification_time_year': 3,
            'notification_mileage': 50000.0,
        }

    def test_create_vehicle(self):
        response = self.client.post(reverse('vehicle-list'), self.vehicle_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['model'], 'RAV4')

    def test_get_vehicle(self):
        vehicle = Vehicle.objects.create(**self.vehicle_data)
        response = self.client.get(reverse('vehicle-detail', args=[vehicle.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['brand'], 'Toyota')

    def test_update_vehicle(self):
        vehicle = Vehicle.objects.create(**self.vehicle_data)
        new_data = {'model': 'Corolla', 'age': 4}
        response = self.client.put(reverse('vehicle-detail', args=[vehicle.id]), new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        vehicle.refresh_from_db()
        self.assertEqual(vehicle.model, 'Corolla')

    def test_delete_vehicle(self):
        vehicle = Vehicle.objects.create(**self.vehicle_data)
        response = self.client.delete(reverse('vehicle-detail', args=[vehicle.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Vehicle.objects.filter(id=vehicle.id).exists())

class MaintenanceTests(APITestCase):
    def setUp(self):
        vtype = Vtype.objects.create(name='Coupe', description='Two-door car type')
        vehicle = Vehicle.objects.create(brand='Ford', model='Mustang', age=3, status='available', Vtype=vtype, kms=20000)
        mtype = Mtype.objects.create(name='Oil Change', description='Engine oil replacement')
        self.maintenance_data = {
            'title': 'Annual Checkup',
            'vehicle_id': vehicle.id,
            'start_time': '2024-01-10T12:00:00Z',
            'end_time': '2024-01-10T15:00:00Z',
            'm_type': mtype.id,
            'description': 'Yearly maintenance checkup',
            'cost': 299.99,
            'kms': 25000
        }

    def test_create_maintenance(self):
        response = self.client.post(reverse('maintenance-list'), self.maintenance_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Annual Checkup')

    def test_get_maintenance(self):
        maintenance = Maintenance.objects.create(**self.maintenance_data)
        response = self.client.get(reverse('maintenance-detail', args=[maintenance.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], 'Yearly maintenance checkup')

    def test_update_maintenance(self):
        maintenance = Maintenance.objects.create(**self.maintenance_data)
        new_data = {'title': 'Biannual Checkup', 'cost': 199.99}
        response = self.client.put(reverse('maintenance-detail', args=[maintenance.id]), new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        maintenance.refresh_from_db()
        self.assertEqual(maintenance.title, 'Biannual Checkup')

    def test_delete_maintenance(self):
        maintenance = Maintenance.objects.create(**self.maintenance_data)
        response = self.client.delete(reverse('maintenance-detail', args=[maintenance.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Maintenance.objects.filter(id=maintenance.id).exists())
