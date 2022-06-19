from django.db import models


class Document(models.Model):
    register_id = models.IntegerField(null=True, help_text='register document number')
    description = models.CharField(max_length=150, help_text='text description document')

    def __int__(self):
        return self.register_id

    def __str__(self):
        return self.description
