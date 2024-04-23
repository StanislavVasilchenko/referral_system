from datetime import datetime, timezone
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User
from users.serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer
from users.utils import generate_invite_cod, generate_verify_code, send_verify_sms


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        phone = serializer.validated_data.get('phone')
        verify_cod = generate_verify_code()
        User.objects.create(
            phone=phone,
            invite_code=generate_invite_cod(),
            verify_code=verify_cod,
            is_active=False,
        )
        send_verify_sms(verify_cod)


class LoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    queryset = User.objects.all()

    def post(self, request, *args, **kwargs):
        verify_code = request.data.get('verify_code')
        user = User.objects.filter(verify_code=verify_code).first()
        if user:
            user = self.queryset.get(verify_code=verify_code)
            user.is_active = True
            user.verify_code = None
            user.last_login = datetime.now(tz=timezone.utc)
            user.save()
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        return Response({'message': 'invalid verification code'}, status=status.HTTP_400_BAD_REQUEST)


class UserProfileAPIView(generics.RetrieveAPIView):
    model = User
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()


class UserUpdateAPIView(generics.UpdateAPIView):
    model = User
    serializer_class = UserProfileSerializer
    queryset = User.objects.all()

    def update(self, request, *args, **kwargs):
        subscribed_code = request.data['subscribed_code']
        user = User.objects.get(id=kwargs['pk'])
        if subscribed_code and user.subscribed_code != subscribed_code:
            user.subscribed_code = subscribed_code
            user.save()
            return Response({'message': f'Add {subscribed_code} in your profile'}, status=status.HTTP_200_OK)
        return Response({'message': f'{subscribed_code} already subscribed'}, status=status.HTTP_400_BAD_REQUEST)
