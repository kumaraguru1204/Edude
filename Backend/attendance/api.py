# attendance/api.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from accounts.models import User
from classes.models import ClassSection

@api_view(['GET'])
def get_students_for_faculty(request):
    user = request.user
    if user.role not in ['faculty', 'admin']:
        return Response({'error': 'Not authorized'}, status=403)

    # Get sections taught by this faculty
    sections = user.sections_taught.all()
    students = User.objects.filter(role='student', studentprofile__section__in=sections).distinct()

    return Response([
        {'id': s.id, 'name': s.full_name or s.username}
        for s in students
    ])