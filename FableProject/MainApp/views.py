from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
import random
from .forms import FeedbackForm
from .models import feedback


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
    # if request.method == 'POST':
    #     form = ContactMessageForm(request.POST)
    #     if form.is_valid():
    #         form.save()  # Save the data to the database
    #         return messages.success(request, 'Thank you for your message! We will get back to you soon.')
            
    #     else:
    #         messages.error(request, 'Please correct the errors below.')
    # else:
    #     form = ContactMessageForm()
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