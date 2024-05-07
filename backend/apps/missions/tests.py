# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
# from .models import Mission, Driver, MissionParticipant
# from apps.users.models import User, Role
# from apps.Vehicles.models import Vehicle, Vtype
# from .serializers import MissionSerializer
# from rest_framework.test import APIClient


# class MissionTests(APITestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.admin_role = Role.objects.create(name="Admin", description="Administrator role")
#         self.admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')

#         # Authenticate as the admin user before making the request
#         self.client.force_authenticate(user=self.admin_user)

#         self.role = Role.objects.create(name="admin", description="A test")

#         self.user = User.objects.create_user(
#             username="testuser",
#             password="testpassword123",
#             phone_number="1234567890",
#             address="123 Test St",
#             role=self.role,
#         )
#         self.mission1 = Mission.objects.create(
#             title="Mission 1",
#             start_time="2024-04-10T12:00:00Z",
#             end_time="2024-04-11T12:00:00Z",
#             status="1",
#             expected_arrival="2024-04-10T15:00:00Z",
#             requester_id=self.user,
#             request_time="2024-04-09T23:09:41Z",
#             description="First test mission",
#         )

#         self.mission2 = Mission.objects.create(
#             title="Mission 2",
#             start_time="2024-04-12T12:00:00Z",
#             end_time="2024-04-13T12:00:00Z",
#             status="2",
#             expected_arrival="2024-04-12T15:00:00Z",
#             requester_id=self.user,
#             request_time="2024-04-11T23:09:41Z",
#             description="Second test mission",
#         )

#     def test_get_all_missions(self):
#         """
#         Ensure we can retrieve a list of all mission objects.
#         """
#         url = reverse("missions_views-list")
#         response = self.client.get(url, format="json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 2)

#         expected_titles = ["Mission 1", "Mission 2"]
#         received_titles = [mission["title"] for mission in response.data]
#         self.assertTrue(all(title in received_titles for title in expected_titles))

#     def test_get_specific_mission(self):
#         """
#         Ensure we can retrieve details of a specific mission.
#         """
#         url = reverse("missions_views-detail", args=[self.mission1.id])
#         response = self.client.get(url, format="json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["id"], self.mission1.id)

#     def test_create_account(self):
#         """
#         Ensure we can create a new account object.
#         """
#         url = reverse("missions_views-list")
#         data = {
#             "title": "tests",
#             "start_time": "2024-04-09T12:00:00Z",
#             "end_time": "2024-04-18T23:11:26Z",
#             "status": "4",
#             "expected_arrival": "2024-04-09T23:11:30Z",
#             "request_time": "2024-04-09T23:09:41Z",
#             "description": "test case 1",
#             "requester_id": self.user.id,
#         }
#         response = self.client.post(url, data, format="json")
#         if response.status_code != status.HTTP_201_CREATED:
#             print(response.data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_delete_mission(self):
#         """
#         Ensure we can delete an existing mission.
#         """
#         url = reverse("missions_views-detail", args=[self.mission2.id])
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_update_mission(self):
#         """
#         Ensure we can update an existing mission.
#         """
#         url = reverse("missions_views-detail", args=[self.mission1.id])
#         updated_data = {
#             "title": "Updated Mission",
#             "start_time": "2024-04-11T12:00:00Z",
#             "end_time": "2024-04-12T12:00:00Z",
#             "status": "5",  # Example of changing status
#             "expected_arrival": "2024-04-11T15:00:00Z",
#             "request_time": "2024-04-10T23:09:41Z",
#             "description": "Updated description",
#             "requester_id": self.user.id,
#         }
#         response = self.client.put(url, updated_data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         self.mission1.refresh_from_db()

#         self.assertEqual(self.mission1.title, "Updated Mission")
#         self.assertEqual(self.mission1.description, "Updated description")
#         self.assertEqual(self.mission1.status, "5")

#     def test_patch_update_mission(self):
#         """
#         Ensure we can partially update an existing mission using PATCH.
#         """
#         url = reverse("missions_views-detail", args=[self.mission1.id])
#         patch_data = {
#             "title": "Patched",
#             "status": "3",
#         }
#         response = self.client.patch(url, patch_data, format="json")
#         if response.status_code != status.HTTP_200_OK:
#             print("Response data:", response.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         self.mission1.refresh_from_db()

#         self.assertEqual(self.mission1.title, "Patched")
#         self.assertEqual(self.mission1.status, "3")

#         # Verify that other fields were not changed
#         self.assertEqual(self.mission1.description, "First test mission")


# class DriverTests(APITestCase):
#     def setUp(self):
#         super().setUp()

#         self.client = APIClient()
#         self.admin_role = Role.objects.create(name="Admin", description="Administrator role")
#         self.admin_user = User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')

