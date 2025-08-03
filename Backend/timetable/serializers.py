from rest_framework import serializers
from .models import TimetableCell

class TimetableCellSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimetableCell
        fields = '__all__'