
from django.contrib import admin
from django.urls import path
from .views import home
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('vehicles/', include('apps.Vehicles.urls')),
    path('usres/', include('apps.users.urls')),
    path('', home, name='home'),
]


