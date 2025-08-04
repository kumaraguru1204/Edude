# classes/models.py
from django.db import models

class ClassSection(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey('accounts.User', on_delete=models.CASCADE, related_name='sections_taught')

    def __str__(self):
        return self.name