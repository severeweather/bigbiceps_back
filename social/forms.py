from django import forms

from .models import UserSocialProfile

class UserSocialProfileForm(forms.ModelForm):
    class Meta:
        model = UserSocialProfile
        fields = [
            'bio',
            'pfp'
        ]