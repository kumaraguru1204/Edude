# accounts/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

ROLE_CHOICES = [
    ('student', 'Student'),
    ('faculty', 'Faculty'),
    ('admin', 'Admin'),
]

class User(AbstractUser):
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    full_name = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"


class StudentProfile(models.Model):
    user = models.OneToOneField('accounts.User', on_delete=models.CASCADE, related_name='student_profile')
    section = models.ForeignKey('classes.ClassSection', on_delete=models.CASCADE)
    enrollment_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.user.username} - {self.section.name}"