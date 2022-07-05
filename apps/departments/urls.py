from django.urls import path

from .views import ListDepartments

urlpatterns = [
    path('list', ListDepartments.as_view(), name='list_departments'),
]
