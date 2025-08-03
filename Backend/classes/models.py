from django.db import models
from accounts.models import User

class ClassSection(models.Model):
    name = models.CharField(max_length=50)
    faculty = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'faculty'},
        related_name='sections_taught'
    )

    def __str__(self):
        return self.name