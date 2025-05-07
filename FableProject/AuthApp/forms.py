from django import forms
from .models import AppUser

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = AppUser
        fields = ['name', 'phone', 'age', 'gender', 'role']  # Add 'role' if you want it editable
