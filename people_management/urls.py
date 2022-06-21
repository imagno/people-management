from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('employees/', include('apps.employees.urls')),
    path('admin/', admin.site.urls),
]
