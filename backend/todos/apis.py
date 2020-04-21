from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from .services import *
from .permissions import UserPermission
from .models import Todo
from users.services import get_user_by


class TodoListApi(APIView):
    permission_classes = [UserPermission, ]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Todo
            fields = ['id', 'content', 'is_complete', 'created_at', 'updated_at']

    def get(self, request):
        user = get_user_by(id=request.user.id)
        todos = list(user.todos.all())
        self.check_object_permissions(request=request, obj=todos)
        serializer = self.OutputSerializer(todos, many=True)
        return Response({'todos': serializer.data}, status=status.HTTP_200_OK)


class TodoCreateApi(APIView):
    permission_classes = [IsAuthenticated, ]

    class InputSerializer(serializers.Serializer):
        content = serializers.CharField(required=True, max_length=255)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Todo
            fields = ['id', 'content', 'is_complete', 'created_at', 'updated_at']

    def post(self, request):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        todo = create_todo(data=input_serializer.validated_data, user=request.user)
        output_serializer = self.OutputSerializer(todo)
        return Response({
            'todo': output_serializer.data
        }, status=status.HTTP_200_OK)


class TodoUpdateApi(APIView):
    permission_classes = [UserPermission, ]

    class InputSerializer(serializers.Serializer):
        content = serializers.CharField(max_length=255, required=False)
        is_complete = serializers.BooleanField(required=False)

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Todo
            fields = ['id', 'content', 'is_complete', 'created_at', 'updated_at']

    def put(self, request, todo_id):
        input_serializer = self.InputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        todo = get_todo_by(id=todo_id)
        self.check_object_permissions(request=request, obj=todo)
        todo = update_todo(data=input_serializer.validated_data, todo=todo)
        output_serializer = self.OutputSerializer(todo)
        return Response({
            'todo': output_serializer.data
        }, status=status.HTTP_200_OK)


class TodoDeleteApi(APIView):
    permission_classes = [UserPermission, ]

    class OutputSerializer(serializers.ModelSerializer):
        class Meta:
            model = Todo
            fields = ['id', 'content', 'is_complete', 'created_at', 'updated_at']

    def delete(self, request, todo_id):
        todo = get_todo_by(id=todo_id)
        self.check_object_permissions(request=request, obj=todo)
        todo = delete_todo(todo=todo)
        output_serializer = self.OutputSerializer(todo)
        return Response({
            'todo': output_serializer.data
        }, status=status.HTTP_200_OK)
