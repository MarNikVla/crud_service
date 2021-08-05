from django import forms

from companies.models import Company


class ModeratorEditForm(forms.ModelForm):
    """Moderator edit form"""

    class Meta:
        model = Company
        fields = ['description', 'news', 'foundation_date', 'avatar']


class UserEditForm(forms.ModelForm):
    """User edit form"""

    class Meta:
        model = Company
        fields = ['news']


class AdminEditForm(forms.ModelForm):
    """Admin edit form"""

    class Meta:
        model = Company
        fields = '__all__'
