from django.db import models


class OvertimeRegistration(models.Model):
    reason = models.CharField(max_length=150, help_text='reason for overtime')

    def __str__(self):
        return self.reason
