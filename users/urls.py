from django.urls import path
from .apis import SignInApi, UserDetailApi, UserUpdateApi, UserDeactivateApi, \
    UserChangePasswordApi, SignUpApi

urlpatterns = [
    path('auth/sign_up', SignUpApi.as_view(), name='sign_up'),
    path('auth/sign_in', SignInApi.as_view(), name='sign_in'),
    path('users/<int:user_id>', UserDetailApi.as_view(), name='user_detail'),
    path('users/<int:user_id>/update', UserUpdateApi.as_view(), name='user_update'),
    path('users/<int:user_id>/deactivate', UserDeactivateApi.as_view(), name='user_deactivate'),
    path('users/<int:user_id>/change_password', UserChangePasswordApi.as_view(), name='user_change_password'),
]
