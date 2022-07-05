from django.urls import path

from .views import ListEmployees, NewEmployee, EditEmployee, DeleteEmployee

urlpatterns = [
    path('', ListEmployees.as_view(), name='list_employees'),
    path('new/', NewEmployee.as_view(), name='new_employee'),
    path('edit/<int:pk>', EditEmployee.as_view(), name='update_employee'),
    path('delete/<int:pk>', DeleteEmployee.as_view(), name='delete_employee'),
]
