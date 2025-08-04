from rest_framework import serializers
from .models import Attendance

class AttendanceSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.username', read_only=True)
    subject = serializers.CharField(source='cell.subject', read_only=True)

    class Meta:
        model = Attendance
        fields = ['id', 'student', 'student_name', 'cell', 'subject', 'status', 'date']