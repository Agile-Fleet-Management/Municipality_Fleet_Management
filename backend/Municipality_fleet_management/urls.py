
from django.contrib import admin
from django.urls import path
from .views import home
from apps.users.urls import urlpatterns as user_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]
urlpatterns += user_urls

