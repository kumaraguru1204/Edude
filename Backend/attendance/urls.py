from django.urls import path
from .views import AttendanceStudentView, AttendanceFacultyView

urlpatterns = [
    path('my/', AttendanceStudentView.as_view(), name='attendance-student'),
    path('mark/', AttendanceFacultyView.as_view(), name='attendance-faculty'),
]