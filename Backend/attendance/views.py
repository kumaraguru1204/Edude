# attendance/views.py
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import Attendance
from .serializers import AttendanceSerializer
from timetable.models import TimetableCell
from rest_framework.response import Response

class AttendanceStudentView(generics.ListAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if self.request.user.role == 'student':
            return Attendance.objects.filter(student=self.request.user)
        return Attendance.objects.none()


class AttendanceMarkView(generics.CreateAPIView):
    serializer_class = AttendanceSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        data = request.data
        if not isinstance(data, list):
            return Response(
                {'error': 'Expected a list of attendance records'},
                status=400
            )

        created = []
        errors = []

        for item in data:
            try:
                student_id = item.get('student')
                cell_id = item.get('cell')
                status_val = item.get('status')
                date = item.get('date')

                if not all([student_id, cell_id, status_val, date]):
                    errors.append({'item': item, 'error': 'Missing fields'})
                    continue

                attendance = Attendance.objects.create(
                    student_id=student_id,
                    cell_id=cell_id,
                    status=status_val,
                    date=date
                )
                created.append(AttendanceSerializer(attendance).data)
            except Exception as e:
                errors.append({'item': item, 'error': str(e)})

        return Response({'created': created, 'errors': errors}, status=201)