from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from datetime import date, datetime, timedelta

class CustomUserProfile(AbstractUser):

    SPLIT_METHODS = [
        ('PATIENT', 'PATIENT'),
        ('DOCTOR', 'DOCTOR')
    ]

    user_type = models.CharField(max_length=10, choices=SPLIT_METHODS)
    address = models.TextField(null=True)
    state = models.CharField(max_length=20, null=True)
    pincode = models.IntegerField(null=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="profile/")

    def __str__(self):
        return self.username
    

class Blog(models.Model):
    
    CATEGORY_METHODS = [
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid-19', 'Covid-19'),
        ('Immunization', 'Immunization')
    ]
    
    author = models.ForeignKey(CustomUserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="blogs/")
    draft = models.BooleanField()
    category_type = models.CharField(max_length=20, choices=CATEGORY_METHODS)
    content = models.TextField()
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if self.author.user_type != 'DOCTOR':
            raise ValidationError('Only doctors can create blogs.')
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Author - {self.author.username}, Category - {self.category_type}"


class Appointment(models.Model):

    APPOINTMENT_CHOICES = [
        ('Not Seen', 'Not Seen'),
        ('Seen', 'Seen'),
        ('Approved', 'Approved'),
        ('Waiting', 'Waiting'),
        ('Completed', 'Completed'),
        ('Rejected', 'Rejected')
    ]

    doctor = models.ForeignKey(CustomUserProfile, on_delete=models.CASCADE, related_name="doctor")
    patient = models.ForeignKey(CustomUserProfile, on_delete=models.CASCADE, related_name="patient")
    doctor_specialization = models.CharField(max_length=100)
    appointment_status = models.CharField(max_length=20, choices=APPOINTMENT_CHOICES)
    appointment_date = models.DateField()
    appointment_end_date = models.DateField(default=None)
    appointment_time = models.TimeField()
    appointment_end_time = models.TimeField()

    def save(self, *args, **kwargs):
        if self.doctor.user_type != 'DOCTOR' and self.patient.user_type != 'PATIENT':
            raise ValidationError('Object cannot be created')
        
        self.appointment_end_time = (datetime.combine(date.today(), self.appointment_time) + timedelta(minutes=45)).time()

        super().save(*args, **kwargs)