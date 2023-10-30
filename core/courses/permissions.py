from rest_framework import permissions


class IsOwnerOrAdmin(permissions.BasePermission):
    """
    Пользователь может удалять курс только если он владелец или администратор.
    """
    def has_permission(self, request, view):
        if request.user and request.user.is_staff:
            return True

        if request.method in permissions.SAFE_METHODS:
            return True

        return False

    def has_object_permission(self, request, view, obj):
        return obj.tutor == request.user or request.user.is_staff


