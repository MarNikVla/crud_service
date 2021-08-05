from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, UpdateView
from django.contrib.auth.forms import UserCreationForm

from accounts.forms import UserProfileEditForm, AdminProfileEditForm
from accounts.models import Profile


class HomePageView(TemplateView):
    """Home page"""
    template_name = 'home.html'


class LoginUserView(LoginView):
    template_name = 'registration/login.html'

    def get_success_url(self):
        return reverse_lazy('accounts:update_profile', kwargs={'pk': self.request.user.profile.pk})


class LogoutUserView(LogoutView):
    next_page = reverse_lazy('home')


class ProfileUpdateDoneView(TemplateView):
    template_name = 'accounts/update_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        updated_pk = self.kwargs['pk']
        context['updated_profile'] = Profile.objects.get(pk=updated_pk)
        return context


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

    # Только сам пользователь и администратор могут изменять профиль пользователя
    def user_has_permissions(self, request):
        is_admin = self.request.user.profile.is_admin
        is_profile_owner = self.request.user.profile.pk == self.kwargs['pk']
        return is_admin or is_profile_owner


class ProfileUpdateView(EditProfilePermissionsMixin, UpdateView):
    """Update Profile view"""
    model = Profile
    template_name = 'accounts/update_profile.html'

    def get_success_url(self):
        return reverse_lazy('accounts:update_done', kwargs={'pk': self.kwargs['pk']})

    # Разнные формы изменения профиля пользователя
    # для разных ролей пользователей
    def get_form_class(self):
        if self.request.user.profile.is_admin:
            return AdminProfileEditForm
        return UserProfileEditForm


class ProfileListView(ListView):
    """List of all profiles"""
    model = Profile
    template_name = 'accounts/users_list.html'
    context_object_name = 'profiles'

    # Исключаем суперюзера из отображения списка пользователей
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.exclude(user__is_superuser=True)


class ProfileDetailView(DetailView):
    """Info about profile"""
    model = Profile
    template_name = 'accounts/user_detail.html'
    context_object_name = 'profile'
