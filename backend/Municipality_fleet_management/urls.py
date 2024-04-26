
from django.contrib import admin
from django.urls import path,include
from .views import home
from apps.missions import urls as missions_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', include('apps.Vehicles.urls')),
    path('usres/', include('apps.users.urls')),
    path('', home, name='home'),
    path('Missions/', include(missions_urls), name='missions'),
]


