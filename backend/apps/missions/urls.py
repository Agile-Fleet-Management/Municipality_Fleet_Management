from .views import MissionViewSet, DriverViewSet, MissionParticipantViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'missions', MissionViewSet)
router.register(r'drivers', DriverViewSet)
router.register(r'mission_participants', MissionParticipantViewSet)
urlpatterns = router.urls