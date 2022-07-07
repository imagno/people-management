from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.departments.models import Department


class ListDepartments(ListView):
    model = Department
    paginated_by = 12

    def get_queryset(self):
        logged_company = self.request.user.employee.company
        queryset = Department.objects.filter(company=logged_company)

        return queryset


class CreateDepartments(CreateView):
    model = Department
    fields = ['name']

    def form_valid(self, form):
        department = form.save(commit=False)
        department.company = self.request.user.employee.company

        department.save()
        return super(CreateDepartments, self).form_valid(form)


class EditDepartments(UpdateView):
    model = Department
    fields = ['name']


class DeleteDepartments(DeleteView):
    model = Department
    success_url = reverse_lazy('list_departments')
