
from django.contrib import admin
from django.urls import path
<<<<<<< Updated upstream
from views import home
=======
from .views import home
>>>>>>> Stashed changes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
]

