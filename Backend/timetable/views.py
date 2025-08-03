from rest_framework import generics
from .models import TimetableCell
from .serializers import TimetableCellSerializer

class TimetableView(generics.ListAPIView):
    serializer_class = TimetableCellSerializer

    def get_queryset(self):
        section_id = self.request.query_params.get('section')
        if section_id:
            return TimetableCell.objects.filter(section_id=section_id)
        return TimetableCell.objects.none()  # Return empty if no section