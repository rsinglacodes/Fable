from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from .forms import FeedbackForm
from .forms import ContactMessageForm
from .models import feedback
from .models import ContactMessage


def home(request):
    return render(request, 'index.html')

def term(request):
    return render(request, 'terms.html')

def setting(request):
    return render(request, 'setting.html')

# def profile(request):
#     return render(request, 'profile.html')

def help(request):
    return render(request, 'help.html')


def feedback_view(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your feedback!')
            return redirect('thanks')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form})

def contact(request):
    print(f"Request method: {request.method}")
    
    if request.method == 'POST':
        print(f"POST data: {request.POST}")
        
        # Directly create a ContactMessage instance
        try:
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone', '')
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            
            # Validate required fields
            if not name or not email or not message:
                messages.error(request, "Please fill in all required fields.")
                return render(request, 'contact.html')
            
            # Create and save the message
            contact_msg = ContactMessage.objects.create(
                name=name,
                email=email,
                phone=phone,
                subject=subject,
                message=message
            )
            
            print(f"Successfully created message with ID: {contact_msg.id}")
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
            
        except Exception as e:
            print(f"Error saving message: {str(e)}")
            messages.error(request, f"Error: {str(e)}")
            return render(request, 'contact.html')
    
    return render(request, 'contact.html')

def thanks(request):
    return render(request, 'thanks.html')
      


def about(request):
    return render(request, 'about.html')

# def amazing(request):
#     return render(request, 'amazing.html')

def beach(request):
    return render(request, 'beach.html')

def coming(request):
    return render(request, 'coming.html')

def confirm(request):
    return render(request, 'confirm.html')


def data(request):
    return render(request, 'data.html')

def homepage(request):
    return render(request, 'homepage.html')

def luxury(request):
    return render(request, 'luxury.html')

def learn(request):
    return render(request, 'learn.html')

def rooms(request):
    return render(request, 'rooms.html')

def search(request):
    return render(request, 'search.html')