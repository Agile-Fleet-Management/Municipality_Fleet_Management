from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Mission
from .serializers import MissionSerializer


class MissionTests(APITestCase):
    def setUp(self):
        # The setUp method is where you should create test objects
        # and perform any setup necessary before each test is run.
        self.url = reverse("missions")  # Adjust the URL name to match your urlpatterns
        self.mission_data = {
            "title": "test case 1",
            "start_time": "2024-04-09T12:00:00Z",
            "end_time": "2024-04-18T23:11:26Z",
            "status": "4",
            "expected_arrival": "2024-04-09T23:11:30Z",
            "request_time": "2024-04-09T23:09:41Z",
            "description": "test case 1",
            "requester_id": 1,
        }
        self.mission = Mission.objects.create(**self.mission_data)

    def test_create_mission(self):
        """
        Ensure we can create a new mission object.
        """
        response = self.client.post(self.url, self.mission_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Mission.objects.count(), 2)  # Assuming one was already created in setUp
