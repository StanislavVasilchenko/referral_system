from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterAPIView, LoginAPIView, UserProfileAPIView, UserUpdateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('', RegisterAPIView.as_view(), name='registration'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('profile/<int:pk>/', UserProfileAPIView.as_view(), name='profile'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='profile_update'),
]
