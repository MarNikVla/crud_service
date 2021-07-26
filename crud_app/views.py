from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, ListView

from crud_app.forms import ProfileEditForm
from crud_app.models import Profile,CompanyModel
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import FormView, UpdateView

class IndexView(TemplateView):
    template_name = "base.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['user'] = Profile.objects.all()
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


class RegisterUserFormView(FormView):
    """Standard registration view"""
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super(RegisterUserFormView, self).form_valid(form)


class ProfileUpdateDoneView(TemplateView):
    template_name = 'crud_app/update_done.html'

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Update Profile view"""
    form_class = ProfileEditForm
    template_name = 'crud_app/update.html'
    success_url = reverse_lazy('update_done')

    def get_object(self):
        """Get object to update from request"""
        return self.request.user.profile

class ProfileListView(ListView):
    """List of all profiles"""
    model = Profile
    template_name = 'crud_app/users_list.html'
    context_object_name = 'profiles'


class ProfileDetailView(DetailView):
    """Info about profile"""
    model = Profile
    template_name = 'crud_app/user_detail.html'
    context_object_name = 'profile'