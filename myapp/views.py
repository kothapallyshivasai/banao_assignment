from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Appointment, Blog, CustomUserProfile
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
import datetime as dt
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/calendar"]

@never_cache
def home(request):
    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "DOCTOR":
            return redirect("doctor-dashboard")
        
        if user.user_type == "PATIENT":
            return redirect("patient-dashboard")
 
    except Exception as e:
        pass

    return render(request, "index.html", {"active": 1})

@never_cache
def register(request):

    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "DOCTOR":
            return redirect("doctor-dashboard")
        
        if user.user_type == "PATIENT":
            return redirect("patient-dashboard")
 
    except Exception as e:
        pass

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
def doctor_login(request):

    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "DOCTOR":
            return redirect("doctor-dashboard")
        
        if user.user_type == "PATIENT":
            return redirect("patient-dashboard")
 
    except Exception as e:
        pass

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

    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "PATIENT":
            return redirect("patient-dashboard")
 
    except Exception as e:
        pass

    appointments = Appointment.objects.filter(doctor=request.user, appointment_status="Not Seen").count()

    return render(request, "doctor/doctor_dashboard.html", {"active": 1, "count": appointments})

@never_cache
@login_required
def doctor_blogs(request):

    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "PATIENT":
            return redirect("patient-dashboard")
        
    except Exception as e:
        pass

    blogs = Blog.objects.filter(author=request.user)
    paginator = Paginator(blogs, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, "doctor/doctor_blogs.html", {"active": 2, "page_obj": page_obj})

@never_cache
@login_required
def doctor_add_blog(request):

    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "PATIENT":
            return redirect("patient-dashboard")
    
    except Exception as e:
        pass

    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")
        category_type = request.POST.get("category_type")
        content = request.POST.get("content")
        summary = request.POST.get("summary")
        draft = request.POST.get("draft") == "on"
        
        if title and image and category_type and content and summary:
            blog = Blog(
                author=request.user,
                title=title,
                image=image,
                category_type=category_type,
                content=content,
                summary=summary,
                draft=draft
            )
            blog.save()
            messages.success(request, "Blog added successfully.")
            return redirect("doctor-dashboard")
        else:
            messages.error(request, "Something went wrong, Please try again later.")
            return redirect("doctor-add-blog")
    
    return render(request, "doctor/doctor_add_blog.html", {"active": 3})

@never_cache
@login_required
def doctor_delete_blog(request, id):
    blog = Blog.objects.get(id=id, author=request.user)
    blog.image.delete(save=False)
    blog.delete()
    messages.success(request, "Blog Deleted Successfully")
    return redirect("doctor-show-blogs")

@never_cache
@login_required
def doctor_edit_blog(request, id):

    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "PATIENT":
            return redirect("patient-dashboard")
        
    except Exception as e:
        pass

    blog = get_object_or_404(Blog, id=id)
    
    if request.method == "POST":
        title = request.POST.get("title")
        category_type = request.POST.get("category_type")
        content = request.POST.get("content")
        summary = request.POST.get("summary")
        draft = 'draft' in request.POST
        
        image = request.FILES.get("image")
        if image:
            blog.image.delete(save=False)
            blog.image = image
        
        if not title or not content:
            messages.error(request, "Please fill out all required fields.")
            return redirect('doctor-edit-blog', id=id)
        
        blog.title = title
        blog.category_type = category_type
        blog.content = content
        blog.summary = summary
        blog.draft = draft
        blog.save()

        messages.success(request, "Blog updated successfully.")
        return redirect('doctor-show-blogs')

    return render(request, "doctor/doctor_edit_blog.html", {"blog": blog})

@never_cache
@login_required
def doctor_schedule(request):
    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "PATIENT":
            return redirect("patient-dashboard")
        
    except Exception as e:
        pass

    appointments = Appointment.objects.filter(doctor=request.user.id)

    for appointment in appointments:
        now = dt.datetime.now()
        appointment_end_datetime = dt.datetime.combine(appointment.appointment_end_date, appointment.appointment_end_time)
        
        if now >= appointment_end_datetime and appointment.appointment_status != 'Completed':
            appointment.appointment_status = 'Completed'
            appointment.save()

    paginator = Paginator(appointments, 8)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, "doctor/schedule.html", {"active": 4, "appointments": page_obj})

