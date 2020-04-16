from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from users.permissions import *
from .services import *
from .models import User
from utils.mailers import send_verify_email
from todos.models import Todo


class SignInApi(APIView):
    permission_classes = [AllowAny, ]

    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField(required=True, max_length=255)
        password = serializers.CharField(required=True, max_length=255)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'email', 'name', 'tel', 'created_at')

    def post(self, request):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        auth_token = authenticate_user(**input_serializer.validated_data)
        user = auth_token.user
        output_serializer = self.OutputSerializer(user)
        return Response({
            'user': output_serializer.data,
            'token': auth_token.key
        }, status=status.HTTP_200_OK)


class SignUpApi(APIView):
    permission_classes = [AllowAny, ]

    class InputSerializer(serializers.Serializer):
        email = serializers.EmailField(required=True, max_length=255)
        name = serializers.CharField(required=True, max_length=255)
        password = serializers.CharField(required=True, max_length=255)
        password_confirmation = serializers.CharField(required=True, max_length=255)
        tel = serializers.CharField(required=True, max_length=255)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'email', 'name', 'tel', 'created_at')

    def post(self, request):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        user = create_user(data=input_serializer.validated_data)
        send_verify_email(user=user)
        output_serializer = self.OutputSerializer(user)
        return Response({
            'user': output_serializer.data
        }, status=status.HTTP_200_OK)


class UserVerifyEmailApi(APIView):
    permission_classes = [AllowAny, ]

    class InputSerializer(serializers.Serializer):
        email_token = serializers.CharField(required=True, max_length=255)

    def put(self, request):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        user = get_user_by(email_token=input_serializer.validated_data.get('email_token'))
        activate_user(user=user)
        return Response(status=status.HTTP_200_OK)


class UserDetailApi(APIView):
    permission_classes = [UserPermission, ]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'email', 'name', 'tel', 'created_at')

    def get(self, request, user_id):
        user = get_user_by(id=user_id)
        self.check_object_permissions(request, obj=user)
        output_serializer = self.OutputSerializer(user)
        return Response({'user': output_serializer.data})


class UserUpdateApi(APIView):
    permission_classes = [UserPermission, ]

    class InputSerializer(serializers.Serializer):
        name = serializers.CharField(max_length=255)
        tel = serializers.CharField(max_length=255)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'email', 'name', 'tel', 'created_at')

    def put(self, request, user_id):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        user = get_user_by(id=user_id)
        self.check_object_permissions(request=request, obj=user)
        user = update_user(data=input_serializer.validated_data, user=user)
        output_serializer = self.OutputSerializer(user)
        return Response({
            'user': output_serializer.data
        }, status=status.HTTP_200_OK)


class UserDeactivateApi(APIView):
    permission_classes = [UserPermission, ]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = User
            fields = ('id', 'email', 'name', 'tel', 'created_at')

    def delete(self, request, user_id):
        user = get_user_by(id=user_id)
        self.check_object_permissions(request=request, obj=user)
        deactivate_user(user)
        output_serializer = self.OutputSerializer(user)
        return Response({
            'user': output_serializer.data
        }, status=status.HTTP_200_OK)


class UserChangePasswordApi(APIView):
    permission_classes = [UserPermission, ]

    class InputSerializer(serializers.Serializer):
        old_password = serializers.CharField(required=True, max_length=255)
        password = serializers.CharField(required=True, max_length=255)
        password_confirmation = serializers.CharField(required=True, max_length=255)

    def put(self, request, user_id):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        user = get_user_by(id=user_id)
        self.check_object_permissions(request=request, obj=user)
        change_password(user=user, data=input_serializer.validated_data)
        return Response(status=status.HTTP_200_OK)


class UserListTodoApi(APIView):
    permission_classes = [IsAuthenticated, ]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Todo
            fields = ['id', 'content', 'is_complete', 'created_at', 'updated_at']

    def get(self, request, user_id):
        user = get_user_by(id=user_id)
        todos = list(user.todos.all())
        serializer = self.OutputSerializer(todos, many=True)
        return Response({'todos': serializer.data}, status=status.HTTP_200_OK)
