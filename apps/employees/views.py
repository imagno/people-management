from django.views.generic import ListView

from .models import Employee


class ListEmployees(ListView):
    model = Employee
    paginated_by = 12
