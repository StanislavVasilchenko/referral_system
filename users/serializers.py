from rest_framework import serializers

from users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone']


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['verify_code']
