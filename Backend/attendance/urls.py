# attendance/urls.py
from django.urls import path
from .views import AttendanceStudentView, AttendanceMarkView

urlpatterns = [
    path('my/', AttendanceStudentView.as_view(), name='attendance-student'),
    path('mark/', AttendanceMarkView.as_view(), name='attendance-mark'),
]