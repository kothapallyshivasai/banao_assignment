from django.urls import path

from myapp.views import doctor_add_blog, doctor_appointment_approve, doctor_appointment_rejected, doctor_blogs, doctor_delete_blog, doctor_edit_blog, doctor_requested_appointments, doctor_schedule, home, doctor_login, logout_user, patient_login, patient_view_blogs, register, doctor_dashboard, patient_dashboard, patient_view_blog, patient_book_appointment, patient_your_appointments

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
    path('doctor/doctor-schedule', doctor_schedule, name="doctor-schedule"),
    path('doctor/doctor-requested-appointments', doctor_requested_appointments, name="doctor-requested-appointments"),
    path('doctor/doctor-appointment-approve/<int:id>', doctor_appointment_approve, name="doctor-appointment-approve"),
    path('doctor/doctor-appointment-rejected/<int:id>', doctor_appointment_rejected, name="doctor-appointment-rejected"),
    
    path('patient/patient-dashboard', patient_dashboard, name="patient-dashboard"),
    path('patient/patient-view-blogs', patient_view_blogs, name="patient-view-blogs"),
    path('patient/patient-view-blog/<int:id>', patient_view_blog, name="patient-view-blog"),
    path('patient/patient-your-appointments', patient_your_appointments, name="patient-your-appointments"),
    path('patient/patient-book-appointment', patient_book_appointment, name="patient-book-appointment"),

    path('logout/', logout_user, name='logout'),
]
