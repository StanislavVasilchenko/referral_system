from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = None

    phone = models.CharField(max_length=12, unique=True, verbose_name='phone number')
    invite_code = models.CharField(max_length=6, unique=True, verbose_name='invite code')
    verify_code = models.CharField(max_length=4, verbose_name='verify', blank=True, null=True)
    subscribed_code = models.CharField(max_length=6, verbose_name='subscribed', blank=True, null=True)

    USERNAME_FIELD = "phone"
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.phone}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
