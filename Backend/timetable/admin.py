from django.contrib import admin
from .models import TimetableCell

@admin.register(TimetableCell)
class TimetableCellAdmin(admin.ModelAdmin):
    list_display = ('section', 'day', 'period_number', 'subject', 'classroom', 'faculty')
    list_filter = ('section', 'day', 'faculty')
    search_fields = ('subject', 'classroom')