from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

def home_view(request):
    return render(request, 'index.html')

User = get_user_model()

def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('mobile')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')


        if password != cpassword:
            messages.error(request, 'Passwords do not match')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered')
        else:
            try:
                validate_password(password)
                User.objects.create_user(
                    email=email,
                    name=name,
                    phone=phone,
                    age=age,
                    gender=gender,
                    password=password
                )
                messages.success(request, 'Registration successful! You can now login.')
                return redirect('login')
            except ValidationError as e:
                for error in e:
                    messages.error(request, error)
    return render(request, 'register.html')



def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        selected_role = request.POST.get('role')


        user = authenticate(request, email=email, password=password)
        if user:
            # Determine if the role matches the actual user status
            if (selected_role == 'admin' and user.is_superuser) or (selected_role == 'user' and not user.is_superuser):
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, "Invalid credentials: Role mismatch")
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html',)


@login_required
def dashboard_view(request):
    return render(request, 'dashboard.html')


@login_required
def logout_view(request):
    logout(request)
    return redirect('home')



@login_required
def view_profile(request):
    if not request.user.is_superuser:
        messages.error(request, "Access denied: You are not authorized to view this page.")
        return redirect('dashboard')  # Redirect to dashboard or home instead of showing raw 403


    return render(request, 'user_profile.html')