from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status

from .services import *
from .permissions import UserPermission


class TodoCreateApi(APIView):
    permission_classes = [IsAuthenticated, ]

    class InputSerializer(serializers.Serializer):
        content = serializers.CharField(required=True, max_length=255)

    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_todo(data=serializer.validated_data, user=request.user)
        return Response(status=status.HTTP_200_OK)


class TodoUpdateApi(APIView):
    permission_classes = [UserPermission, ]

    class InputSerializer(serializers.Serializer):
        content = serializers.CharField(max_length=255, required=False)
        is_complete = serializers.BooleanField(required=False)

    def put(self, request, todo_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = get_todo_by(id=todo_id)
        self.check_object_permissions(request=request, obj=todo)
        update_todo(data=serializer.validated_data, todo=todo)
        return Response(status=status.HTTP_200_OK)


class TodoDeleteApi(APIView):
    permission_classes = [UserPermission, ]

    def delete(self, request, todo_id):
        todo = get_todo_by(id=todo_id)
        self.check_object_permissions(request=request, obj=todo)
        delete_todo(todo=todo)
        return Response(status=status.HTTP_200_OK)
