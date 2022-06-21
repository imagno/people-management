from django.db import models

from apps.employees.models import Employee


class OvertimeRegistration(models.Model):
    reason = models.CharField(max_length=150, help_text='reason for overtime')
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT)

    def __str__(self):
        return self.reason
