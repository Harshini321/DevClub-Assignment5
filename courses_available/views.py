from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Courses
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# Create your views here.

class CourseListView(LoginRequiredMixin,ListView):
    model=Courses
    # courses_available/coursesavailablle_list.html
    context_object_name='allCourses'

class CourseDetailView(LoginRequiredMixin, DetailView):
    model=Courses
    # courses_available/coursesavailablle_list.html

class CourseCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
    model=Courses
    fields=['title','description','course_head']

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False

class CourseUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Courses
    fields=['title','description','course_head']

    def test_func(self):
        course=self.get_object()
        if self.request.user.is_superuser:
            return True
        return False

class CourseDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Courses
    success_url='/home'
    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False