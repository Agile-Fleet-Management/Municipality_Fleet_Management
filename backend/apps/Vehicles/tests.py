from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Vehicle, Vtype, Mtype, Maintenance
from apps.users.models import User, Role


class VtypeTests(APITestCase):
    def setUp(self):

        self.client = APIClient()
        self.admin_role = Role.objects.create(name="Admin", description="Administrator role")
        self.admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')

        # Authenticate as the admin user before making the request
        self.client.force_authenticate(user=self.admin_user)
        self.vtype = Vtype.objects.create(name="Sedan", description="Comfortable seating for four")

    def test_create_vtype(self):
        url = reverse('vtypes-list')
        data = {'name': 'Convertible', 'description': 'Open roof enjoyment'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vtype.objects.count(), 2)
        self.assertEqual(Vtype.objects.last().name, 'Convertible')

    def test_get_vtype(self):
        url = reverse('vtypes-detail', args=[self.vtype.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.vtype.name)

    def test_update_vtype(self):
        url = reverse('vtypes-detail', args=[self.vtype.id])
        data = {'name': 'Updated Type', 'description': 'Updated description'}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vtype.refresh_from_db()
        self.assertEqual(self.vtype.name, 'Updated Type')

    def test_delete_vtype(self):
        url = reverse('vtypes-detail', args=[self.vtype.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vtype.objects.count(), 0)

class VehicleTests(APITestCase):
    def setUp(self):

        self.client = APIClient()
        self.admin_role = Role.objects.create(name="Admin", description="Administrator role")
        self.admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')

        # Authenticate as the admin user before making the request
        self.client.force_authenticate(user=self.admin_user)

        self.vtype = Vtype.objects.create(name="SUV", description="Spacious and robust")
        self.vehicle = Vehicle.objects.create(
            brand='Ford',
            model='Explorer',
            age=10,
            status='2',
            Vtype=self.vtype,
            kms=100000,
            notification_time_year=5,
            notification_mileage=120000,
        )

    def test_create_vehicle(self):
        url = reverse('vehicles-list')
        data = {
            "brand": "Honda",
            "model": "Civic",
            "age": 3,
            "status": "2",
            "Vtype": self.vtype.id,
            "kms": 25000,
            "notification_time_year": 2,
            "notification_mileage": 50000,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vehicle.objects.count(), 2)
        self.assertEqual(Vehicle.objects.last().brand, "Honda")

    def test_update_vehicle(self):
        url = reverse('vehicles-detail', args=[self.vehicle.id])
        data = {
            "brand": "Toyota",
            "model": "Corolla",
            "age": 4,
            "status": "3",  # Vehicle is now booked
            "Vtype": self.vtype.id,
            "kms": 55000,
            "notification_time_year": 4,
            "notification_mileage": 75000,
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vehicle.refresh_from_db()
        self.assertEqual(self.vehicle.model, "Corolla")

    def test_delete_vehicle(self):
        url = reverse('vehicles-detail', args=[self.vehicle.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vehicle.objects.count(), 0)
