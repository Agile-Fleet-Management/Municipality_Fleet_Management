from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.users.models import Role, User
from rest_framework.test import APIClient
from rest_framework import status
import uuid

from django.urls import reverse
class RoleModelTests(TestCase):
    def test_create_role(self):
        role = Role.objects.create(name="Admin", description="Administrator role")
        self.assertEqual(role.__str__(), "Admin")

class UserModelTests(TestCase):
    def setUp(self):
        Role.objects.create(name="Admin", description="Administrator role")

    def test_create_user(self):
        User = get_user_model()
        role = Role.objects.get(name="Admin")
        user = User.objects.create_user(username="john", phone_number="1234567890", address="123 Main St", role_id=role)
        self.assertEqual(user.__str__(), "john")
        self.assertEqual(user.role_id, role)
class UserViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin_role = Role.objects.create(name="Admin", description="Administrator role")
        unique_suffix = uuid.uuid4().hex  # Ensures uniqueness
        self.username = f"john_{unique_suffix}"
        self.user_data = {
            "username": self.username,
            "email": f"{self.username}@example.com",
            "password": "test1234",
            "phone_number": "1234567890",
            "address": "123 Main St",
            "first_name": "John",
            "last_name": "Doe",
            "role_id": self.admin_role.id
        }
        self.admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        self.client.force_authenticate(user=self.admin_user)

    def test_user_registration(self):
        response = self.client.post(reverse('register'), self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED, response.data)
        self.client.logout()  # Reset client state after the test

    def tearDown(self):
        User.objects.filter(username__startswith='john_').delete()  # Clean up any test users
