import binascii
import os
from datetime import timedelta

from django.contrib.auth import authenticate
from rest_framework.exceptions import ValidationError, APIException, AuthenticationFailed
from django.utils import timezone
from django.conf import settings

from auth_tokens.services import expire_token, create_token
from .models import User


def create_user(data, **kwargs):
    for key, value in kwargs.items():
        data[key] = value
    if data.get('password') != data.get('password_confirmation'):
        raise ValidationError('passsword and password confirmation don\'t match')
    validated_data = data.copy()
    validated_data.pop('password_confirmation')
    user = User.objects.create_user(**dict(validated_data))
    return user


def update_user(user, data):
    if not any(data.values()):
        raise ValidationError
    user.name = data.get('name') or user.name
    user.tel = data.get('tel') or user.tel
    user.save(update_fields=['name', 'tel'])


def deactivate_user(user):
    expire_token(user=user)
    user.is_active = False
    user.save(update_fields=['is_active'])
    user.delete()


def activate_user(user):
    if user.email_token_expired_at < timezone.now():
        user.email_token = binascii.hexlify(os.urandom(20)).decode()
        user.email_token_expired_at = timezone.now() + timedelta(settings.TOKEN_EXPIRED_AFTER_SECONDS)
        user.save(update_fields=['email_token', 'email_token_expired_at'])
        raise APIException('Token expired')
    user.is_active = True
    user.save(update_fields=['is_active'])


def change_password(user, data):
    if data.get('password') != data.get('password_confirmation'):
        raise ValidationError
    authenticate_user(email=user.email, password=data.get('old_password'))
    user.set_password(data.get('new_password'))
    user.change_init_password = True
    user.save(update_fields=['password', 'change_init_password'])


def authenticate_user(email, password):
    user = authenticate(email=email, password=password)
    if not user:
        raise AuthenticationFailed
    expire_token(user=user)
    auth_token = create_token(user=user)
    return auth_token.key


def get_user_by(**kwargs):
    user = User.objects.get(**kwargs)
    if not user:
        raise APIException(code=200, detail='object not found')
    return user


def get_deleted_user_by(**kwargs):
    user = User.objects.deleted_only().get(**kwargs)
    if not user:
        raise APIException(code=200, detail='object not found')
    return user
