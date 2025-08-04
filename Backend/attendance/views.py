# attendance/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from .models import Attendance
from .serializers import AttendanceSerializer
from accounts.models import User
from timetable.models import TimetableCell
from classes.models import ClassSection

class AttendanceStudentView(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'student':
            return Attendance.objects.filter(student=self.request.user)
        return Attendance.objects.none()


class AttendanceFacultyView(generics.ListCreateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role in ['faculty', 'admin']:
            # Get all sections taught by this faculty
            section_ids = self.request.user.sections_taught.values_list('id', flat=True)
            return Attendance.objects.filter(cell__section_id__in=section_ids)
        return Attendance.objects.none()

    def perform_create(self, serializer):
        if self.request.user.role not in ['faculty', 'admin']:
            raise PermissionDenied("Only faculty can mark attendance.")
        serializer.save()