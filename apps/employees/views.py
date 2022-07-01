from django.views.generic import ListView, UpdateView

from .models import Employee


class ListEmployees(ListView):
    model = Employee
    paginated_by = 12

    def get_queryset(self):
        logged_company = self.request.user.employee.company
        queryset = Employee.objects.filter(company=logged_company)

        return queryset


class EditEmployee(UpdateView):
    model = Employee
    fields = ['name', 'departments']
