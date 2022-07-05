from django.views.generic import ListView

from apps.departments.models import Department


class ListDepartments(ListView):
    model = Department
    paginated_by = 12

    def get_queryset(self):
        logged_company = self.request.user.employee.company
        queryset = Department.objects.filter(company=logged_company)

        return queryset
