from django.urls import path

from .views import CreateCompany, EditCompany

urlpatterns = [
    path('new', CreateCompany.as_view(), name='create_company'),
    path('edit/<int:pk>', EditCompany.as_view(), name='edit_company'),
]
