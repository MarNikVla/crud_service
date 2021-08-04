from django import forms

from accounts.models import Profile

class UserProfileEditForm(forms.ModelForm):
    """Profile edit form"""

    class Meta:
        model = Profile
        exclude = ['user','is_admin', 'is_moderator']


# class ModeratorProfileEditForm(forms.ModelForm):
#     """Profile edit form"""
#
#     class Meta:
#         model = Profile
#         exclude = ['user','is_admin', 'is_moderator']

class AdminProfileEditForm(forms.ModelForm):
    """Profile edit form"""

    class Meta:
        model = Profile
        exclude = ['user', 'is_admin']
