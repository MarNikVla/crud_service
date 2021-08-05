from django import forms

from accounts.models import Profile

class UserProfileEditForm(forms.ModelForm):
    """User form"""

    class Meta:
        model = Profile
        exclude = ['user','is_admin', 'is_moderator']


class AdminProfileEditForm(forms.ModelForm):
    """if profile.is_admin form"""

    class Meta:
        model = Profile
        exclude = ['user', 'is_admin']
