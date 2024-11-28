from django import forms
from profile_app.models import Profile

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic', 'gender', 'age']

        widgets = {
            'gender': forms.Select(choices=[('M', 'Male'), ('F', 'Female')]),
            'age': forms.NumberInput(attrs={'min': 0}),
        }

