from django.urls import path

from myapp.views import home, doctor_login, logout_user, patient_login, register, doctor_dashboard, patient_dashboard

urlpatterns = [
    path('', home, name="home"),
    path('register', register, name="register"),
    path('doctor-login', doctor_login, name="doctor_login"),
    path('patient-login', patient_login, name="patient_login"),
    path('doctor-dashboard', doctor_dashboard, name="doctor-dashboard"),
    path('patient-dashboard', patient_dashboard, name="patient-dashboard"),
    path('logout/', logout_user, name='logout'),
]
