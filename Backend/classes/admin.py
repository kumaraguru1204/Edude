from django.contrib import admin
from .models import ClassSection

@admin.register(ClassSection)
class ClassSectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'faculty')
    search_fields = ('name',)
    list_filter = ('faculty',)