from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny

from api.permissions import AdminPermissions, AuthenticatedUserPermissions
from api.serializers import AdminCompanySerializer, UserCompanySerializer, ModeratorCompanySerializer
from companies.models import Company


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all().exclude(title__iexact='No company')
    permission_classes = [AllowAny, ]

    permission_classes_by_action = {
        'create': [AdminPermissions],
        'list': [AllowAny],
        'update': [AuthenticatedUserPermissions | AdminPermissions],
        'partial_update': [AuthenticatedUserPermissions | AdminPermissions],
        'destroy': [AdminPermissions],
    }

    def get_permissions(self):
        try:
            # return permission_classes depending on `action`
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except (KeyError):
            # action is not set return default permission_classes
            return [permission() for permission in self.permission_classes]

    def get_serializer_class(self):
        if not bool(self.request.user and self.request.user.is_authenticated):
            return UserCompanySerializer
        if self.request.user.profile.is_admin:
            return AdminCompanySerializer
        elif self.request.user.profile.is_moderator:
            return ModeratorCompanySerializer
        else:
            return UserCompanySerializer
