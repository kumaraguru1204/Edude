from django.urls import path
from .views import TimetableView

urlpatterns = [
    path('', TimetableView.as_view(), name='timetable-list'),
]