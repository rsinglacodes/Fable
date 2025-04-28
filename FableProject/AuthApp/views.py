from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from .models import AppUser
from .forms import EditProfileForm
from django.contrib.auth import logout
from HotelApp.models import Booking  

def home_view(request):
    return render(request, 'index.html')

def register_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        mobile = request.POST.get('phone')

        if password != cpassword:
            messages.error(request, "Passwords do not match!")
            return redirect('register')
        
        if not all([name, email, age, gender, password, mobile]):
            messages.error(request, "Please fill in all fields!")
            return redirect('register')

        try:
            # Check if user already exists
            if AppUser.objects.filter(email=email).exists():
                messages.error(request, "Email already registered!")
                return redirect('register')

            # Create user
            user = AppUser.objects.create_user(
                email=email,
                name=name,
                phone=mobile,
                age=int(age),
                gender=gender,
                password=password
            )
            messages.success(request, "Registration successful! Please login.")
            return redirect('login')
        except ValidationError as e:
            messages.error(request, str(e))
            return redirect('register')
        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('register')

    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('username')  # This matches your form field name
        password = request.POST.get('password')
        remember = request.POST.get('remember')  # Checkbox value
        
        # Authenticate using email as username
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            if remember in request.POST:
                request.session.set_expiry(1209600)  # 2 weeks
            else:
                request.session.set_expiry(0)  # Browser session
            return redirect('hotel_list')
        else:
            messages.error(request, "Invalid email or password!")
            return redirect('login')
    
    return render(request, 'login.html')




@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login')
def view_profile(request):
    bookings = Booking.objects.filter(user=request.user).order_by('-check_in')
    return render(request, 'profile.html', {
        'user': request.user,
        'bookings': bookings  # Pass bookings to template
    })

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('view_profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

@login_required
def delete_profile(request):
    if request.method == 'POST':
        user = request.user
        user.delete()               # First, delete the user
        logout(request)             # Then logout
        messages.success(request, "Your profile has been deleted.")
        return redirect('home')
    return render(request, 'delete_profile_confirm.html')
