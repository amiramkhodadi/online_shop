from django.conf import settings
from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.hashers import check_password
from account.models import User


class SettingsBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
            try:
                user = User.objects.get(email=username)
                if user.check_password(password):
                    return user
                return None
            except User.DoesNotExist:
                return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None