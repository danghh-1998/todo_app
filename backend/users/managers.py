import binascii
from datetime import timedelta
import os

from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.conf import settings
from safedelete.managers import SafeDeleteManager


class UserManager(BaseUserManager, SafeDeleteManager):
    def create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.email_token = binascii.hexlify(os.urandom(20)).decode()
        user.email_token_expired_at = timezone.now() + timedelta(seconds=settings.TOKEN_EXPIRED_AFTER_SECONDS)
        user.save(using=self._db)
        return user
