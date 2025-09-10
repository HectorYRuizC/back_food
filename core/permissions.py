from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        user = getattr(obj, "user", None)
        return user == request.user

class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)
