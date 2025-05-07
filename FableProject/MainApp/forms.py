from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'comment', 'suggestion']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Name',
                'id': 'id_name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Your Email',
                'id': 'id_email'
            }),
            'comment': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Share your feedback with us...',
                'rows': 4,
                'id': 'id_comment'
            }),
            'suggestion': forms.Textarea(attrs={
                'class': 'form-control', 
                'placeholder': 'Share your suggestions with us...',
                'rows': 4,
                'id': 'id_suggestion'
            }),
        }