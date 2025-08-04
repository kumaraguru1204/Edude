from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Note, Feedback
from .serializers import NoteSerializer, FeedbackSerializer
from timetable.models import TimetableCell

class NoteListCreateView(generics.ListCreateAPIView):
    serializer_class = NoteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cell_id = self.request.query_params.get('cell')
        return Note.objects.filter(cell_id=cell_id)

    def perform_create(self, serializer):
        cell = TimetableCell.objects.get(id=self.request.data['cell'])
        serializer.save(faculty=self.request.user, cell=cell)

class FeedbackListCreateView(generics.CreateAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cell_id = self.request.query_params.get('cell')
        return Feedback.objects.filter(cell_id=cell_id)

    def perform_create(self, serializer):
        cell = TimetableCell.objects.get(id=self.request.data['cell'])
        serializer.save(student=self.request.user, cell=cell)

class FeedbackListView(generics.ListAPIView):
    serializer_class = FeedbackSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cell_id = self.request.query_params.get('cell')
        return Feedback.objects.filter(cell_id=cell_id)