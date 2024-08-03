from django.core.paginator import Paginator
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Blog, CustomUserProfile
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
    return render(request, "doctor/doctor_dashboard.html", {"active": 1})

@never_cache
@login_required
def doctor_blogs(request):
    blogs = Blog.objects.filter(author=request.user)
    paginator = Paginator(blogs, 2)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    return render(request, "doctor/doctor_blogs.html", {"active": 2, "page_obj": page_obj})

@never_cache
@login_required
def doctor_add_blog(request):
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
def patient_dashboard(request):
    return render(request, "patient/patient_dashboard.html", {"active": 1})

@never_cache
@login_required
def patient_view_blogs(request):
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
@login_required
def patient_view_blog(request, id):
    blog = Blog.objects.get(id=id, draft=False)
    return render(request, "patient/patient_view_blog.html", {"blog": blog})

def logout_user(request):
    logout(request)
    return redirect('home')
