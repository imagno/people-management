from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50, help_text='company name')

    def __str__(self):
        return self.name
