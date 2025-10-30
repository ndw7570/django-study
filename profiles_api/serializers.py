from rest_framework import serializers

from profiles_api import models

class NamTestHelloMessageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=10)
    message = serializers.CharField(max_length=100)
    class Meta:
        model = models.NamTestHelloMessage
        fields = ['id', 'name', 'message']

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']

        )

        return user