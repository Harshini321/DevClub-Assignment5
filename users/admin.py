from django.contrib import admin
from .models import Course,Student,Instructor,Admin,Profile
# Register your models here.

admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Admin)
admin.site.register(Profile)
