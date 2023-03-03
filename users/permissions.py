from rest_framework import permissions

class PermissionIsSuper(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated and request.user.is_employee:
            return True

        return (obj.id == request.user.id)