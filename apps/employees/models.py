from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50, help_text='employee name')

    def __str__(self):
        return self.name
