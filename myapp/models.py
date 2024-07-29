from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUserProfile(AbstractUser):

    SPLIT_METHODS = [
        ('PATIENT', 'PATIENT'),
        ('DOCTOR', 'DOCTOR')
    ]

    user_type = models.CharField(max_length=10, choices=SPLIT_METHODS)
    address = models.TextField(null=True)
    state = models.CharField(max_length=20, null=True)
    pincode = models.IntegerField(null=True)
    profile_picture = models.ImageField(null=True, blank=True, upload_to="static/profile")

    def __str__(self):
        return self.username