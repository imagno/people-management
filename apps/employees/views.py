from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Employee


class ListEmployees(ListView):
    model = Employee
    paginated_by = 12

    def get_queryset(self):
        logged_company = self.request.user.employee.company
        queryset = Employee.objects.filter(company=logged_company)

        return queryset


class NewEmployee(CreateView):
    model = Employee
    fields = ['name', 'departments']

    def form_valid(self, form):
        employee = form.save(commit=False)
        employee.company = self.request.user.employee.company
        employee.user = User.objects.create(username=employee.name.split(' ')[0]+employee.name.split(' ')[1])

        employee.save()
        return super(NewEmployee, self).form_valid(form)


class EditEmployee(UpdateView):
    model = Employee
    fields = ['name', 'departments']


class DeleteEmployee(DeleteView):
    model = Employee
    success_url = reverse_lazy('list_employees')
