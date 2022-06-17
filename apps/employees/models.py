from django.db import models


class Employee(models.Model):
    nome = models.CharField(max_length=50, help_text='employee name')

    def __str__(self):
        return self.nome
