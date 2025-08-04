from django.urls import path
from .views import NoteListCreateView, FeedbackListCreateView, FeedbackListView

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('feedback/', FeedbackListCreateView.as_view(), name='feedback-create'),
    path('feedback/list/', FeedbackListView.as_view(), name='feedback-list'),
]