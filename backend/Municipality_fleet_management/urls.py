
from django.contrib import admin

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ... your other url patterns
    path('admin/', admin.site.urls),
    path('vehicle/', include('apps.Vehicles.urls')),
    # ...
]


# Add this line at the bottom of your urlpatterns list
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)








# from django.urls import path,include
# from .views import home
# # from apps.Vehicles import urls
# from apps.Vehicles import urls as vehicles_urls


# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('home/', home, name='home'),
#     path('vehicle/', include(vehicles_urls)),
# ]

