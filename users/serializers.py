from rest_framework import serializers
from rest_framework.fields import SerializerMethodField

from users.models import User


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone']


class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['verify_code']


class UserProfileSerializer(serializers.ModelSerializer):
    subscriber = SerializerMethodField()

    def get_subscriber(self, obj):
        subscriber = User.objects.filter(subscribed_code=obj.invite_code)
        return UserRegistrationSerializer(subscriber, many=True, read_only=True).data

    class Meta:
        model = User
        fields = ['phone', 'invite_code', 'subscriber']
