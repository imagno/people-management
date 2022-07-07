from django.urls import path

from .views import ListDepartments, CreateDepartments, EditDepartments, DeleteDepartments

urlpatterns = [
    path('list', ListDepartments.as_view(), name='list_departments'),
    path('new', CreateDepartments.as_view(), name='create_departments'),
    path('edit/<int:pk>/', EditDepartments.as_view(), name='update_departments'),
    path('delete/<int:pk>/', DeleteDepartments.as_view(), name='delete_departments'),

]
