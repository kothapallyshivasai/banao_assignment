from django.contrib import admin

from .models import CustomUserProfile, Blog, Appointment

# Register your models here.
admin.site.register(CustomUserProfile)
admin.site.register(Blog)
admin.site.register(Appointment)