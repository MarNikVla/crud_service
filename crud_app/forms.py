from django import forms
from crud_app.models import Profile

class ProfileEditForm(forms.ModelForm):
    """Profile edit form"""
    class Meta:
        model = Profile
        exclude = ['user']