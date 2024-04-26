from django.test import TestCase
from django.contrib.auth import get_user_model
from apps.users.models import Role, User
from rest_framework.test import APIClient
from rest_framework import status
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
        self.user_data = {
            "username": "john",
            "email": "john@example.com",
            "password": "test1234",
            "phone_number": "1234567890",
            "address": "123 Main St",
            "role_id": self.admin_role
        }
        # Create an admin user for authentication in tests
        self.admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')
        # No need to create another user here if you're just testing registration

    def test_user_registration(self):
        # Authenticate as the admin user before making the request
        self.client.force_authenticate(user=self.admin_user)
        response = self.client.post(reverse('register'), self.user_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Add a cleanup step to un-authenticate after the request
        self.client.force_authenticate(user=None)

    def test_token_obtain_pair(self):
        response = self.client.post(reverse('login'), {'username': 'john', 'password': 'test1234'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)

    def test_verify_token(self):
        login_response = self.client.post(reverse('login'), {'username': 'john', 'password': 'test1234'})
        verify_response = self.client.post(reverse('token_verify'), {'token': login_response.data['access']})
        self.assertEqual(verify_response.status_code, status.HTTP_200_OK)
        self.assertTrue(verify_response.data['valid'])

    def test_user_test_view(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(reverse('test'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
