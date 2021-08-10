from rest_framework.permissions import BasePermission

class AdminPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.profile.is_admin:
            return True
        return False


class AuthenticatedUserPermissions(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.profile.company.pk == int(view.kwargs['pk']):
            return True
        return False