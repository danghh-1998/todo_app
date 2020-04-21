from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        current_user = request.user
        if type(obj) is list:
            for item in obj:
                if current_user != item.user:
                    return False
            return True
        else:
            return current_user == obj.user
