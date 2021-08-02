from django import forms

from companies.models import Company


class StaffEditForm(forms.ModelForm):
    """Staff edit form"""

    class Meta:
        model = Company
        fields = ['description', 'news']


class UserEditForm(forms.ModelForm):
    """User edit form"""

    class Meta:
        model = Company
        fields = ['news']
