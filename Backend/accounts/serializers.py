from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Call parent to authenticate and get access/refresh
        data = super().validate(attrs)

        # Add custom claims
        data['role'] = self.user.role
        data['username'] = self.user.username
        data['full_name'] = self.user.full_name or ''

        return data