from django.contrib.auth.mixins import AccessMixin
from django.http import HttpResponse, Http404, HttpResponseNotAllowed, HttpResponseForbidden
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Company


class EditCompanyPermissionsMixin(AccessMixin):
    pass
    #
    # def dispatch(self, request, *args, **kwargs):
    #     if request.user.is_authenticated and self.user_has_permissions(request):
    #         return super(EditCompanyPermissionsMixin, self).dispatch(
    #             request, *args, **kwargs)
    #
    #     return HttpResponseForbidden("You do not have permission to Edit or Delete Company Profile")
    #
    # def user_has_permissions(self, request):
    #     print(self.__dir__())
    #     print(self.fields)
    #     # print(self.get_deferred_fields(self))
    #     return self.request.user.profile.company.pk == self.kwargs['pk']


class CompanyList(ListView):
    context_object_name = 'companies'
    model = Company


class CompanyCreate(CreateView):
    model = Company
    fields = ['title', ]
    success_url = reverse_lazy('companies:company_list')


class CompanyUpdate(EditCompanyPermissionsMixin, UpdateView):
    model = Company
    fields = ['title', 'description']
    success_url = reverse_lazy('companies:company_list')

    def get_queryset(self):
        qs = super().get_queryset()
        # if self.request.user ==
        return Company.objects.filter(staff=self.request.user)


        # if request.user.is_superuser:
        #     return qs
        # return qs.filter(author=request.user)



class CompanyDelete(EditCompanyPermissionsMixin,DeleteView):
    model = Company
    success_url = reverse_lazy('companies:company_list')
