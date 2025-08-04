# classes/urls.py
from django.urls import path
from .api import get_students_for_faculty

urlpatterns = [
    path('students/', get_students_for_faculty, name='get-students'),
]