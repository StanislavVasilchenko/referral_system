from django.urls import path

from users.apps import UsersConfig
from users.views import RegisterAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('', RegisterAPIView.as_view(), name='registration'),
]