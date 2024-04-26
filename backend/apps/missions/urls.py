from .views import MissionViewSet, DriverViewSet, MissionParticipantViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'missions', MissionViewSet, basename='missions_views')
router.register(r'drivers', DriverViewSet,basename='drivers')
router.register(r'mission_participants', MissionParticipantViewSet,basename='mission_participants')
urlpatterns = router.urls