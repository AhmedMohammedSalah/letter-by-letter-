from django.contrib.auth.backends import BaseBackend,ModelBackend
from .models import CustomUser
class AdminAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        # Authenticate admin users using username and password
        user = super().authenticate(request, username=username, password=password, **kwargs)
        if user and user.is_staff:
            return user  # Return the authenticated admin user
        return None  # Return None if authentication fails or user is not admin

class NIDAuthenticationBackend(BaseBackend):
    def authenticate(self, request, nid=None):
        try:
            user = CustomUser.objects.get(nid=nid)
        except CustomUser.DoesNotExist:
            return None
        return user

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None