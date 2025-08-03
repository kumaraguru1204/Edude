from django.db import models
from classes.models import ClassSection
from accounts.models import User

class TimetableCell(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]

    day = models.CharField(max_length=10, choices=DAY_CHOICES)
    period_number = models.PositiveIntegerField()  
    subject = models.CharField(max_length=100)
    classroom = models.CharField(max_length=50)
    section = models.ForeignKey(ClassSection, on_delete=models.CASCADE)
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # Prevent duplicate entries for same day & period
        unique_together = ('section', 'day', 'period_number')
        ordering = ['day', 'period_number']

    def __str__(self):
        return f"{self.section} - {self.day} P{self.period_number}: {self.subject}"