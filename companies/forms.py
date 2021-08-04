from django import forms

from companies.models import Company


class ModeratorEditForm(forms.ModelForm):
    """Staff edit form"""

    class Meta:
        model = Company
        fields = ['description', 'news']


class UserEditForm(forms.ModelForm):
    """User edit form"""

    class Meta:
        model = Company
        fields = ['news']


class AdminEditForm(forms.ModelForm):
    """Staff edit form"""

    class Meta:
        model = Company
        fields = '__all__'