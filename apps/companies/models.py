from django.db import models
from django.shortcuts import reverse


class Company(models.Model):
    name = models.CharField(max_length=50, help_text='company name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')
