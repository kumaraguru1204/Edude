from django.contrib import admin
from .models import Note, Feedback

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('cell', 'faculty', 'created_at')

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('cell', 'student', 'is_anonymous', 'created_at')