from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseForbidden
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


class LoginUserView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('accounts:update_profile')
    # success_url = reverse_lazy('accounts:update_profile')


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('home')


class ProfileUpdateDoneView(TemplateView):
    template_name = 'accounts/update_done.html'


class RegisterUserFormView(FormView):
    """Standard registration view"""
    form_class = UserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        form.save()
        return super(RegisterUserFormView, self).form_valid(form)


class EditProfilePermissionsMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and self.user_has_permissions(request):
            return super(EditProfilePermissionsMixin, self).dispatch(
                request, *args, **kwargs)

        return HttpResponseForbidden("You do not have permission to Edit User Profile")

    def user_has_permissions(self, request):
        return self.request.user.profile.pk == self.kwargs['pk']


class ProfileUpdateView(EditProfilePermissionsMixin, UpdateView):
    """Update Profile view"""
    model = Profile
    form_class = ProfileEditForm
    template_name = 'accounts/update_profile.html'
    success_url = reverse_lazy('accounts:update_done')

    # def get_object(self):
    #     """Get object to update from request"""
    #     return self.request.user.profile


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
