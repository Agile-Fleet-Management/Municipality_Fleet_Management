
from django.contrib import admin

from django.urls import path, include

urlpatterns = [
    # ... your other url patterns
    path('admin/', admin.site.urls),
    path('vehicle/', include('apps.Vehicles.urls')),
    # ...
]










# from django.urls import path,include
# from .views import home
# # from apps.Vehicles import urls
# from apps.Vehicles import urls as vehicles_urls


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('home/', home, name='home'),
#     path('vehicle/', include(vehicles_urls)),
# ]

