from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponse, Http404, HttpResponseNotAllowed, HttpResponseForbidden
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import StaffEditForm, UserEditForm
from .models import Company


class EditCompanyPermissionsMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.user_has_permissions(request):
            return super(EditCompanyPermissionsMixin, self).dispatch(
                request, *args, **kwargs)

        return HttpResponseForbidden("You do not have permission to Edit Company Profile")

    def user_has_permissions(self, request):
        return self.request.user.profile.company.pk == self.kwargs['pk']


class DeleteCompanyPermissionsMixin(AccessMixin):

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

    # fields = ['title', 'description']
    success_url = reverse_lazy('companies:company_list')

    def get_form_class(self):
        if self.request.user.profile.is_moderator:
            form_class = StaffEditForm
        else:
            form_class = UserEditForm
        return form_class
        # fc= super().get_form_class()

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     # if self.request.user ==
    #     return Company.objects.filter(staff=self.request.user)

    # if request.user.is_superuser:
    #     return qs
    # return qs.filter(author=request.user)


class CompanyDelete(DeleteCompanyPermissionsMixin, DeleteView):
    model = Company
    success_url = reverse_lazy('companies:company_list')


class CompanyDetailView(DetailView):
    model = Company
    template_name = 'companies/company_detail.html'
    context_object_name = 'company'
