from django.urls import path

from .views import ListEmployees, EditEmployee, DeleteEmployee

urlpatterns = [
    path('', ListEmployees.as_view(), name='list_employees'),
    path('edit/<int:pk>', EditEmployee.as_view(), name='update_employee'),
    path('delete/<int:pk>', DeleteEmployee.as_view(), name='delete_employee'),
]
