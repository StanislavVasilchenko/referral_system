from rest_framework import generics
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserSerializer
from users.utils import generate_invite_cod, generate_verify_code


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        phone = serializer.validated_data.get('phone')
        User.objects.create(
            phone=phone,
            invite_code=generate_invite_cod(),
            verify_code=generate_verify_code(),
            is_active=False,
        )


class LoginAPIView(APIView):
    ...


class ProfileAPIView(generics.RetrieveAPIView):
    ...
