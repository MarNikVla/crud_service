from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from crud_app.models import UserModel,CompanyModel


class IndexView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['user'] = UserModel.objects.all()
        context['company'] = CompanyModel.objects.all()
        return context


class CompanyDetailView(DetailView):
    model = CompanyModel
    template_name = 'crud_app/company_detail.html'
    context_object_name = 'company'

    def get_queryset(self):
        company = self.kwargs.get('company_title', '')
        q = super().get_queryset()
        return q.filter(company__name=company)


def RegisterUserFormView(FormView):
    """Standard registration view"""
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super(RegisterUserFormView, self).form_valid(form)
