from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Courses
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import Student
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

class CourseListView(LoginRequiredMixin, ListView):
    model = Courses
    context_object_name = 'allCourses'


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Courses


class CourseCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Courses
    fields = ['title', 'description', 'course_head']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


class CourseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Courses
    fields = ['title', 'description', 'course_head']

    def test_func(self):
        course = self.get_object()
        if self.request.user.is_superuser:
            return True
        return False


class CourseDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Courses
    success_url = '/home'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


def add_course(request, pk):
    course = Courses.objects.get(id=pk)
    student = Student.objects.get(user=request.user)
    if student.courses.contains(course):
        # If course is already present
        messages.success(request,f'You are already registered in {course} Course')
        return redirect('courses-available')

    student.courses.add(course)
    messages.success(request,f'You are successfully registered to {course} Course')
    return redirect('courses-available')