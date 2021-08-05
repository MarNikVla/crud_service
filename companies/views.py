from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponseForbidden
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import ModeratorEditForm, UserEditForm, AdminEditForm
from .models import Company


class EditCompanyPermissionsMixin(AccessMixin):

    # Только пользователи и модераторы компании могут изменять портфолио своей компании
    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.is_admin or self.user_has_permissions(request):
            return super(EditCompanyPermissionsMixin, self).dispatch(
                request, *args, **kwargs)

        return HttpResponseForbidden("You do not have permission to Edit Company Profile")

    def user_has_permissions(self, request):
        return self.request.user.profile.company.pk == self.kwargs['pk']


class DeleteCompanyPermissionsMixin(AccessMixin):

    # Только is_admin может удалять компании
    def dispatch(self, request, *args, **kwargs):
        if request.user.profile.is_admin:
            return super(DeleteCompanyPermissionsMixin, self).dispatch(
                request, *args, **kwargs)

        return HttpResponseForbidden("You do not have permission to Delete Company Profile")


class CompanyList(ListView):
    context_object_name = 'companies'
    model = Company

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.exclude(title__iexact='No company')


class CompanyCreate(CreateView):
    model = Company
    fields = ['title', ]
    success_url = reverse_lazy('companies:company_list')


class CompanyUpdateView(EditCompanyPermissionsMixin, UpdateView):
    model = Company
    success_url = reverse_lazy('companies:company_list')

    # Разнные формы изменения портфолио компании
    # для разных ролей пользователей
    def get_form_class(self):
        if self.request.user.profile.is_admin:
            return AdminEditForm
        if self.request.user.profile.is_moderator:
            return ModeratorEditForm
        return UserEditForm


class CompanyDelete(DeleteCompanyPermissionsMixin, DeleteView):
    model = Company
    success_url = reverse_lazy('companies:company_list')

    # Переопределим get_queryset чтобы случайно не удалить компанию заглушку
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.exclude(title__iexact='No company')


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'companies/company_detail.html'
    context_object_name = 'company'
