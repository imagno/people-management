from django.urls import path

from .views import ListEmployees, EditEmployee

urlpatterns = [
    path('', ListEmployees.as_view(), name='list_employees'),
    path('edit/<int:pk>', EditEmployee.as_view(), name='update_employee'),
]
