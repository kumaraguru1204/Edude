# classes/api.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import User

@api_view(['GET'])
def get_students_for_faculty(request):
    user = request.user
    if user.role not in ['faculty', 'admin']:
        return Response({'error': 'Not authorized'}, status=403)

    # Get all sections taught by this faculty
    section_ids = user.sections_taught.values_list('id', flat=True)
    # Get all students in those sections
    students = User.objects.filter(
        student_profile__section_id__in=section_ids
    ).distinct()

    return Response([
        {
            'id': s.id,
            'name': s.full_name or s.username,
            'role': s.role
        }
        for s in students
    ])