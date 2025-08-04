from django.contrib import admin
from .models import Attendance

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'cell', 'status', 'date')
    list_filter = ('status', 'date', 'cell__section')
    search_fields = ('student__username', 'cell__subject')