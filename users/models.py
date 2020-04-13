from django.db import models
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser
from safedelete.models import SafeDeleteModel, SOFT_DELETE_CASCADE

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin, SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    is_active = models.BooleanField(default=False)
    email_token = models.CharField(max_length=255)
    email_token_expired_at = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    class Meta:
        app_label = 'users'
        db_table = 'user'

    @property
    def full_name(self):
        return self.name

    @property
    def short_name(self):
        return self.name

    def __str__(self):
        return self.email
