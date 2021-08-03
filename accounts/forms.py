from django import forms

from accounts.models import Profile


class ProfileEditForm(forms.ModelForm):
    """Profile edit form"""

    class Meta:
        model = Profile
        exclude = ['user','is_admin', 'is_moderator']

class AdminEditForm(forms.ModelForm):
    """Profile edit form"""

    class Meta:
        model = Profile
        exclude = ['user', 'is_moderator']
