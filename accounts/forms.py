from django import forms

from accounts.models import Profile


class ProfileEditForm(forms.ModelForm):
    """Profile edit form"""

    class Meta:
        model = Profile
        exclude = ['user','company']