@never_cache
@login_required
def doctor_requested_appointments(request):
    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "PATIENT":
            return redirect("patient-dashboard")
        
    except Exception as e:
        pass

    appointments = Appointment.objects.filter(doctor=request.user, appointment_status__in=["Not Seen", "Seen"])
    appointments.update(appointment_status="Seen")
    
    return render(request, "doctor/requested_appointments.html", {"active": 5, "appointments": appointments})

@never_cache
@login_required
def doctor_appointment_approve(request, id):
    try:
        appointment = Appointment.objects.get(pk=id, doctor=request.user)

        start_datetime = dt.datetime.combine(appointment.appointment_date, appointment.appointment_time).isoformat()
        end_datetime = dt.datetime.combine(appointment.appointment_end_date, appointment.appointment_end_time).isoformat()

        event = {
            'summary': f'Appointment with {appointment.doctor.first_name} {appointment.doctor.last_name} - {id}',
            'location': 'Online',
            'description': f'Speciality: {appointment.doctor_specialization}',
            'start': {
                'dateTime': f"{start_datetime}Z",
                'timeZone': 'Asia/Kolkata',
            },
            'end': {
                'dateTime': f"{end_datetime}Z",
                'timeZone': 'Asia/Kolkata',
            },
            'attendees': [
                {'email': appointment.patient.email},
                {'email': appointment.doctor.email},
            ],
            'organizer': {
                'email': appointment.doctor.email,
            },
        }

        creds = None

        if os.path.exists("token.json"):
            try:
                creds = Credentials.from_authorized_user_file("token.json", SCOPES)
            except Exception as e:
                print(f"Error loading credentials from file: {e}")

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token: 
                try:
                    creds.refresh(Request())
                except Exception as e:
                    print(f"Error refreshing credentials: {e}")
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials-desk.json", SCOPES)
                creds = flow.run_local_server(port=0)
            
            if creds:
                with open("token.json", "w") as token:
                    token.write(creds.to_json())
            else:
                print("Failed to obtain credentials")
                messages.error(request, "Something went wrong, Please try again later!")
                return redirect("doctor-requested-appointments")

        try:
            service = build('calendar', 'v3', credentials=creds)
            event_result = service.events().insert(calendarId='primary', body=event).execute()
            messages.success(request, "Appointment has been Accepted!")

            appointment.appointment_status = "Approved"
            appointment.save()

            return redirect("doctor-requested-appointments")
        except HttpError as error:
            print(f'An error occurred: {error}')
            messages.error(request, "Something went wrong, Please try again later!")
            return redirect("doctor-requested-appointments")

    except Appointment.DoesNotExist:
        messages.error(request, "Appointment does not exist.")
        return redirect("doctor-requested-appointments")
    except Exception as e:
        print(f'An error occurred: {e}')
        messages.error(request, "Something went wrong, Please try again later!")
        return redirect("doctor-requested-appointments")
    
@never_cache
@login_required 
def doctor_appointment_rejected(request, id):
    appointment = Appointment.objects.get(pk=id, doctor=request.user)
    appointment.appointment_status = "Rejected"
    appointment.save()
    messages.info(request, "Appointment has been Rejected!")
    return redirect("doctor-requested-appointments")

@never_cache
@login_required
def patient_dashboard(request):

    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "DOCTOR":
            return redirect("doctor-dashboard")
        
    except Exception as e:
        pass

    rejected_appointments = Appointment.objects.filter(patient=request.user, appointment_status="Rejected")
    approved_appointments = Appointment.objects.filter(patient=request.user, appointment_status="Approved")
    
    if request.method == "POST" and request.POST.get('update_status'):
        approved_appointments.update(appointment_status="Done")
        rejected_appointments.delete()

    return render(request, "patient/patient_dashboard.html", {"active": 1, "rejected_appointments": rejected_appointments, 
                            "approved_appointments": approved_appointments})

