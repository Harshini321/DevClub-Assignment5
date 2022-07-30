# from django.shortcuts import render
# from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# from .models import Courses
# from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
# # Create your views here.

# class CourseListView(LoginRequiredMixin,ListView):
#     model=Courses
#     # courses_available/coursesavailablle_list.html
#     context_object_name='allCourses'

# class CourseDetailView(LoginRequiredMixin, DetailView):
#     model=Courses
#     # courses_available/coursesavailablle_list.html

# class CourseCreateView(LoginRequiredMixin,UserPassesTestMixin,CreateView):
#     model=Courses
#     fields=['title','description','course_head']

#     def test_func(self):
#         if self.request.user.is_superuser:
#             return True
#         return False

# class CourseUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
#     model=Courses
#     fields=['title','description','course_head']

#     def test_func(self):
#         course=self.get_object()
#         if self.request.user.is_superuser:
#             return True
#         return False

# class CourseDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
#     model=Courses
#     success_url='/home'
#     def test_func(self):
#         if self.request.user.is_superuser:
#             return True
#         return False


from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Courses
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import Student
from django.shortcuts import redirect

# Create your views here.

class CourseListView(LoginRequiredMixin, ListView):
    model = Courses
    # courses_available/coursesavailablle_list.html
    context_object_name = 'allCourses'


class CourseDetailView(LoginRequiredMixin, DetailView):
    model = Courses
    # courses_available/coursesavailablle_list.html


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
        return redirect('courses-available')

    student.courses.add(course)
    return redirect('courses-available')