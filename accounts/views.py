from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.forms import UserCreationForm

from accounts.forms import ProfileEditForm
from accounts.models import Profile


class HomePageView(TemplateView):
    """Home page"""
    template_name = 'home.html'


class ProfileUpdateDoneView(TemplateView):
    template_name = 'accounts/update_done.html'


class RegisterUserFormView(FormView):
    """Standard registration view"""
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super(RegisterUserFormView, self).form_valid(form)


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    """Update Profile view"""
    form_class = ProfileEditForm
    template_name = 'accounts/update.html'
    success_url = reverse_lazy('update_done')

    def get_object(self):
        """Get object to update from request"""
        return self.request.user.profile


class ProfileListView(ListView):
    """List of all profiles"""
    model = Profile
    template_name = 'accounts/users_list.html'
    context_object_name = 'profiles'


class ProfileDetailView(DetailView):
    """Info about profile"""
    model = Profile
    template_name = 'accounts/user_detail.html'
    context_object_name = 'profile'