@never_cache
@login_required
def patient_view_blogs(request):

    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "DOCTOR":
            return redirect("doctor-dashboard")
        
    except Exception as e:
        pass

    category_type = request.POST.get('category_type', None)
    
    if request.method == "POST":
        if category_type:
            blogs = Blog.objects.filter(draft=False, category_type=category_type)
        else:
            blogs = Blog.objects.filter(draft=False)
        
        paginator = Paginator(blogs, 2)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        
        return render(request, "patient/patient_view_blogs.html", {
            "active": 2, 
            "page_obj": page_obj, 
            "selected_category": category_type
        })
    
    blogs = Blog.objects.filter(draft=False)
    paginator = Paginator(blogs, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    
    return render(request, "patient/patient_view_blogs.html", {
        "active": 2, 
        "page_obj": page_obj, 
        "selected_category": None
    })

@never_cache
def patient_login(request):

    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "DOCTOR":
            return redirect("doctor-dashboard")
        
        if user.user_type == "PATIENT":
            return redirect("patient-dashboard")
        
    except Exception as e:
        pass

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
@login_required
def patient_view_blog(request, id):

    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "DOCTOR":
            return redirect("doctor-dashboard")
        
    except Exception as e:
        pass

    blog = Blog.objects.get(id=id, draft=False)
    return render(request, "patient/patient_view_blog.html", {"blog": blog})

@never_cache
@login_required
def patient_your_appointments(request):

    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "DOCTOR":
            return redirect("doctor-dashboard")
        
    except Exception as e:
        pass

    appointments = Appointment.objects.filter(patient=request.user.id)

    for appointment in appointments:
        now = dt.datetime.now()
        appointment_end_datetime = dt.datetime.combine(appointment.appointment_end_date, appointment.appointment_end_time)
        
        if now >= appointment_end_datetime and appointment.appointment_status != 'Completed':
            appointment.appointment_status = 'Completed'
            appointment.save()

    paginator = Paginator(appointments, 8)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, "patient/your_appointments.html", {"appointments": page_obj, "active": 3})

@never_cache
@login_required
def patient_book_appointment(request):
    try:
        user = request.user
        if user.is_superuser:
            return redirect("/admin")
        
        if user.user_type == "DOCTOR":
            return redirect("doctor-dashboard")
        
    except Exception as e:
        pass

    if request.method == "POST":
        appointment_date_str = request.POST.get('date')
        start_time_str = request.POST.get('start_time')

        appointment_date = dt.datetime.strptime(appointment_date_str, '%Y-%m-%d').date()
        start_time = dt.datetime.strptime(start_time_str, '%H:%M').time()

        now = dt.datetime.now()
        appointment_start_datetime = dt.datetime.combine(appointment_date, start_time)

        if appointment_date < now.date() or (appointment_date == now.date() and start_time < now.time()):
            messages.error(request, "Appointment date or time cannot be in the past.")
            return redirect("patient-book-appointment")

        appointment = Appointment()
        appointment.doctor = CustomUserProfile.objects.get(username=request.POST.get('doctor_username'))
        appointment.patient = request.user
        appointment.doctor_specialization = request.POST.get('speciality')
        appointment.appointment_status = "Not Seen"

        appointment.appointment_date = appointment_date
        appointment.appointment_time = start_time

        appointment_end_datetime = appointment_start_datetime + dt.timedelta(minutes=45)
        appointment_end_time = appointment_end_datetime.time()

        appointment.appointment_end_time = appointment_end_time
        appointment.appointment_end_date = appointment_end_datetime.date()

        appointment.save()
        
        messages.info(request, "Appointment was sent, Please wait until doctor responds.")
        return redirect("patient-dashboard")

    doctors = CustomUserProfile.objects.filter(user_type="DOCTOR")
    paginator = Paginator(doctors, 6)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    return render(request, "patient/book_appointment.html", {"doctors": page_obj, "active": 4})

@login_required
def logout_user(request):
    logout(request)
    return redirect('home')

