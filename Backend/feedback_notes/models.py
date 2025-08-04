from django.db import models
from accounts.models import User
from timetable.models import TimetableCell

class Note(models.Model):
    cell = models.ForeignKey(TimetableCell, on_delete=models.CASCADE)
    faculty = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Note for {self.cell.subject} by {self.faculty.username}"

class Feedback(models.Model):
    cell = models.ForeignKey(TimetableCell, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    is_anonymous = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback for {self.cell.subject}"