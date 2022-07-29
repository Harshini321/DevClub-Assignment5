from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import User
from courses_available.models import Courses
from PIL import Image

# Create your models here.

class Course(models.Model):
    title = models.CharField(max_length=6)
    description = models.TextField()
    course_head = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Student(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    courses=models.ManyToManyField(Courses,blank=True)

    def __str__(self):
        return self.user.username

class Instructor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    courses=models.ManyToManyField(Courses,blank=True)

    def __str__(self):
        return self.user.username

class Admin(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    courses=models.ManyToManyField(Courses,blank=True)
    def __str__(self):
        return self.user.username

class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kawrgs):
        super().save(*args,**kawrgs)
        img=Image.open(self.image.path)
        if img.height>300 or img.width>300:
            output_size=(300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

from django.db.models.signals import m2m_changed

def courses_changed(sender,**kwargs):
    u1=User.objects.filter(username='Student1').first()
    s1=Student.objects.filter(user=u1).first()
    c1=Courses.objects.filter(title='MTL100').first()
    s1.courses.add(c1)
m2m_changed.connect(courses_changed,sender=Student.courses.through)

