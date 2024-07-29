from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import CustomUserProfile
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache

@never_cache
def home(request):
    return render(request, "index.html", {"active": 1})

@never_cache
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email-id')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        user_type = request.POST.get('user-type')
        address = request.POST.get('address')
        state = request.POST.get('state')
        pincode = request.POST.get('pincode')
        profile_picture = request.FILES.get('profile-picture')

        if password1 != password2:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if CustomUserProfile.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        if CustomUserProfile.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return redirect('register')

        user = CustomUserProfile.objects.create_user(
            username=username,
            email=email,
            password=password1,
            first_name=first_name,
            last_name=last_name,
            user_type=user_type,
            address=address,
            state=state,
            pincode=pincode,
            profile_picture=profile_picture
        )

        user = authenticate(request, username=username, password=password1)
        if user is not None:
            login(request, user)
            messages.success(request, "Registration successful!")
            if user.user_type == "DOCTOR":
                return redirect('doctor-dashboard')
            return redirect('patient-dashboard')
            
    return render(request, "register.html", {"active": 3})

@never_cache
def patient_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.user_type == 'PATIENT':
            login(request, user)
            return redirect('patient-dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('patient_login')
    
    return render(request, "patient_login.html", {"active": 2})

@never_cache
def doctor_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None and user.user_type == 'DOCTOR':
            login(request, user)
            return redirect('doctor-dashboard')
        else:
            messages.error(request, "Invalid username or password.")
            return redirect('doctor_login')
    
    return render(request, "doctor_login.html", {"active": 4})

@never_cache
@login_required
def doctor_dashboard(request):
    return render(request, "doctor_dashboard.html", {})

@never_cache
@login_required
def patient_dashboard(request):
    return render(request, "patient_dashboard.html", {})

def logout_user(request):
    logout(request)
    return redirect('home')
