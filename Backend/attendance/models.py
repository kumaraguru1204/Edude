from django.db import models
from accounts.models import User
from timetable.models import TimetableCell

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    ]

    student = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'student'})
    cell = models.ForeignKey(TimetableCell, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    date = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'cell', 'date')
        ordering = ['-date']

    def __str__(self):
        return f"{self.student.username} - {self.cell.subject} - {self.status}"