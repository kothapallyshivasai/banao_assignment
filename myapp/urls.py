from django.urls import path

from myapp.views import doctor_add_blog, doctor_blogs, doctor_delete_blog, doctor_edit_blog, home, doctor_login, logout_user, patient_login, patient_view_blogs, register, doctor_dashboard, patient_dashboard, patient_view_blog

urlpatterns = [
    path('', home, name="home"),
    
    path('register', register, name="register"),
    path('doctor-login', doctor_login, name="doctor_login"),
    path('patient-login', patient_login, name="patient_login"),

    path('doctor/doctor-dashboard', doctor_dashboard, name="doctor-dashboard"),
    path('doctor/doctor-show-blogs', doctor_blogs, name="doctor-show-blogs"),
    path('doctor/doctor-add-blog', doctor_add_blog, name="doctor-add-blog"),
    path('doctor/doctor-delete-blog/<int:id>', doctor_delete_blog, name="doctor-delete-blog"),
    path('doctor/doctor-edit-blog/<int:id>', doctor_edit_blog, name="doctor-edit-blog"),
    
    path('patient/patient-dashboard', patient_dashboard, name="patient-dashboard"),
    path('patient/patient-view-blogs', patient_view_blogs, name="patient-view-blogs"),
    path('patient/patient-view-blog/<int:id>', patient_view_blog, name="patient-view-blog"),

    path('logout/', logout_user, name='logout'),
]