#         # Authenticate as the admin user before making the request
#         self.client.force_authenticate(user=self.admin_user)
        
#         self.role = Role.objects.create(name="Test Role", description="A test")
#         self.user = User.objects.create_user(
#             username="testuser",
#             password="testpassword123",
#             phone_number="1234567890",
#             address="123 Test St",
#             role=self.role,
#         )

#         self.mission1 = Mission.objects.create(
#             title="Mission 1",
#             start_time="2024-04-10T12:00:00Z",
#             end_time="2024-04-11T12:00:00Z",
#             status="1",
#             expected_arrival="2024-04-10T15:00:00Z",
#             requester_id=self.user,
#             request_time="2024-04-09T23:09:41Z",
#             description="First test mission",
#         )
#         self.mission2 = Mission.objects.create(
#             title="Mission 2",
#             start_time="2024-04-12T12:00:00Z",
#             end_time="2024-04-13T12:00:00Z",
#             status="2",
#             expected_arrival="2024-04-12T15:00:00Z",
#             requester_id=self.user,
#             request_time="2024-04-11T23:09:41Z",
#             description="Second test mission",
#         )

#         self.vehicle_type = Vtype.objects.create(
#             name="Ambulance", description="Ambulance type vehicle"
#         )
#         self.vehicle1 = Vehicle.objects.create(
#             brand="Toyota",
#             model="Corolla",
#             age=2,
#             status="2",
#             Vtype=self.vehicle_type,
#             kms="50000",
#             notification_time_year=3,
#             notification_mileage=50000.0,
#         )
#         self.vehicle2 = Vehicle.objects.create(
#             brand="Mercedes",
#             model="Benz",
#             age=1,
#             status="2",
#             Vtype=self.vehicle_type,
#             kms="20000",
#             notification_time_year=4,
#             notification_mileage=40000.0,
#         )
#         self.vehicle3 = Vehicle.objects.create(
#             brand="Toyota",
#             model="Benz",
#             age=1,
#             status="2",
#             Vtype=self.vehicle_type,
#             kms="20000",
#             notification_time_year=4,
#             notification_mileage=40000.0,
#         )
#         self.driver1 = Driver.objects.create(
#             mission_id=self.mission1, vehicle_id=self.vehicle2, driver_id=self.user
#         )
#         self.driver2 = Driver.objects.create(
#             mission_id=self.mission1, vehicle_id=self.vehicle1, driver_id=self.user
#         )

#     def test_create_driver(self):
#         """
#         Ensure we can create a new driver object.
#         """
#         url = reverse("drivers-list")
#         data = {
#             "mission_id": self.mission2.id,
#             "vehicle_id": self.vehicle1.id,
#             "driver_id": self.user.id,
#         }
#         response = self.client.post(url, data, format="json")
#         if response.status_code != status.HTTP_201_CREATED:
#             print("Response data:", response.data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_get_driver_details(self):
#         """
#         Ensure we can retrieve details of a specific driver.
#         """
#         url = reverse("drivers-detail", args=[self.driver1.id])
#         response = self.client.get(url, format="json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["id"], self.driver1.id)

#     def test_update_driver(self):
#         """
#         Ensure we can update an existing driver.
#         """
#         url = reverse("drivers-detail", args=[self.driver1.id])
#         updated_data = {
#             "mission_id": self.mission2.id,
#             "vehicle_id": self.vehicle1.id,
#             "driver_id": self.user.id,
#         }
#         response = self.client.put(url, updated_data, format="json")
#         if response.status_code != status.HTTP_200_OK:
#             print("Response data:", response.data)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_patch_update_driver(self):
#         """
#         Ensure we can partially update an existing driver using PATCH.
#         """
#         url = reverse("drivers-detail", args=[self.driver1.id])
#         patch_data = {
#             "vehicle_id": self.vehicle3.id,
#         }
#         response = self.client.patch(url, patch_data, format="json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         if response.status_code != status.HTTP_200_OK:
#             print("Response data:", response.data)
#         self.driver1.refresh_from_db()
#         self.assertEqual(self.driver1.vehicle_id.id, self.vehicle3.id)

#     def test_delete_driver(self):
#         """
#         Ensure we can delete an existing driver.
#         """
#         url = reverse("drivers-detail", args=[self.driver1.id])
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#     def test_view_all_drivers(self):
#         """
#         Ensure we can view all drivers.
#         """
#         url = reverse("drivers-list")
#         response = self.client.get(url, format="json")
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(len(response.data), 2)

#         expected_ids = {self.driver1.id, self.driver2.id}
#         received_ids = {driver["id"] for driver in response.data}
#         self.assertTrue(expected_ids == received_ids)
