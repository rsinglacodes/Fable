from django import forms
from .models import feedback
from .models import ContactMessage

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = feedback
        fields = ['name', 'email', 'comment']
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
        }

# forms.py
class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'name',
                'required': True
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'id': 'email',
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'phone'
            }),
            'subject': forms.Select(attrs={
                'class': 'form-control',
                'id': 'subject'
            }, choices=[
                ('reservation', 'Reservation Inquiry'),
                ('feedback', 'Feedback'),
                ('support', 'General Support'),
                ('partnership', 'Business Partnership'),
                ('other', 'Other')
            ]),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'id': 'message',
                'required': True
            }),
        }