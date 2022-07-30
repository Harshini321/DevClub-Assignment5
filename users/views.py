
from django.shortcuts import render,redirect
from django.http import HttpResponse
# forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm,ProfileUpdateForm,UserUpdateForm
from courses_available.models import Courses
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    DetailView,
)
from .models import Course,Student
# Create your views here.


@login_required
def home(request):
    if request.user.is_superuser or request.user.email[0:4]=='prof':
        context={
            'courses':Courses.objects.all()
        }
    else:
        context={
            'courses':Student.objects.filter(user=request.user).first().courses.all()
        }
    return render(request,'users/home.html',context)

@login_required
def allCourses(request):
    context={
        'allCourses':Course.objects.all()
    }
    return render(request,'users/allCourses.html',context)


def register(request):
    if request.method=='POST':
        form=UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your account has been created {username}! You are now able to Login')
            return redirect('login')
    else:
        form=UserRegistrationForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile(request):
    if request.method =='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your profile has been updated! ')
            return redirect('profile')

    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form
    }
    return render(request,'users/profile.html',context)

class CourseDetailView(DetailView):
    model=Course

class ProfileDetailView(DetailView):
    model=Course

