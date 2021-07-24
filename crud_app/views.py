from django.shortcuts import render
from django.views.generic import TemplateView
from crud_app.models import UserModel,CompanyModel

class IndexView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['user'] = UserModel.objects.all()
        context['company'] = CompanyModel.objects.all()
        return context