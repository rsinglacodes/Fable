from django import forms
from .models import feedback
from .models import ContactMessage

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['name', 'email', 'comment']  # Make sure these match your model fields
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Your Feedback', 'rows': 4}),
           
        }






class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']